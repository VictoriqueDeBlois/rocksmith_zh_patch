"""用 ollama 校对之前由 AI 生成的翻译(汉化组人工汉化的条目自动跳过)。

用法:
  python scripts/proofread_translations.py ^
      --current learnplay_cache4/localization/maingame.csv ^
      --translations data/translations_ai.json ^
      --skip data/translations_legacy.json ^
      --out data/translations_proofread.json ^
      --changes data/proofread_changes.json ^
      --config config/workers.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

from localization import (
    PLACEHOLDER_RE,
    load_json,
    load_slots,
    write_json,
)

PROOFREAD_SYSTEM = (
    "你是 Rocksmith 2014 中文汉化的资深校对。下面给出若干组 {英文原文 -> 现有中文译文}，"
    "请逐条校对并修正错译、漏译、术语不统一、占位符丢失、错别字与不通顺之处；"
    "如果译文已经准确自然，就原样返回。\n"
    "规则：\n"
    "1. 每个 id 一一对应输出，输出数量与输入完全一致，不得合并、遗漏或新增。\n"
    "2. 保留 {C} {B} {L} {X} {Y} {A} {0} {1} 与 [1] [2] 等占位符原样。\n"
    "3. 保留 Rocksmith、Ubisoft、Uplay、Steam、PSN、Xbox LIVE、PlayStation、Real Tone Cable 等品牌名，"
    "音名/和弦记号/歌曲名/艺人名不翻译。\n"
    "4. 术语统一：tuning=调弦，fret=品，capo=变调夹，arrangement=编曲，Lead=主音，Rhythm=节奏，Bass=贝斯，tone=音色，calibration=校准。\n"
    "5. 不要使用半角逗号 ,（用中文逗号，），不要包含换行。\n"
    "6. 只返回符合指定结构的 JSON，不要输出任何解释。"
)

PROOFREAD_SCHEMA = {
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


def chat_once(endpoint: str, model: str, items: list[dict], timeout: int) -> dict:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": PROOFREAD_SYSTEM},
            {"role": "user", "content": json.dumps(items, ensure_ascii=False)},
        ],
        "stream": False,
        "think": False,
        "format": PROOFREAD_SCHEMA,
        "keep_alive": "30m",
        "options": {"temperature": 0, "num_ctx": 8192, "num_predict": 4096},
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


def proofread_batch(endpoint: str, model: str, batch: list[dict], timeout: int) -> list[dict]:
    items = [
        {"id": it["id"], "source": it["source"], "translation": it["translation"]}
        for it in batch
    ]
    result = chat_once(endpoint, model, items, timeout)
    out = result["translations"]
    expected = [it["id"] for it in batch]
    if len(out) != len(expected):
        raise ValueError(f"count mismatch: expected {len(expected)}, got {len(out)}")
    by_id: dict[str, str] = {}
    for x in out:
        rid = x.get("id")
        if rid in by_id:
            raise ValueError(f"duplicate id: {rid}")
        by_id[rid] = x.get("text", "")
    missing = [eid for eid in expected if eid not in by_id]
    if missing:
        raise ValueError(f"missing ids: {missing}")
    return [{"id": eid, "text": by_id[eid]} for eid in expected]


def validate(translated: str) -> tuple[bool, str]:
    if not translated.strip():
        return False, "empty"
    if "\n" in translated or "\r" in translated:
        return False, "embedded newline"
    return True, ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", required=True, help="当前(learnplay) maingame.csv, 提供英文原文")
    ap.add_argument("--translations", required=True, help="待校对的 AI 翻译 json")
    ap.add_argument("--skip", action="append", default=[], help="跳过这些 json 中的 id (如汉化组翻译)")
    ap.add_argument("--out", required=True, help="校对结果 json")
    ap.add_argument("--changes", default=None, help="变动明细 json (id -> {source, before, after})")
    ap.add_argument("--config", required=True, help="workers.json")
    ap.add_argument("--worker", default=None, help="只使用指定 worker")
    ap.add_argument("--batch-size", type=int, default=20)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    current = load_slots(Path(args.current))
    translations = load_json(Path(args.translations))
    skip: set[str] = set()
    for p in args.skip:
        skip.update(load_json(Path(p)).keys())

    todo = []
    for sid in sorted(translations, key=int):
        if sid in skip:
            continue
        source = current.get(sid)
        if source is None:
            print(f"警告: {sid} 不在当前 CSV 中, 跳过", file=sys.stderr)
            continue
        todo.append({"id": sid, "source": source, "translation": translations[sid]})
    print(f"待校对条目: {len(todo)} (跳过汉化组/其他: {len(skip & set(translations))})", flush=True)
    if args.dry_run:
        return

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    workers = cfg["workers"]
    if args.worker:
        workers = [w for w in workers if w["name"] == args.worker]
    if not workers:
        raise SystemExit("no worker available")
    worker = workers[0]  # 校对只用一个模型, 避免多模型互相覆盖
    endpoint, model = worker["endpoint"], worker["model"]
    timeout = int(worker.get("timeout", 900))

    done = load_json(Path(args.out))
    changes: dict[str, dict] = {}
    if args.changes and Path(args.changes).exists():
        changes = json.loads(Path(args.changes).read_text(encoding="utf-8"))

    batch = []
    idx = 0
    def flush():
        nonlocal batch, idx
        if not batch:
            return
        expected = {it["id"]: it for it in batch}
        received = None
        last_error = ""
        for attempt in range(1, 4):
            try:
                candidate = proofread_batch(endpoint, model, batch, timeout)
                received = {it["id"]: it["text"].strip() for it in candidate}
                for it in batch:
                    ok, reason = validate(received[it["id"]])
                    if not ok:
                        raise ValueError(f"{it['id']}: {reason}")
                break
            except Exception as exc:
                received = None
                last_error = str(exc)
                print(f"batch {idx + 1} attempt {attempt} failed: {last_error}", flush=True)
                time.sleep(attempt * 3)
        if received is None:
            raise RuntimeError(f"proofread failed: {last_error}")
        for sid, text in received.items():
            text = text.replace(",", "，")
            before = expected[sid]["translation"]
            if text != before:
                changes[sid] = {
                    "source": expected[sid]["source"],
                    "before": before,
                    "after": text,
                }
            done[sid] = text
        write_json(Path(args.out), done)
        if args.changes:
            write_json(Path(args.changes), changes)
        idx += 1
        print(f"batch {idx}: proofread {len(batch)} -> total {len(done)}", flush=True)
        batch = []

    for it in todo:
        if it["id"] in done:
            continue
        batch.append(it)
        if len(batch) >= args.batch_size:
            flush()
    flush()
    print(f"proofread complete: {len(done)} entries, changed {len(changes)} -> {args.out}", flush=True)


if __name__ == "__main__":
    main()
