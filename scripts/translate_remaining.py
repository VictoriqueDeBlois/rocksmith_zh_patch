"""翻译 Rocksmith 2014 剩余英文文本 (可并行使用多台 ollama / 自定义模型)。

与旧脚本 translate_new_strings.py 相比:
- 不只翻译 learnplay 新增 id, 而是翻译“全部仍为英文”的 id
  (含汉化组未汉化的旧 id 与所有新增 id);
- 支持 config/workers.json 配置多台 ollama 服务(本机 + 服务器), 进程内并行;
- 按英文原文去重后翻译, 断点续传, 每批落盘;
- 自动拆分/还原 {C} {B} {L} [1] 等占位符, 保证占位符不丢失;
- 单批失败自动降级为逐条翻译, 个别顽固条目记录到 .failed.json 不影响整体。

用法示例:
  python scripts/translate_remaining.py ^
      --legacy legacy_cache4/localization/maingame.csv ^
      --current learnplay_cache4/localization/maingame.csv ^
      --existing data/translations_merged.json ^
      --out data/translations_remaining.json ^
      --config config/workers.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

from localization import (
    PLACEHOLDER_RE,
    is_translatable,
    load_json,
    load_legacy_translations,
    load_slots,
    write_json,
)

TRANSLATION_SYSTEM = (
    "你是 Rocksmith 2014 游戏本地化译者，把英文游戏文本翻译成自然、简洁的简体中文。\n"
    "规则：\n"
    "1. 输入是一组独立文本片段，每个片段带唯一 id；输出 translations 数组的数量必须与输入完全一致，且 id 一一对应，不得合并、遗漏或新增项目。\n"
    "2. 保留所有占位符原样：{C} {B} {L} {X} {Y} {A} {0} {1} 以及 [1] [2] 等。\n"
    "3. 保留品牌与专有名词：Rocksmith、Ubisoft、Uplay、Steam、PSN、Xbox LIVE、PlayStation、Nintendo、Real Tone Cable、iTunes 等。\n"
    "4. 音名、和弦记号（如 Am、C#7、A♭）、歌曲名、艺人名、DLC 包名不翻译。\n"
    "5. 术语统一：tuning=调弦，fret=品，capo=变调夹，arrangement=编曲，Lead=主音，Rhythm=节奏，Bass=贝斯，tone=音色，calibration=校准，riff=乐句，phrase=乐句，score attack=得分挑战，Learn a Song=学习歌曲，Guitarcade=吉他街机，Session Mode=即兴演奏，amp=音箱，pedal=效果器，chord=和弦，note=音符，string=琴弦，pickup=拾音器，volume=音量。\n"
    "6. 译文中不要使用半角逗号 ,（请改用中文逗号，），不要包含换行。\n"
    "7. 只返回符合指定结构的 JSON，不要输出任何解释。"
)


def load_workers(config_path: Path) -> list[dict]:
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    workers = cfg.get("workers") or []
    if not workers:
        raise SystemExit(f"config {config_path} 中没有 workers")
    for w in workers:
        w.setdefault("concurrency", 1)
        w.setdefault("weight", 1)
        w.setdefault("batch_size", 24)
        w.setdefault("timeout", 900)
    return workers


def split_for_translation(batch: list[dict]) -> tuple[list[dict], dict]:
    """把含占位符的文本切成纯文本段, 返回 (请求段列表, 还原计划)。"""
    request_items: list[dict] = []
    plans: dict[str, list] = {}
    for item in batch:
        pieces = re.split(f"({PLACEHOLDER_RE.pattern})", item["text"])
        plan: list[tuple[str, str]] = []
        seg_no = 0
        for piece in pieces:
            if not piece:
                continue
            if PLACEHOLDER_RE.fullmatch(piece):
                plan.append(("literal", piece))
            else:
                seg_id = f'{item["id"]}S{seg_no}'
                request_items.append({"id": seg_id, "text": piece})
                plan.append(("segment", seg_id))
                seg_no += 1
        plans[item["id"]] = plan
    return request_items, plans


def validate(source: str, translated: str) -> tuple[bool, str]:
    if sorted(PLACEHOLDER_RE.findall(source)) != sorted(PLACEHOLDER_RE.findall(translated)):
        return False, "placeholder mismatch"
    if not translated.strip():
        return False, "empty translation"
    if "\n" in translated or "\r" in translated:
        return False, "embedded newline"
    return True, ""


def chat_once(endpoint: str, model: str, system: str, request_items: list[dict],
              schema: dict, timeout: int, num_ctx: int = 8192) -> dict:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(request_items, ensure_ascii=False)},
        ],
        "stream": False,
        "think": False,
        "format": schema,
        "keep_alive": "30m",
        "options": {"temperature": 0, "num_ctx": num_ctx, "num_predict": 4096},
    }
    req = urllib.request.Request(
        endpoint.rstrip("/") + "/api/chat",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        result = json.load(resp)
    return json.loads(result["message"]["content"])


TRANSLATION_SCHEMA = {
    "type": "object",
    "properties": {
        "translations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"id": {"type": "string"}, "text": {"type": "string"}},
                "required": ["id", "text"],
            },
        }
    },
    "required": ["translations"],
}


def restore_and_map(endpoint: str, model: str, batch: list[dict], timeout: int) -> dict[str, str]:
    """翻译一个 batch, 返回 {short_id: translated}。失败抛异常。

    注意: 模型有时会打乱返回顺序, 因此严格按 id 匹配, 不能依赖数组顺序。
    """
    request_items, plans = split_for_translation(batch)
    if not request_items:
        return {it["id"]: it["text"] for it in batch}
    result = chat_once(endpoint, model, TRANSLATION_SYSTEM, request_items,
                       TRANSLATION_SCHEMA, timeout)
    items = result["translations"]
    expected_ids = [it["id"] for it in request_items]
    if len(items) != len(expected_ids):
        raise ValueError(f"Segment count mismatch: expected {len(expected_ids)}, got {len(items)}")
    seg_by_id: dict[str, str] = {}
    for it in items:
        rid = it.get("id")
        if rid in seg_by_id:
            raise ValueError(f"duplicate returned id: {rid}")
        seg_by_id[rid] = it["text"]
    missing = [eid for eid in expected_ids if eid not in seg_by_id]
    if missing:
        raise ValueError(f"missing returned ids: {missing}")
    restored = {}
    for item in batch:
        translated = "".join(
            value if kind == "literal" else seg_by_id[value]
            for kind, value in plans[item["id"]]
        )
        ok, reason = validate(item["text"], translated)
        if not ok:
            raise ValueError(f'{item["id"]}: {reason}')
        restored[item["id"]] = translated
    return restored


def text_done(text: str, done: dict, text_to_ids: dict) -> bool:
    return all(sid in done for sid in text_to_ids[text])


def translate_worker(worker: dict, texts: list[str], text_to_ids: dict,
                     done: dict, out_part: Path, failed_out: Path | None) -> None:
    endpoint = worker["endpoint"]
    model = worker["model"]
    name = worker["name"]
    batch_size = int(worker.get("batch_size", 24))
    timeout = int(worker.get("timeout", 900))
    max_chars = 15000  # 防止长文本把请求撑爆 num_ctx

    pending = [t for t in texts if not text_done(t, done, text_to_ids)]
    total = len(pending)
    print(f"[{name}] worker start: {model} @ {endpoint} | pending unique texts: {total}", flush=True)
    if total == 0:
        return

    # 给每条文本一个稳定且短小的 id, 避免把整段原文塞进 id 导致模型出错
    short_id = {}
    id_to_text = {}
    for i, text in enumerate(sorted(texts)):
        sid = f"T{i:06d}"
        short_id[text] = sid
        id_to_text[sid] = text

    batch: list[dict] = []
    batch_chars = 0
    batch_index = 0
    failed_log: dict[str, str] = {}

    def commit(received: dict[str, str]):
        for canonical_short, translated in received.items():
            source = id_to_text[canonical_short]
            translated = translated.replace(",", "，")
            for sid in text_to_ids[source]:
                done[sid] = translated
        write_json(out_part, dict(done))
        if failed_out is not None:
            write_json(failed_out, failed_log)

    def flush():
        nonlocal batch, batch_chars, batch_index
        if not batch:
            return
        received = None
        last_error = ""
        for attempt in range(1, 4):
            try:
                received = restore_and_map(endpoint, model, batch, timeout)
                break
            except Exception as exc:
                received = None
                last_error = str(exc)
                print(f"[{name}] batch {batch_index + 1} attempt {attempt} failed: {last_error}", flush=True)
                time.sleep(attempt * 3)
        if received is None:
            # 降级: 逐条翻译, 避免一条坏数据拖垮整批
            received = {}
            print(f"[{name}] batch {batch_index + 1} -> fallback per-item ...", flush=True)
            for item in batch:
                ok = False
                for attempt in range(1, 4):
                    try:
                        got = restore_and_map(endpoint, model, [item], timeout)
                        received[item["id"]] = got[item["id"]]
                        ok = True
                        break
                    except Exception as exc:
                        last_error = str(exc)
                        time.sleep(attempt * 2)
                if not ok:
                    failed_log[item["id"]] = last_error
                    print(f"[{name}] FAILED text: {id_to_text[item['id']][:90]!r} ({last_error})", flush=True)
        commit(received)
        batch_index += 1
        print(f"[{name}] batch {batch_index}: {len(received)} texts -> saved {len(done)} ids"
              f"{' | failed ' + str(len(failed_log)) if failed_log else ''}", flush=True)
        batch = []
        batch_chars = 0

    for text in pending:
        sid = short_id[text]
        if batch and batch_chars + len(text) > max_chars:
            flush()
        batch.append({"id": sid, "text": text})
        batch_chars += len(text)
        if len(batch) >= batch_size:
            flush()
    flush()
    print(f"[{name}] worker done: {len(done)} ids saved to {out_part}"
          f"{' | failed ' + str(len(failed_log)) if failed_log else ''}", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Translate remaining English text of Rocksmith 2014")
    ap.add_argument("--legacy", required=True, help="老版(汉化组) maingame.csv")
    ap.add_argument("--current", required=True, help="当前(learnplay) maingame.csv")
    ap.add_argument("--existing", action="append", default=[], help="已完成的翻译 json (可多个)")
    ap.add_argument("--out", required=True, help="输出 translations json")
    ap.add_argument("--config", required=True, help="workers 配置文件")
    ap.add_argument("--worker", default=None, help="只运行指定 name 的 worker")
    ap.add_argument("--merge-only", action="store_true", help="只把 part 文件合并到 --out")
    ap.add_argument("--dry-run", action="store_true", help="只统计, 不调用 ollama")
    args = ap.parse_args()

    legacy_zh = load_legacy_translations(Path(args.legacy))
    current = load_slots(Path(args.current))

    covered: set[str] = set(legacy_zh)
    for existing in args.existing:
        covered.update(load_json(Path(existing)).keys())

    remaining_ids = [
        sid for sid, text in current.items()
        if sid not in covered and is_translatable(text)
    ]
    text_to_ids: dict[str, list[str]] = defaultdict(list)
    for sid in remaining_ids:
        text_to_ids[current[sid]].append(sid)
    texts = sorted(text_to_ids)
    print(f"legacy(汉化组) ids: {len(legacy_zh)} | covered by existing json: {len(covered - set(legacy_zh))}", flush=True)
    print(f"remaining ids: {len(remaining_ids)} | unique texts: {len(texts)}", flush=True)
    if args.dry_run:
        for t in texts[:20]:
            print("  ", t[:100])
        return

    workers = load_workers(Path(args.config))
    if args.worker:
        workers = [w for w in workers if w["name"] == args.worker]
        if not workers:
            raise SystemExit(f"worker '{args.worker}' not found in config")
    if args.merge_only:
        merged: dict[str, str] = {}
        for w in workers:
            part = Path(str(args.out).replace(".json", f".part.{w['name']}.json"))
            if part.exists():
                merged.update(load_json(part))
        write_json(Path(args.out), merged)
        print(f"merged parts -> {args.out}: {len(merged)} ids")
        return

    out_path = Path(args.out)
    failed_path = Path(str(args.out).replace(".json", ".failed.json"))
    if len(workers) == 1:
        worker = workers[0]
        done = load_json(out_path)
        translate_worker(worker, texts, text_to_ids, done, out_path, failed_path)
        missing = [t for t in texts if not text_done(t, done, text_to_ids)]
        if missing:
            print(f"警告: 仍有 {len(missing)} 条文本未翻译, 见 {failed_path}", file=sys.stderr)
            raise SystemExit(2)
        print(f"Complete: {len(done)} ids -> {out_path}", flush=True)
        return

    total_weight = sum(int(w.get("weight", 1)) for w in workers)
    # 若之前用单 worker 直接写过 --out, 把已完成部分按文本归属预填到各 part, 便于续传
    main_done = load_json(out_path) if out_path.exists() else {}
    threads = []
    for idx, w in enumerate(workers):
        start = sum(int(workers[j].get("weight", 1)) for j in range(idx)) * len(texts) // total_weight
        end = sum(int(workers[j].get("weight", 1)) for j in range(idx + 1)) * len(texts) // total_weight
        slice_texts = texts[start:end]
        part_path = Path(str(out_path).replace(".json", f".part.{w['name']}.json"))
        fpart = Path(str(out_path).replace(".json", f".part.{w['name']}.failed.json"))
        done = load_json(part_path)
        if main_done:
            for text in slice_texts:
                for sid in text_to_ids[text]:
                    if sid in main_done:
                        done[sid] = main_done[sid]
        th = threading.Thread(
            target=translate_worker,
            args=(w, slice_texts, text_to_ids, done, part_path, fpart),
            daemon=True,
        )
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    merged = {}
    for w in workers:
        part = Path(str(out_path).replace(".json", f".part.{w['name']}.json"))
        merged.update(load_json(part))
    write_json(out_path, merged)
    print(f"All workers complete: {len(merged)} ids -> {out_path}")


if __name__ == "__main__":
    main()
