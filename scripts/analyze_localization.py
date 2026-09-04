import json
import re
import sys
from pathlib import Path


CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def load(path: Path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    rows = text.splitlines()
    by_id = {}
    duplicates = []
    malformed = []
    for line in rows:
        if not line:
            continue
        parts = line.split(",", 2)
        if len(parts) < 2 or not parts[0].isdigit():
            malformed.append(line[:120])
            continue
        string_id, english_slot = parts[0], parts[1]
        if string_id in by_id:
            duplicates.append(string_id)
        by_id[string_id] = (english_slot, line)
    return rows, by_id, duplicates, malformed


def main():
    old_path = Path(sys.argv[1])
    new_path = Path(sys.argv[2])
    old_rows, old_by_id, old_duplicates, old_malformed = load(old_path)
    new_rows, new_by_id, new_duplicates, new_malformed = load(new_path)

    common_ids = old_by_id.keys() & new_by_id.keys()
    old_only = sorted(old_by_id.keys() - new_by_id.keys(), key=int)
    new_only = sorted(new_by_id.keys() - old_by_id.keys(), key=int)
    new_only_nonempty = [string_id for string_id in new_only if new_by_id[string_id][0]]
    new_only_unique_texts = {new_by_id[string_id][0] for string_id in new_only_nonempty}
    translated_common = []
    unchanged_common = []
    for string_id in common_ids:
        old_english_slot = old_by_id[string_id][0]
        new_english_slot = new_by_id[string_id][0]
        if old_english_slot != new_english_slot and CJK_RE.search(old_english_slot):
            translated_common.append(string_id)
        else:
            unchanged_common.append(string_id)

    result = {
        "legacy": {
            "rows": len(old_rows),
            "unique_ids": len(old_by_id),
            "duplicate_ids": old_duplicates[:20],
            "malformed_lines": len(old_malformed),
            "replacement_characters": sum(row.count("\ufffd") for row in old_rows),
        },
        "learn_play": {
            "rows": len(new_rows),
            "unique_ids": len(new_by_id),
            "duplicate_ids": new_duplicates[:20],
            "malformed_lines": len(new_malformed),
            "replacement_characters": sum(row.count("\ufffd") for row in new_rows),
        },
        "comparison": {
            "common_ids": len(common_ids),
            "legacy_only_ids": len(old_only),
            "learn_play_only_ids": len(new_only),
            "learn_play_only_nonempty_ids": len(new_only_nonempty),
            "learn_play_only_unique_english_texts": len(new_only_unique_texts),
            "translated_common_ids": len(translated_common),
            "unchanged_common_ids": len(unchanged_common),
            "learn_play_only_range": [new_only[0], new_only[-1]] if new_only else None,
            "learn_play_only_samples": [
                {
                    "id": string_id,
                    "english": new_by_id[string_id][0],
                }
                for string_id in new_only[:20]
            ],
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
