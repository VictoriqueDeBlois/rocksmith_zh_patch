"""合并所有翻译来源并审计, 产出最终 translations_final.json。

优先级(高 -> 低): 人工 overrides > 汉化组 legacy > AI(按 --ai 传入顺序, 前者优先,
例如先传校对后的 proofread, 再传新翻译/旧翻译)。
用法:
  python scripts/merge_and_audit_translations.py ^
      --current learnplay_cache4/localization/maingame.csv ^
      --legacy-json data/translations_legacy.json ^
      --ai data/translations_proofread.json data/translations_remaining.json data/translations_merged.json ^
      --overrides config/overrides.json ^
      --out data/translations_final.json ^
      --report data/audit_final.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from localization import (
    CJK_RE,
    PLACEHOLDER_RE,
    is_translatable,
    load_json,
    load_slots,
    write_json,
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", required=True, type=Path)
    ap.add_argument("--legacy-json", type=Path, default=None)
    ap.add_argument("--ai", action="append", default=[], type=Path)
    ap.add_argument("--overrides", type=Path, default=None)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--report", type=Path, default=None)
    args = ap.parse_args()

    current = load_slots(args.current)
    legacy = load_json(args.legacy_json) if args.legacy_json else {}
    overrides = load_json(args.overrides) if args.overrides else {}
    ai_sources = [load_json(p) for p in args.ai]

    final: dict[str, str] = {}
    unknown_overrides = sorted(set(overrides) - set(current), key=int)
    for sid in sorted(current, key=int):
        text = current[sid]
        translated = None
        if sid in overrides:
            translated = overrides[sid]
        elif sid in legacy:
            translated = legacy[sid]
        else:
            for src in ai_sources:
                if sid in src:
                    translated = src[sid]
                    break
        if translated is not None and translated != text:
            final[sid] = translated

    # ----- 审计 -----
    covered_keys = set(legacy) | set(overrides)
    for ai in ai_sources:
        covered_keys |= set(ai)
    missing = []          # 完全没有译文来源覆盖且仍为英文
    kept_english = []     # 有来源覆盖，但译文有意保留英文(品牌/专名等)
    placeholder_errors = []
    empty = []
    no_cjk = []
    embedded = []
    for sid in sorted(current, key=int):
        source = current[sid]
        if sid not in final and sid in covered_keys:
            kept_english.append(sid)
            continue
        if is_translatable(source) and sid not in final:
            missing.append(sid)
            continue
        translated = final.get(sid, "")
        if not translated.strip():
            continue
        if sorted(PLACEHOLDER_RE.findall(source)) != sorted(PLACEHOLDER_RE.findall(translated)):
            placeholder_errors.append(sid)
        if not CJK_RE.search(translated) and is_translatable(source):
            no_cjk.append((sid, translated))
        if "," in translated or "\n" in translated or "\r" in translated:
            embedded.append(sid)

    report = {
        "current_ids": len(current),
        "final_ids": len(final),
        "legacy_ids": len(legacy),
        "override_ids": len(overrides),
        "unknown_override_ids": unknown_overrides,
        "ai_ids_used": {str(p): len(load_json(p)) for p in args.ai},
        "missing": missing,
        "missing_count": len(missing),
        "kept_english_count": len(kept_english),
        "kept_english": kept_english,
        "placeholder_errors": placeholder_errors,
        "empty": empty,
        "no_cjk_count": len(no_cjk),
        "no_cjk_samples": no_cjk[:20],
        "embedded_delimiters": embedded,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.report:
        write_json(args.report, report)

    problems = bool(missing or unknown_overrides or placeholder_errors or empty or embedded)
    if problems:
        raise SystemExit(1)
    write_json(args.out, final)
    print(f"合并完成: {len(final)} 条 -> {args.out}")


if __name__ == "__main__":
    main()
