"""把老版(汉化组) maingame.csv 中已汉化的 id -> 中文 提取成 JSON。

这些条目来自人工汉化组, 之后“校对”阶段会跳过它们。
用法:
  python scripts/extract_legacy_translations.py ^
      legacy_cache4/localization/maingame.csv data/translations_legacy.json
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from localization import load_legacy_translations, write_json


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("legacy_csv", type=Path)
    ap.add_argument("out_json", type=Path)
    args = ap.parse_args()

    data = load_legacy_translations(args.legacy_csv)
    write_json(args.out_json, dict(sorted(data.items(), key=lambda kv: int(kv[0]))))
    print(f"legacy(汉化组) 翻译条目: {len(data)} -> {args.out_json}")


if __name__ == "__main__":
    main()
