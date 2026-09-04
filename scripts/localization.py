"""Shared helpers for Rocksmith 2014 localization scripts.

Rocksmith 的 maingame.csv 每行形如:
    id,English,French,Spanish,Italian,German,...,Japanese,...
本汉化方案把简体/繁体中文写入“English(第 2 列, 下标 1)”,
其余列保持不变, 游戏以英文语言运行时即显示中文。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

# CJK 统一表意文字 (含扩展 A)
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
# 游戏内嵌占位符: {C} {B} {L} {X} {0} ... 或 [1]
PLACEHOLDER_RE = re.compile(r"\{[A-Za-z]+\}|\[[0-9]+\]")
TEXT_COL = 1  # "English" 列, 我们写入中文的列


def load_slots(csv_path: Path, col: int = TEXT_COL) -> dict[str, str]:
    """读取 maingame.csv, 返回 {string_id: 第 col 列文本}。"""
    slots: dict[str, str] = {}
    malformed = 0
    for line in csv_path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        parts = line.split(",", 2)
        if len(parts) >= 2 and parts[0].isdigit():
            slots[parts[0]] = parts[col] if col == 1 else line.split(",")[col] if len(line.split(",")) > col else ""
        else:
            malformed += 1
    return slots


def load_legacy_translations(csv_path: Path) -> dict[str, str]:
    """从老版(汉化组) CSV 提取已汉化条目: 第 1 列含 CJK 的 id -> 中文。"""
    translations: dict[str, str] = {}
    malformed = 0
    for line in csv_path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        parts = line.split(",", 2)
        if len(parts) < 2 or not parts[0].isdigit():
            malformed += 1
            continue
        string_id, text = parts[0], parts[1]
        if CJK_RE.search(text):
            translations[string_id] = text
    return translations


def load_json(path: Path | None) -> dict[str, str]:
    if path is None or not Path(path).exists():
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def has_cjk(text: str) -> bool:
    return bool(CJK_RE.search(text))


def is_translatable(text: str) -> bool:
    """是否值得送入翻译: 非空、不含 CJK、至少含一个 ASCII 字母。"""
    if not text or not text.strip():
        return False
    if CJK_RE.search(text):
        return False
    return any(ch.isascii() and ch.isalpha() for ch in text)
