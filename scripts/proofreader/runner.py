"""Bounded concurrent requests, strict validation and atomic worker checkpoints."""
from __future__ import annotations

import hashlib
import json
import re
import threading
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from scripts.localization import CJK_RE, load_json, write_json
from .router import TOKENS

SCHEMA = {"type": "object", "properties": {"translations": {"type": "array", "items": {
    "type": "object", "properties": {"id": {"type": "string"}, "text": {"type": "string"},
    "reason": {"type": "string"}}, "required": ["id", "text"]}}}, "required": ["translations"]}

def validate(source, text, original="", category="G", reason=""):
    if not isinstance(text, str) or not text.strip():
        return "empty or non-string translation"
    if TOKENS.findall(source) != TOKENS.findall(text):
        return "placeholder order/count mismatch"
    if any(mark in text for mark in (",", "\n", "\r", "\\n", "\\r")):
        return "comma or newline"
    if text != original:
        if source.strip().lower() in {"combo", "head", "box", "drive", "pad"}:
            return "ambiguous isolated term; context review required"
        if re.search(r"更自然|更流畅|更符合.*习惯|略显生硬|优化表达", reason) and not re.search(r"漏译|误译|错译|丢失|错误|术语|遗漏|条件|逻辑|原意", reason):
            return "style-only rationale"
        if re.sub(r"\s+", "", text) == re.sub(r"\s+", "", original):
            return "whitespace-only polishing"
        if re.search(r"\bcross button\b", source, re.I) and "十字键" in text:
            return "cross button is not D-pad"
        if re.search(r"\bscore attack\b", source, re.I) and "得分挑战" in original and "得分挑战" not in text:
            return "Score Attack terminology regression"
        if CJK_RE.search(original) and not CJK_RE.search(text):
            return "Chinese reverted to English"
        if category == "E" and len(source) <= 60 and CJK_RE.search(original):
            old_words = set(re.findall(r"[A-Za-z]+", TOKENS.sub("", original).lower()))
            new_words = set(re.findall(r"[A-Za-z]+", TOKENS.sub("", text).lower()))
            if new_words - old_words:
                return "possible tone/preset name reverted to English; review manually"
        if re.search(r"\bprofiles?\b", source, re.I) and "配置文件" in text:
            return "profile terminology regression"
        if "玩家档案" in original and "玩家档案" not in text:
            return "profile terminology regression"
        if "她" in text and "她" not in original:
            return "pronoun regression"
    return ""

def chat_once(worker, system, items):
    # Same Ollama protocol as translate_remaining.chat_once; keep the paired
    # source/current translation intact to avoid losing proofreading context.
    payload = {"model": worker["model"], "messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": json.dumps(items, ensure_ascii=False)}],
        "stream": False, "think": False, "format": SCHEMA, "keep_alive": "30m",
        "options": {"temperature": 0, "num_ctx": 16384, "num_predict": 8192}}
    request = urllib.request.Request(worker["endpoint"].rstrip("/") + "/api/chat",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(request, timeout=worker.get("timeout", 900)) as response:
        envelope = json.load(response)
    result = json.loads(envelope["message"]["content"])
    return map_response(items, result)

def map_response(items, result):
    rows = result.get("translations") if isinstance(result, dict) else None
    if not isinstance(rows, list) or len(rows) != len(items):
        raise ValueError("response count mismatch")
    mapped = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or row["id"] in mapped:
            raise ValueError("invalid or duplicate response id")
        if not isinstance(row.get("text"), str) or not isinstance(row.get("reason", ""), str):
            raise ValueError("invalid response text/reason")
        mapped[row["id"]] = row
    if set(mapped) != {item["id"] for item in items}:
        raise ValueError("response ids mismatch")
    return mapped

def fingerprint(items, prompts, workers):
    # Includes implementation so changed validation/routing cannot reuse old results.
    implementation = {p.name: p.read_text(encoding="utf-8") for p in Path(__file__).parent.glob("*.py")}
    data = json.dumps([items, prompts, workers, implementation], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def run(items, workers, prompts, out, request_fn=chat_once):
    signature = fingerprint(items, prompts, workers)
    partitions = [items[index::len(workers)] for index in range(len(workers))]

    def worker_run(worker, assigned):
        part = Path(str(out) + f".part.{worker['name']}.json")
        saved = load_json(part)
        if saved and saved.get("fingerprint") != signature:
            raise ValueError(f"Stale checkpoint {part}; choose a new --out or remove old parts")
        done = saved.get("items", {})
        lock = threading.Lock()
        batches = []
        for category in "ABCDEFG":
            batch, chars = [], 0
            for item in assigned:
                if item["category"] != category or item["id"] in done:
                    continue
                size = len(item["source"]) + len(item["translation"])
                if batch and (len(batch) >= worker.get("batch_size", 24) or chars + size > 10000):
                    batches.append((category, batch))
                    batch, chars = [], 0
                batch.append(item)
                chars += size
            if batch:
                batches.append((category, batch))

        errors = {}
        def process(category, batch):
            inputs = [{key: item[key] for key in ("id", "source", "translation")} for item in batch]
            try:
                mapped = request_fn(worker, prompts[category], inputs)
            except Exception as exc:
                if len(batch) > 1:
                    for item in batch:
                        process(category, [item])
                    return
                with lock:
                    errors[batch[0]["id"]] = str(exc)
                return  # Not checkpointed: next invocation retries transport failures.
            records = {}
            for item in batch:
                row = mapped[item["id"]]
                rejection = validate(item["source"], row["text"], item["translation"], category, row.get("reason", ""))
                records[item["id"]] = dict(item, revised=item["translation"] if rejection else row["text"],
                    candidate=row["text"], reason=row.get("reason", "模型未提供理由，需复核"), rejection=rejection)
            with lock:
                done.update(records)
                write_json(part, {"fingerprint": signature, "items": done})
                print(f"[{worker['name']}] completed {len(done)}/{len(assigned)}", flush=True)

        with ThreadPoolExecutor(max_workers=worker.get("concurrency", 2)) as pool:
            futures = [pool.submit(process, category, batch) for category, batch in batches]
            for future in as_completed(futures):
                future.result()
        return done, errors

    all_done, all_errors = {}, {}
    with ThreadPoolExecutor(max_workers=len(workers)) as pool:
        futures = [pool.submit(worker_run, worker, group) for worker, group in zip(workers, partitions)]
        for future in as_completed(futures):
            done, errors = future.result()
            all_done.update(done)
            all_errors.update(errors)
    return all_done, all_errors
