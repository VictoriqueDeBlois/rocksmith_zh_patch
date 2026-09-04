"""把人工复核过的 UI 术语覆盖(config/overrides.json)合并进某个翻译 json。

用法:
  python scripts/apply_translation_overrides.py data/translations_merged.json
  默认读取 scripts 同级的 ../config/overrides.json; 可用 --overrides 覆盖。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import localization as L


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", type=Path, help="要写入覆盖的翻译 json")
    ap.add_argument("--overrides", type=Path, default=None)
    args = ap.parse_args()

    ov_path = args.overrides or (Path(__file__).resolve().parent.parent / "config" / "overrides.json")
    overrides = json.loads(ov_path.read_text(encoding="utf-8"))
    data = json.loads(args.target.read_text(encoding="utf-8"))
    unknown = sorted(set(overrides) - set(data), key=int)
    if unknown:
        raise SystemExit(f"覆盖项 id 不在目标 json 中: {unknown}")
    data.update(overrides)
    L.write_json(args.target, data)
    print(f"已应用 {len(overrides)} 条人工复核覆盖 -> {args.target}")


if __name__ == "__main__":
    main()
