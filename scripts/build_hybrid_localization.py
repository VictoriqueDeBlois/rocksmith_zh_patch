"""把最终翻译写回当前(learnplay) maingame.csv 的“English”列, 生成汉化版 CSV。

用法:
  python scripts/build_hybrid_localization.py ^
      --current learnplay_cache4/localization/maingame.csv ^
      --translations data/translations_final.json ^
      --out work/hybrid_cache4/localization/maingame.csv
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from localization import CJK_RE


def split_line(line: str):
    parts = line.split(",", 2)
    if len(parts) < 3 or not parts[0].isdigit():
        return None
    return parts[0], parts[1], parts[2]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", required=True, type=Path)
    ap.add_argument("--translations", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    translations = json.loads(args.translations.read_text(encoding="utf-8"))
    output_lines = []
    replaced = 0
    malformed = 0
    unknown = 0
    for line in args.current.read_text(encoding="utf-8-sig", errors="strict").splitlines():
        parsed = split_line(line)
        if parsed is None:
            malformed += 1
            output_lines.append(line)
            continue
        string_id, current_text, rest = parsed
        translated = translations.get(string_id)
        if translated is not None and translated != current_text:
            output_lines.append(f"{string_id},{translated},{rest}")
            replaced += 1
        else:
            output_lines.append(line)
            if translated is None and string_id in translations:
                unknown += 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\r\n".join(output_lines) + "\r\n", encoding="utf-8", newline="")
    print(json.dumps({
        "rows": len(output_lines),
        "replaced": replaced,
        "malformed": malformed,
        "translations_total": len(translations),
    }, ensure_ascii=False, indent=2))
    print(f"hybrid CSV -> {args.out}")


if __name__ == "__main__":
    main()
