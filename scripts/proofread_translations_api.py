r"""用 DeepSeek V4 Flash (API) 校对 AI 译文，跳过汉化组人工译文。

与 ollama 版 proofread_translations.py 不同：
- 走 DeepSeek 官方 OpenAI 兼容 API（比本机 ollama 更强，交叉校对）；
- 支持并发、断点续传、每批落盘；
- 支持 --limit/--seed 抽样，先小样对比再决定全量。

用法:
  1) 复制 config/api.example.json 为 config/api.json，填入 api_key：
       copy config\api.example.json config\api.json   # 然后编辑 api_key
  2) 抽样 100 条对比：
       uv run python scripts\proofread_translations_api.py ^
           --current learnplay_cache4\localization\maingame.csv ^
           --translations data\translations_remaining.json ^
           --skip data\translations_legacy.json ^
           --out data\proofread_sample.json ^
           --changes data\proofread_sample_changes.json ^
           --api-config config\api.json --limit 100 --seed 42
  3) 全量校对：
       uv run python scripts\proofread_translations_api.py ^
           --current learnplay_cache4\localization\maingame.csv ^
           --translations data\translations_remaining.json ^
           --skip data\translations_legacy.json ^
           --out data\translations_proofread.json ^
           --changes data\proofread_changes.json ^
           --api-config config\api.json
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from localization import (
    CJK_RE,
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
    "1. 输出必须是 JSON 对象，形如 {\"translations\":[{\"id\":\"...\",\"text\":\"...\"}, ...]}，"
    "数量与输入完全一致，id 一一对应，不得合并、遗漏或新增。\n"
    "2. 保留 {C} {B} {L} {X} {Y} {A} {0} {1} 与 [1] [2] 等占位符原样。\n"
    "3. 保留 Rocksmith、Ubisoft、Uplay、Steam、PSN、Xbox LIVE、PlayStation、Real Tone Cable 等品牌名，"
    "音名/和弦记号/歌曲名/艺人名不翻译。\n"
    "4. 术语统一：tuning=调弦，fret=品，capo=变调夹，arrangement=编曲，Lead=主音，Rhythm=节奏，Bass=贝斯，tone=音色，calibration=校准。\n"
    "5. 不要使用半角逗号 ,（用中文逗号，），不要包含换行。\n"
    "6. 只输出 JSON，不要任何解释。"
)


def chat_once(cfg: dict, items: list[dict], timeout: int) -> list[dict]:
    """调用 OpenAI 兼容 chat/completions，返回 [{id, text}]。"""
    url = cfg["base_url"].rstrip("/") + "/chat/completions"
    payload = {
        "model": cfg.get("model", "deepseek-v4-flash"),
        "messages": [
            {"role": "system", "content": PROOFREAD_SYSTEM},
            {"role": "user", "content": json.dumps(items, ensure_ascii=False)},
        ],
        "stream": False,
        "response_format": {"type": "json_object"},
        "max_tokens": 8192,
    }
    temp = cfg.get("temperature")
    if temp is not None:
        payload["temperature"] = temp
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + cfg.get("api_key", "").strip(),
    }
    req = urllib.request.Request(url, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                                 headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        result = json.load(resp)
    content = result["choices"][0]["message"]["content"]
    # 去掉可能的 ```json ... ``` 围栏
    content = re.sub(r"^```(?:json)?\s*", "", content.strip())
    content = re.sub(r"\s*```$", "", content)
    data = json.loads(content)
    return data["translations"]


def proofread_batch(cfg: dict, batch: list[dict], timeout: int) -> dict[str, str]:
    items = [
        {"id": it["id"], "source": it["source"], "translation": it["translation"]}
        for it in batch
    ]
    out = chat_once(cfg, items, timeout)
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
    return by_id


def validate(translated: str) -> tuple[bool, str]:
    if not translated.strip():
        return False, "empty"
    if "\n" in translated or "\r" in translated:
        return False, "embedded newline"
    return True, ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", required=True, help="当前(learnplay) maingame.csv")
    ap.add_argument("--translations", required=True, help="待校对翻译 json")
    ap.add_argument("--skip", action="append", default=[], help="跳过 json (如汉化组 translations_legacy.json)")
    ap.add_argument("--out", required=True, help="校对结果 json")
    ap.add_argument("--changes", default=None, help="改动明细 json")
    ap.add_argument("--api-config", required=True, help="config/api.json (DeepSeek)")
    ap.add_argument("--batch-size", type=int, default=40)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0, help="只校对随机抽样 N 条(0=全量)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = json.loads(Path(args.api_config).read_text(encoding="utf-8"))

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
    if args.limit and args.limit < len(todo):
        todo = random.Random(args.seed).sample(todo, args.limit)
    print(f"待校对条目: {len(todo)} (跳过汉化组: {len(skip & set(translations))}) | "
          f"model={cfg.get('model')} base={cfg.get('base_url')}", flush=True)
    if args.dry_run:
        return
    if not cfg.get("api_key"):
        print("api_key 为空，请先在 config/api.json 里填入你的 DeepSeek API Key", file=sys.stderr)
        raise SystemExit(1)

    out_path = Path(args.out)
    done = load_json(out_path)
    changes: dict[str, dict] = {}
    if args.changes and Path(args.changes).exists():
        changes = json.loads(Path(args.changes).read_text(encoding="utf-8"))
    timeout = int(cfg.get("timeout", 300))

    todo = [it for it in todo if it["id"] not in done]
    batches = [todo[i:i + args.batch_size] for i in range(0, len(todo), args.batch_size)]
    print(f"剩余未校对批次: {len(batches)} (并发 {args.concurrency})", flush=True)

    lock = threading.Lock()
    stats = {"n": 0}

    def process(batch: list[dict]) -> None:
        last_error = ""
        received = None
        for attempt in range(1, 4):
            try:
                received = proofread_batch(cfg, batch, timeout)
                break
            except Exception as exc:
                last_error = str(exc)
                print(f"batch 失败(attempt {attempt}): {last_error}", flush=True)
                time.sleep(attempt * 4)
        if received is None:
            raise RuntimeError(f"校对失败: {last_error}")
        with lock:
            by_id_batch = {it["id"]: it for it in batch}
            for sid, text in received.items():
                text = text.replace(",", "，").strip()
                before = by_id_batch[sid]["translation"]
                if text != before:
                    changes[sid] = {
                        "source": by_id_batch[sid]["source"],
                        "before": before,
                        "after": text,
                    }
                done[sid] = text
            write_json(out_path, done)
            if args.changes:
                write_json(Path(args.changes), changes)
            stats["n"] += len(received)
            print(f"+{len(received)} -> total {len(done)} | 累计改动 {len(changes)}", flush=True)

    with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as ex:
        futs = [ex.submit(process, b) for b in batches]
        for f in as_completed(futs):
            f.result()

    print(f"校对完成: {len(done)} 条, 有改动 {len(changes)} 条 -> {args.out}", flush=True)


if __name__ == "__main__":
    main()
