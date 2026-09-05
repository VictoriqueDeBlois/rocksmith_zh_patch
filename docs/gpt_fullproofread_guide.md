# 给 GPT 的 Rocksmith 2014 全文校对引导上下文

> 用途：让 GPT（新会话）依据既定规则对 Rocksmith 2014 中文化的全文译文做校对，
> 输出“修订提案”（JSON），供本项目导入、人工/其它模型复核后落地。
> **GPT 只读仓库文件并产出提案文件，不要直接修改任何现有翻译数据。**

## 1. 项目背景

- 游戏：Rocksmith 2014（Steam Remastered 版）。
- 汉化方式：游戏文本在 `cache.psarc` → `cache4.7z` → `localization\maingame.csv`。
  CSV 每行格式：`id,<中文写入 English 列>,其余语言列……`；我们**把简体中文写入第 2 列（下标 1）**，
  其余列保持原样，游戏以英文语言运行时即显示中文。
- 现译文来源分层（重要，优先级由高到低）：
  1. `config\overrides.json`（64 条人工 UI 术语，**不要推翻**）
  2. `data\proofread_manual.json`（人工锁定 256 条：15 条审校 + 102 条 profile 统一 + 140 条审阅落地，**不要推翻**）
  3. 汉化组（老版 v3 人工简体）`data\translations_legacy.json`（4022 条；是否纳入本次校对由用户决定）
  4. AI 全量新译 `data\translations_remaining.json`（16067 条，qwen3.8 生成，简体）

## 2. 校对范围（默认，避免重复劳动）

- **默认审校对象 = `data\translations_remaining.json` 中“尚未被人工锁定”的条目**
  （即从 16067 条里去掉 `data\proofread_manual.json` 已含的 id）。
- 已锁定的 256 条、`config\overrides.json` 64 条 **默认不审**（除非你发现与下列铁律冲突的硬伤，再单列）。
- 汉化组 `translations_legacy.json`：用户此前要求“汉化组部分不参与 AI 校对”；但发现过少量 id 漂移。
  是否审它请由用户明确：默认不审，可选审（我会把开关写清楚）。

## 3. 必须读取/可参考的文件

| 作用 | 路径 |
|---|---|
| 全部 AI 现译（主对象） | `./data\translations_remaining.json` |
| 人工锁定（跳过） | `...\data\proofread_manual.json` |
| 人工 UI 术语（跳过） | `...\config\overrides.json` |
| 汉化组（默认跳过） | `...\data\translations_legacy.json` |
| 英文原文（按 id 查） | `...\learnplay_cache4\localization\maingame.csv`（第 1 列 id、第 2 列英文原文） |
| 审阅规则全文（重要） | `...\docs/review_500_verdicts.md`（A 逐条 + B 20 条规则 + C 程序化建议） |
| 规则扫描候选 | `...\docs\rule_scan_report.md`、`...\data\rule_scan_candidates.json` |
| 待核实上下文队列 | `...\data\review_context_queue.json` |
| 500 条抽样审阅做法参考 | `...\docs\proofread_sample500_docs/review_500_verdicts.md`、`...\docs\review_guide_prompt.md` |

JSON 结构：`translations_remaining.json` 是 `{ "id": "中文" }`，英文原文要从 maingame.csv 按 id 取第 2 列。

## 4. 技术铁律（违反任何一条都算错误提案）

1. 占位符是游戏按键/图标：`{C} {B} {L} {X} {Y} {A} {0} {1} [1] [2]`。
   **必须原样保留、数量与出现顺序不变**；不得用标点/空格替换或删除；不要把 `{C}` 改写成“，”。
2. 输出译文：**简体中文**；不要半角逗号 `,`（用中文逗号 `，`）；不要含 `\n`/`\r`。
3. 品牌/专有名词保留英文：Rocksmith、Ubisoft、Uplay、Steam、PSN、Xbox LIVE、PlayStation、
   Real Tone Cable、歌曲/艺人名、吉他型号（Epiphone®…、Gibson®…）等。
4. 音色/预设/风格名**已翻译成中文的不要改回英文**（如 Harmonic Minor Electronic → 和声小调电子）。
5. 面向玩家统一用“你”；歌曲/物品用“它/它们”，不要用“她”指代歌曲/物品。

## 5. 已落地术语表（不要当新问题再报，也不要改回）

- profile → **玩家档案**（全局已统一，102 条已锁定）
- cab / box → **箱体**；amp → **音箱**；head → **音箱头**；combo → **一体式音箱**；
  speaker driver → **扬声器单元**；open-back → **背部开放式**
- inline → **联排**（6 联排/4 联排）
- fret-hand mute → **左手制音**；palm mute → **手掌制音**
- slide → **滑音**；tremolo（教学拨弦）→ **快速反复拨弦**（效果器/音色语境另论）
- Scale Shape → **音阶指型**；Arpeggio → **琶音**；Technique → **技巧**
- Authentic Tone → **原曲音色**；Complexity → **复杂度**（区别于 Difficulty=难度）；
  Path → **演奏路径**；D-pad → **十字键**；Session Drums → **即兴鼓组**
- 多人：session → **会话**；match → **对局**；matchmaking → **匹配**；
  group leader / host → **队长 / 房主**（不要互串）；event(活动) → **活动**（不是程序“事件”）
- streak → **连击**；能量槽/量表 → **量槽**（不是“计量表”）
- major chord → **大三和弦**；octave(任务) → **八度音程**；Phrygian Dominant → **弗里吉亚属音阶**
- Slap → **拍弦**；Pop → **勾拍**（教学语境）

## 6. 审阅规则（B 节 20 条，GPT 逐条应用到全文）

1. play/hit/pick 先判对象：游玩/播放/弹奏/拨动/拨响 不能互相替代。
2. 教学句保留动作限制/步骤/力度边界：“不要”≠“不需要”，“可以”≠“只需要”，“只需”≠“刚刚”。
3. 方向按语境：推弦 up/down=音高；滤波器 up/down=频率；不要当屏幕上下。
4. 指法用明确名称（食指/中指/无名指/小指）；按压/轻触/点按/拨弦不混。
5. 贝斯：Slap=拍弦、Pop=勾拍；泛音=特定位置轻触琴弦。
6. tremolo 按语境：教学=快速反复拨弦；效果器/音色名不套同一译法。
7. 节拍：正拍/反拍（两拍之间），不要机械译“强拍/弱拍”。
8. 区分调性/和弦/音程：大三和弦、八度音程、Phrygian Dominant ≠ 属调。
9. Scale Shape=音阶指型、Arpeggio=琶音、Technique=技巧；正文可解释“各音分开弹”。
10. 界面显示描述 ≠ 演奏技法：ghosted notes=淡化显示的音符；without notes=不显示音符提示；In Tune=已调准状态。
11. 设备结构专词：head=音箱头、combo=一体式音箱、speaker driver=扬声器单元、Square=方波、pad=铺底音色。
12. 效果器名按功能译：fuzz=法兹、overdrive 语境 drive=过载、voiced for=针对…调校。
13. 多人概念按作用域：会话/对局/匹配/队长/房主/活动。
14. 同一控件/功能在标题、任务、说明用同一译名。
15. 任务条件逐项保留：超过、至少、连续、一局内、同时、仅在、不得、即将攻击前。
16. streak=连击；量槽按游戏功能表达。
17. 检查先行词与中文省略：不擅自补“部分”；允许省略玩家主语；who/what/it/this 要明确指向。
18. 识别整句漏译与强调语：EXPIRES、THE、普通任务标题、风格通名要译；品牌型号保留。
19. 教学口语自然化：dive into=开始练习、put it all together in a song=在歌曲中综合运用、bring you in=提示进入演奏。
20. 排版：中英/中数之间统一间隔；中文省略号用“……”；清除多余空格；占位符邻接标点按实际显示确认（不要盲目删）。

## 7. C 节建议的检查项（GPT 校对时逐项过）

- 漏译：长英文原样保留、中文句中残留普通英文（豁免品牌/型号/和弦符号/动态名称）。
- 条件核对：源文有 only / without / before / at least / beat / in a row / in a single game /
  at the same time 时，确认译文体现了该条件。
- 数值/量词/比较核对：数字顺序、量词、“超过 15,000,000”等。
- 误译短语线索（扫描已圈出）：被返回、忍住不用…的冲动、幽灵音符、创建匹配、贝斯事件、
  贝斯词汇量、特殊计量表、敲击琴品、琴颈的顶部、滑音颤音、合奏鼓组 等。
- 名称一致性：同一英文概念跨条目译名不同时，汇总并统一。
- 排版/占位符邻接标点：谨慎，见规则 20。

## 8. 输出要求（GPT 交付物）

请产出一个 JSON 文件（建议路径 `./data\gpt_review_proposals.json`），结构：

```json
{
  "meta": {
    "scope": "translations_remaining 未锁定条目",
    "reviewed_ids": 15811,
    "changed": 1234,
    "rules_applied": true
  },
  "proposals": [
    {
      "id": "12345",
      "source": "英文原文",
      "original": "现译",
      "revised": "你的最终修订译文",
      "reason": "错译/漏译/术语/语病…",
      "rule_ref": "B-3 / C-条件 / 术语",
      "confidence": "high|medium|low"
    }
  ],
  "uncertain_ids": [ ... ]
}
```

附加要求：
- 只列出**需要改**的条目；认为“现译正确”的不列出（隐含不改）。
- 已锁定 id（`data\proofread_manual.json`、`config\overrides.json`）除非硬伤，否则不列。
- revised 必须满足第 4 节技术铁律；无法确定词义的条目放进 `uncertain_ids`，不要臆造。
- 若改了 500+ 条，请另外在 reason 里给出可归纳的“通用规则/程序化修复”，便于一次性批量落地。

## 9. 给用户的附加信息（便于 GPT 上下文判断）

- 这批现译由 qwen3.8（27B 级）生成，整体简体、质量较好；常见问题是：
  术语不一致、个别整句漏译/保留英文、教学句动作对象与否定、占位符邻接标点、数字空格。
- 之前用 DeepSeek V4 Flash 做过 500 条抽样，改动率约 10%，且它喜欢“润色式重写”，
  所以**建议 GPT 只改真错，不要为了改写而改写**。
- 全量 16067 中 1512 条是“有意保留英文”（品牌/型号/和弦符号等），不必当漏译。
- 若审汉化组 legacy 4022，注意可能存在的 id 漂移（同一 id 在老版 2014 与 Remastered 之间英文不同），
  需结合英文原文判断，而不是只看中文。
