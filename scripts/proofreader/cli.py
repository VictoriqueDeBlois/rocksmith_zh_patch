"""Run with python -m scripts.proofreader.cli."""
import argparse
import json
import random
import re
from collections import Counter
from pathlib import Path

from scripts.localization import load_json, load_slots, write_json
from .prompts import ROOT, build_prompts
from .router import CATEGORIES, route
from .runner import run, validate

def select(items, limit, seed, per_category=0):
    rng = random.Random(seed)
    shuffled = sorted(items, key=lambda item: item["id"])
    rng.shuffle(shuffled)
    chosen = []
    for category in CATEGORIES:
        group = [item for item in shuffled if item["category"] == category]
        if len(group) < per_category:
            raise ValueError(f"{category}: only {len(group)} entries; need {per_category}")
        chosen.extend(group[:per_category])
    if limit is not None and limit < len(chosen):
        raise ValueError("--limit smaller than per-category quota")
    used = {item["id"] for item in chosen}
    chosen.extend(item for item in shuffled if item["id"] not in used)
    return chosen[:limit] if limit is not None else chosen

def main():
    parser = argparse.ArgumentParser(__doc__)
    for flag, default in (("current", "learnplay_cache4/localization/maingame.csv"),
                          ("translations", "data/translations_remaining.json"),
                          ("config", "config/workers.json"), ("legacy", "data/translations_legacy.json"),
                          ("out", "data/proofread_routed.json"), ("changes", "data/proofread_routed_changes.json")):
        parser.add_argument("--" + flag, type=Path, default=ROOT / default)
    parser.add_argument("--skip", action="append", type=Path, default=[])
    parser.add_argument("--include-legacy", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--per-category", type=int, default=0, help="stratified minimum per bucket, e.g. 20")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if (args.limit is not None and args.limit < 1) or args.per_category < 0:
        parser.error("sample sizes must be positive")
    skips = [ROOT / "data/proofread_manual.json", ROOT / "config/overrides.json", *args.skip]
    for path in [args.current, args.translations, args.config, args.legacy, *skips]:
        if not path.is_file():
            parser.error(f"missing input: {path}")
    protected = {p.resolve() for p in [args.current, args.translations, args.config, args.legacy, *skips]}
    if args.out.resolve() in protected or args.changes.resolve() in protected or args.out.resolve() == args.changes.resolve():
        parser.error("outputs must be distinct and must not overwrite inputs")
    source, translations = load_slots(args.current), load_json(args.translations)
    legacy = load_json(args.legacy)
    if args.include_legacy:
        translations = {**legacy, **translations}
    excluded = set()
    for path in skips:
        excluded.update(load_json(path))
    if not args.include_legacy:
        excluded.update(legacy)
    eligible, skipped = [], Counter()
    for sid, translation in translations.items():
        if sid in excluded:
            skipped["locked_or_legacy"] += 1
            continue
        if sid not in source:
            skipped["missing_source"] += 1
            continue
        category = route(source[sid], translation)
        if category == "SKIP":
            skipped["router_skip"] += 1
            continue
        eligible.append(dict(id=sid, source=source[sid], translation=translation, category=category))
    items = select(eligible, args.limit, args.seed, args.per_category)
    prompts = build_prompts()
    workers = load_json(args.config).get("workers", [])
    if not workers or len({w["name"] for w in workers}) != len(workers):
        parser.error("workers must have unique names")
    for worker in workers:
        if not re.fullmatch(r"[\w-]+", worker["name"]) or not worker.get("endpoint") or not worker.get("model"):
            parser.error("invalid worker configuration")
        for field in ("concurrency", "batch_size", "timeout"):
            if int(worker.get(field, 1)) < 1:
                parser.error(f"invalid {field}")
    report = {"selected": len(items), "seed": args.seed, "per_category": args.per_category,
              "eligible_categories": dict(Counter(i["category"] for i in eligible)),
              "sample_categories": dict(Counter(i["category"] for i in items)), "excluded": dict(skipped)}
    write_json(Path(str(args.out) + ".sample.json"), {i["id"]: i for i in items})
    if args.dry_run:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return
    done, errors = run(items, workers, prompts, args.out)
    # Full input map preserves excluded/unselected rows byte-for-byte as values.
    final = dict(translations)
    changes = {}
    for sid, item in done.items():
        final[sid] = item["revised"]
        if item["revised"] != item["translation"]:
            changes[sid] = {"source": item["source"], "original": item["translation"],
                "revised": item["revised"], "category": item["category"], "reason": item["reason"]}
    report.update(completed=len(done), failed=len(errors), changed=len(changes),
        change_rate=len(changes) / len(done) if done else None,
        skipped=sum(bool(i["rejection"]) for i in done.values()),
        rejections={sid: i for sid, i in done.items() if i["rejection"]}, errors=errors,
        final_violations={i["id"]: issue for i in items
            if (issue := validate(i["source"], final[i["id"]], i["translation"], i["category"]))})
    write_json(args.out, final)
    write_json(args.changes, changes)
    write_json(Path(str(args.out) + ".report.json"), report)
    print(json.dumps({k: v for k, v in report.items() if k not in ("rejections", "errors", "final_violations")}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
