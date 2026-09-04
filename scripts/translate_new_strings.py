import json
import re
import sys
import time
import urllib.request
from collections import defaultdict
from pathlib import Path


PLACEHOLDER_RE = re.compile(r"\{[A-Za-z]+\}|\[[0-9]+\]")


def load_slots(path: Path):
    slots = {}
    for line in path.read_text(encoding="utf-8-sig", errors="strict").splitlines():
        parts = line.split(",", 2)
        if len(parts) >= 2 and parts[0].isdigit():
            slots[parts[0]] = parts[1]
    return slots


def split_for_translation(batch):
    request_items = []
    plans = {}
    for item in batch:
        pieces = re.split(f"({PLACEHOLDER_RE.pattern})", item["text"])
        plan = []
        segment_number = 0
        for piece in pieces:
            if not piece:
                continue
            if PLACEHOLDER_RE.fullmatch(piece):
                plan.append(("literal", piece))
            else:
                segment_id = f'{item["id"]}S{segment_number}'
                request_items.append({"id": segment_id, "text": piece})
                plan.append(("segment", segment_id))
                segment_number += 1
        plans[item["id"]] = plan
    return request_items, plans


def call_ollama(endpoint: str, model: str, batch):
    request_items, plans = split_for_translation(batch)
    schema = {
        "type": "object",
        "properties": {
            "translations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "text": {"type": "string"},
                    },
                    "required": ["id", "text"],
                },
            }
        },
        "required": ["translations"],
    }
    system = (
        "你是 Rocksmith 2014 游戏本地化译者。把英文 UI 文本翻译为自然、简洁的简体中文。"
        "每个 id 对应一个独立文本片段；不得合并、遗漏或添加项目。"
        "保留 Rocksmith、Ubisoft、Steam、PSN、Xbox LIVE 等品牌名。"
        "术语统一：tuning=调弦，fret=品，capo=变调夹，arrangement=编曲，"
        "Lead=主音，Rhythm=节奏，Bass=贝斯，tone=音色，calibration=校准。"
        "只返回符合指定结构的 JSON，不要解释。"
    )
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
        "options": {
            "temperature": 0,
            "num_ctx": 8192,
            "num_predict": 4096,
        },
    }
    request = urllib.request.Request(
        endpoint.rstrip("/") + "/api/chat",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=600) as response:
        result = json.load(response)
    items = json.loads(result["message"]["content"])["translations"]
    expected_ids = [item["id"] for item in request_items]
    if len(items) != len(expected_ids):
        raise ValueError(
            f"Segment count mismatch: expected {len(expected_ids)}, got {len(items)}"
        )
    segment_text = {}
    returned_ids = [item.get("id") for item in items]
    if returned_ids == expected_ids:
        segment_text = {item["id"]: item["text"] for item in items}
    else:
        segment_text = {
            expected_id: item["text"] for expected_id, item in zip(expected_ids, items)
        }

    restored = []
    for item in batch:
        translated = "".join(
            value if kind == "literal" else segment_text[value]
            for kind, value in plans[item["id"]]
        )
        restored.append({"id": item["id"], "text": translated})
    return restored


def validate(source: str, translated: str):
    if sorted(PLACEHOLDER_RE.findall(source)) != sorted(PLACEHOLDER_RE.findall(translated)):
        return False, "placeholder mismatch"
    if not translated.strip():
        return False, "empty translation"
    if "\n" in translated or "\r" in translated:
        return False, "embedded newline"
    return True, ""


def main():
    old_path = Path(sys.argv[1])
    new_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    model = sys.argv[4] if len(sys.argv) > 4 else "qwen3.5:9b"
    batch_size = int(sys.argv[5]) if len(sys.argv) > 5 else 24
    endpoint = sys.argv[6] if len(sys.argv) > 6 else "http://127.0.0.1:11434"
    shard_index = int(sys.argv[7]) if len(sys.argv) > 7 else 0
    shard_count = int(sys.argv[8]) if len(sys.argv) > 8 else 1
    if shard_count < 1 or not 0 <= shard_index < shard_count:
        raise ValueError("shard_index must be in [0, shard_count)")

    old_slots = load_slots(old_path)
    new_slots = load_slots(new_path)
    new_ids = sorted(set(new_slots) - set(old_slots), key=int)

    text_to_ids = defaultdict(list)
    for string_id in new_ids:
        text_to_ids[new_slots[string_id]].append(string_id)

    translations = {}
    if output_path.exists():
        translations = json.loads(output_path.read_text(encoding="utf-8"))

    assigned_sources = list(text_to_ids)[shard_index::shard_count]
    assigned_ids = {
        string_id
        for source in assigned_sources
        for string_id in text_to_ids[source]
    }

    pending = []
    for source in assigned_sources:
        ids = text_to_ids[source]
        if not all(string_id in translations for string_id in ids):
            pending.append({"id": ids[0], "text": source})

    total = len(pending)
    print(
        f"Shard {shard_index + 1}/{shard_count}: need {total} unique translations "
        f"for {len(assigned_ids)} IDs using {model} at {endpoint}",
        flush=True,
    )

    for offset in range(0, total, batch_size):
        batch = pending[offset : offset + batch_size]
        expected = {item["id"]: item["text"] for item in batch}
        received = None
        last_error = None
        for attempt in range(1, 4):
            try:
                candidate = call_ollama(endpoint, model, batch)
                for item in candidate:
                    item["text"] = re.sub(r"[\r\n]+", " ", item["text"]).strip()
                received = {item["id"]: item["text"] for item in candidate}
                if set(received) != set(expected):
                    if len(candidate) == len(batch):
                        received = {
                            source_item["id"]: translated_item["text"]
                            for source_item, translated_item in zip(batch, candidate)
                        }
                    else:
                        raise ValueError(
                            f"ID mismatch; missing={set(expected)-set(received)}, "
                            f"extra={set(received)-set(expected)}"
                        )
                for string_id, source in expected.items():
                    ok, reason = validate(source, received[string_id])
                    if not ok:
                        raise ValueError(f"{string_id}: {reason}")
                break
            except Exception as exc:
                received = None
                last_error = str(exc)
                print(f"Batch {offset // batch_size + 1} attempt {attempt} failed: {last_error}", flush=True)
                time.sleep(attempt)
        if received is None:
            raise RuntimeError(f"Translation failed after retries: {last_error}")

        for canonical_id, translated in received.items():
            source = expected[canonical_id]
            translated = translated.replace(",", "，")
            for string_id in text_to_ids[source]:
                translations[string_id] = translated

        output_path.write_text(
            json.dumps(translations, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        done = min(offset + batch_size, total)
        saved = len(assigned_ids.intersection(translations))
        print(f"Translated {done}/{total} unique strings; saved {saved}/{len(assigned_ids)} assigned IDs", flush=True)

    missing = sorted(assigned_ids - set(translations), key=int)
    if missing:
        raise RuntimeError(f"Missing translations for {len(missing)} IDs: {missing[:10]}")
    print(
        f"Complete: {len(assigned_ids.intersection(translations))} assigned IDs "
        f"written to {output_path}",
        flush=True,
    )


if __name__ == "__main__":
    main()
