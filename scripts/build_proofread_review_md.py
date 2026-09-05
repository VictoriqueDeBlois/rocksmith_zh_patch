"""把 DeepSeek 抽检结果生成“给新会话模型审阅”的 Markdown 清单。

用法:
  uv run python scripts/build_proofread_review_md.py ^
      --current learnplay_cache4/localization/maingame.csv ^
      --translations data/translations_remaining.json ^
      --proofread data/proofread_sample500.json ^
      --changes data/proofread_sample500_changes.json ^
      --skip data/translations_legacy.json ^
      --skip data/proofread_manual.json ^
      --limit 500 --seed 20260905 ^
      --out docs/proofread_sample500_review.md
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from localization import load_json, load_slots


def esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", required=True)
    ap.add_argument("--translations", required=True)
    ap.add_argument("--proofread", required=True, help="DS 抽检输出 json")
    ap.add_argument("--changes", default=None, help="DS 改动明细 json")
    ap.add_argument("--skip", action="append", default=[])
    ap.add_argument("--limit", type=int, default=500)
    ap.add_argument("--seed", type=int, default=20260905)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    current = load_slots(Path(args.current))
    translations = load_json(Path(args.translations))
    proofread = load_json(Path(args.proofread))
    changes = load_json(Path(args.changes)) if args.changes else {}
    skip = set()
    for p in args.skip:
        skip.update(load_json(Path(p)).keys())

    todo = [sid for sid in sorted(translations, key=int)
            if sid not in skip and current.get(sid) is not None]
    sample = set(random.Random(args.seed).sample(todo, min(args.limit, len(todo))))

    # 按 (英文, 现译) 聚合重复 id
    rows: dict[tuple[str, str], dict] = {}
    for sid in sorted(sample, key=int):
        src = current[sid]
        zh = translations[sid]
        ds = proofread.get(sid, "")
        key = (src, zh)
        if key not in rows:
            rows[key] = {"ids": [], "src": src, "zh": zh, "ds": ds}
        rows[key]["ids"].append(sid)

    changed = 0
    unchanged = 0
    missing_ds = 0
    lines = []
    for (src, zh), r in sorted(rows.items(), key=lambda kv: int(kv[1]["ids"][0])):
        ds = r["ds"]
        if not ds:
            missing_ds += 1
            status = "缺 DS 结果"
        elif ds == zh:
            unchanged += 1
            status = "未改动"
        else:
            changed += 1
            status = "改动"
        ids = ", ".join(r["ids"])
        lines.append(
            f"| {esc(ids)} | {esc(src)} | {esc(zh)} | {esc(ds)} | {status} |"
        )

    changed_ids = set(changes)
    n_rows = len(rows)
    out_p = Path(args.out)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    md = f"""# Rocksmith 2014 译文 DS Flash 抽检审阅清单（{n_rows} 组文本 / 样本 {len(sample)} 条 id）

> 本文档是给「另一个模型开新会话」阅读的审阅材料。请**不要修改仓库任何文件**，
> 只需阅读本清单并输出：①每条/每类要不要采纳 DS 改动；②归纳出的通用规则清单。

## 1. 背景（供审阅模型了解上下文）

- 项目：Rocksmith 2014 (Remastered) 中文化。把中文写入 `maingame.csv` 的 English 列，游戏英文语言下显示中文。
- 「现译」= 服务器 **qwen3.8** 生成的简体译文（`data/translations_remaining.json`，共 16067 条，已排除汉化组 4022 条）。
- 「DS」= **DeepSeek V4 Flash** 对本条提出的校对建议。
- 本清单样本：随机 {len(sample)} 条 id（seed={args.seed}），**已排除** 汉化组 4022 条 + 人工锁定 `data/proofread_manual.json`（116 条）。
- 已落地、**不要再当新问题报**的全局规则：
  1. 占位符 `{{C}} {{B}} {{L}} {{X}} {{A}} {{0}} {{1}} [1]` 是按键/图标，**必须保留**；DS 若删改占位符即为错误建议。
  2. `profile` 统一译「玩家档案」（已全局替换 102 条）。
  3. 音色/预设/风格名（Harmonic Minor Electronic 等）保持中文译名，不要改回英文。
  4. 术语：cab/box=箱体、amp=音箱、inline=联排、fret-hand mute=左手制音、slide=滑音。
  5. 代词：玩家用「你」；歌曲/物品用「它」，不用「她」。

## 2. 统计

- 唯一文本组数：{n_rows}
- 「改动」（DS 建议 ≠ 现译）：**{changed}**
- 「未改动」：{unchanged}
- DS 结果缺失：{missing_ds}
- 其中已在 `data/proofread_sample500_changes.json` 记录的改动 id 数：{len(changed_ids)}

## 3. 清单

| ID | 英文原文 | 现译（qwen3.8） | DS 建议 | 状态 |
|---|---|---|---|---|
{chr(10).join(lines)}

## 4. 请输出（建议格式）

```
## 审阅结论
### A. 逐条判定（可选，可只列需要改的）
- ids: [...], 采纳: 现译/DS/重译, 最终文本: "...", 理由: "..."
### B. 归纳规则（重点）
- 规则1: ...
  - 证据: ids [...]
### C. 建议落到程序里的修复（如全局替换、术语表、prompt 修改）
```

## 5. 附加材料
- `data/proofread_sample500.json`：500 条 id 的 DS 最终文本（含未改动）
- `data/proofread_sample500_changes.json`：仅改动明细（id -> {{source,before,after}}）
- `data/translations_remaining.json`：全部现译
- `data/proofread_manual.json`：已人工锁定的最终译文（合并时优先级最高）
"""
    out_p.write_text(md, encoding="utf-8")
    print(f"已生成 {out_p}: 唯一文本组 {n_rows} | 改动 {changed} | 未改动 {unchanged} | 缺DS {missing_ds}")


if __name__ == "__main__":
    main()
