"""按审阅规则对全量译文做确定性扫描，输出候选清单(不自动改)。

规则来源: review.md 第 B/C 节。输出 docs/rule_scan_report.md + data/rule_scan_candidates.json
"""
from __future__ import annotations

import json, re
from collections import Counter
from pathlib import Path

from localization import CJK_RE, PLACEHOLDER_RE, load_json, load_slots, write_json

# 误译/翻译腔短语候选 (审阅 C.3 及 B 规则)
BLACKLIST = [
    "被返回", "忍住不用", "幽灵音符", "创建匹配", "贝斯事件", "贝斯词汇量",
    "特殊计量表", "敲击琴品", "琴颈的顶部", "滑音颤音", "合奏鼓组",
    "不需要",  # 见规则2 (但可能误报, 仅提示)
]

def scan(args):
    current = load_slots(Path(args.current))
    rem = load_json(Path(args.remaining))
    out = {
        "english_leftover_sentence": [],
        "blacklist_phrase": [],
        "cjk_ascii_no_space": [],
        "placeholder_followed_by_comma": [],
    }
    for sid in sorted(rem, key=int):
        zh = rem[sid]
        if not zh.strip():
            continue
        # A. 疑似整句漏译(无 CJK 且像英文句子)
        if not CJK_RE.search(zh):
            letters = re.findall(r"[A-Za-z]+", zh)
            if len(letters) >= 4 and sum(len(x) for x in letters) >= 25:
                out["english_leftover_sentence"].append({"id": sid, "zh": zh})
        # B. 误译/翻译腔短语
        for phrase in BLACKLIST:
            if phrase in zh:
                out["blacklist_phrase"].append({"id": sid, "phrase": phrase, "zh": zh})
        # C. 中英/中数之间缺空格 (仅提示; 排除占位符邻接)
        clean = PLACEHOLDER_RE.sub("", zh)
        for m in re.finditer(r"[\u4e00-\u9fff]([A-Za-z0-9])", clean):
            out["cjk_ascii_no_space"].append({"id": sid, "ctx": zh[max(0,m.start()-12):m.end()+12]})
            break
        # D. 占位符后紧跟逗号(可能来自 DS 或 qwen 遗留)
        if re.search(r"\}[，,]", zh):
            out["placeholder_followed_by_comma"].append({"id": sid, "zh": zh})

    # 汇总
    report = {}
    for k, v in out.items():
        report[k] = len(v)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    write_json(Path(args.out_json), out)
    return out

def main() -> None:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--current", required=True)
    ap.add_argument("--remaining", required=True)
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--out-json", required=True)
    args = ap.parse_args()
    out = scan(args)
    p = Path(args.out_md)
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# 全量译文规则扫描报告（不自动修改，仅供审阅/落地）", ""]
    summary = {k: len(v) for k, v in out.items()}
    lines.append("## 统计\n")
    for k, v in summary.items():
        lines.append(f"- {k}: **{v}**")
    lines.append("")
    for k, v in out.items():
        lines.append(f"## {k}（{len(v)}）")
        for item in v[:40]:
            if k == "blacklist_phrase":
                lines.append(f"- [{item['id']}] `{item['phrase']}` :: {item['zh'][:100]}")
            elif k == "cjk_ascii_no_space":
                lines.append(f"- [{item['id']}] …{item['ctx']}…")
            else:
                lines.append(f"- [{item['id']}] {item['zh'][:120]}")
        lines.append("")
    p.write_text("\n".join(lines), encoding="utf-8")
    print("report:", p)

if __name__ == "__main__":
    main()
