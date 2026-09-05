# 规格说明：分类路由 + 多 Prompt 的 qwen 全文校对脚本（做成 skill 式模块）

> 本文档是给 GPT 的**实现规格**。目标：写一个脚本/模块（类 skill），
> 用**服务器 qwen3.8** 对 Rocksmith 2014 全量译文按“不同情况”用**不同校对 prompt** 分批校对。
> 产出“修订提案 JSON”，经人工/其它模型复核后锁进 `proofread_manual.json`。
> GPT 只负责把脚本写好并自测；不要修改仓库里现有翻译数据。

## 1. 目标与非目标

- 目标：把“一条通用校对 prompt 打全场”换成 **router(分类) → 每类专用 prompt → 校对 → 校验 → 汇总 diff**，
  从而减少通用模型的“润色式重写”，提高术语/语境准确性。
- 非目标：
  - 不追求模型自己“判定对错后自动落库”；输出候选提案，落库需后续复核。
  - 不审汉化组 legacy（默认），除非用户开启。
  - 不做全量无条件重写；只改真错。

## 2. 硬约束（任何 prompt 都必须遵守，写进系统提示）

1. 占位符 `{C} {B} {L} {X} {Y} {A} {0} {1} [1] [2]` 原样保留、数量与顺序不变；不得用标点替换/删除。
2. 简体中文；不用半角逗号 `,`；不含 `\n`/`\r`。
3. 品牌/专名保留英文：Rocksmith、Ubisoft、Steam、PSN、Xbox LIVE、PlayStation、Real Tone Cable、歌/艺人/吉他型号。
4. 已翻译成中文的音色/预设/风格名不要改回英文。
5. 代词：玩家用“你”；歌曲/物品用“它/它们”，不用“她”。
6. **只改真正的错误；现译准确自然就原样返回；不要为了改写而改写。**

## 3. 已落地术语（写进 prompt，禁止反向修改）

profile=玩家档案；cab/box=箱体；amp=音箱；head=音箱头；combo=一体式音箱；speaker driver=扬声器单元；
inline=联排；fret-hand mute=左手制音；palm mute=手掌制音；slide=滑音；
Scale Shape=音阶指型；Arpeggio=琶音；Technique=技巧；Authentic Tone=原曲音色；Complexity=复杂度；
Path=演奏路径；D-pad=十字键；Session Drums=即兴鼓组；session=会话；match=对局；matchmaking=匹配；
group leader=队长；host=房主；event(活动)=活动；streak=连击；Slap=拍弦；Pop=勾拍；
major chord=大三和弦；octave=八度音程；Phrygian Dominant=弗里吉亚属音阶。

## 4. 复用现有代码（不要重造轮子）

- `scripts/localization.py`：`load_slots`（读 maingame.csv）、`load_json`、`write_json`、`CJK_RE`、`PLACEHOLDER_RE`。
- 并发/断点续传参考 `scripts/translate_remaining.py` 的 worker 写法（ThreadPool、按 worker 落盘、续传）。
- ollama 调用参考 `scripts/translate_remaining.py::chat_once/restore_and_map`（含占位符拆分与还原、
  id 匹配、validate）。
- 服务配置：`config/workers.json`（4 个 server-gpu0..3，endpoint `http://127.0.0.1:11435~11438`，
  model `qwen3.8:latest`，concurrency=2，batch=24）。
- 输入数据：
  - 现译：`data/translations_remaining.json`（16067，`{id:zh}`）
  - 英文原文：`learnplay_cache4/localization/maingame.csv`（id,英文,其余列…）
  - 跳过：`data/proofread_manual.json`(256)、`config/overrides.json`(64)
  - 规则全文：`review.md`（20 条规则）

## 5. 架构建议

```
translations_remaining.json ──► router（本地规则，不调模型）
                                   │  按 id 分类到若干“桶”
                                   ▼
      bucket A/B/C/… 各自批量调用 qwen3.8（每桶不同 SYSTEM prompt）
                                   ▼
        校验器：占位符/逗号/换行/空 → 输出 diff + 理由
                                   ▼
      data/proofread_routed.json（修订提案，含 original/revised/reason/category）
```

建议目录（GPT 自定，以下为推荐）：
```
scripts/proofreader/
  __init__.py
  router.py        # 分类
  prompts.py       # 每类 SYSTEM/提示词模板
  runner.py        # 并发/断点/校验/落盘
  cli.py           # argparse 入口
  README.md        # 说明 + 用法
```
入口示例：
```
uv run python -m scripts.proofreader.cli --current learnplay_cache4\localization\maingame.csv \
    --translations data\translations_remaining.json \
    --skip data\proofread_manual.json --skip config\overrides.json \
    --config config\workers.json --out data\proofread_routed.json \
    --changes data\proofread_routed_changes.json [--limit 500 --seed 42]
```

## 6. 分类桶（router）设计——核心

分类在本地用规则做，**每类一个专用 SYSTEM prompt**。建议桶：

| 桶 | 触发线索（关键词/正则，大小写不敏感） | 该桶 prompt 额外强调（除硬约束+术语） |
|---|---|---|
| A UI/短标签 | len≤20、无教学词、大写按钮词(CANCEL/MEDIUM…) | 菜单/按钮语境；全大写标题也要译中文；简短直接 |
| B 教学/教程 | slide/bend/fret/fretboard/string/chord/pick/mute/palm/technique/指法/按弦/扫弦/拨弦/推弦/滑音… | 完整应用 20 条规则中的动作/否定/方向/指法/节拍/口语化（规则2-9、19） |
| C 任务/成就 | beat/score/at least/in a row/in a single game/without/before/collect/destroy/超过/连续/一局内… | 逐项保留任务条件与数字量词（规则15、16），数值顺序核对 |
| D 多人/在线 | Xbox/PSN/PlayStation/LIVE/session/match/host/party/profile/online | 术语表多人段；避免“被返回”等翻译腔；允许省略主语 |
| E 设备/效果器/音色 | cab/amp/head/combo/tone/pedal/fuzz/overdrive/wah/drive/electronic/pad… | 设备/效果器专词（规则11-12），音色/风格名保持中文不回英文 |
| F 界面/系统提示 | title/menu/continue/exit/error/load/save/settings/…短提示 | 简洁自然；禁止漏译标题（规则18） |
| G 一般叙述 | 长句、教学已覆盖之外的说明 | 通用：自然中文、只改真错、代词/先行词（规则17、19） |
| SKIP | 无字母/纯数字/和弦符号/品牌型号正则（Epiphone®…、Am7、640x480）/纯占位符 | 不调模型 |

路由优先级：SKIP 最先，其次按关键词命中多个桶时**取第一个命中**（桶顺序自定义，建议 B 早于 G，C 早于 G，E 早于 G）。无法归入的进 G。

## 7. Prompt 模板要求

每桶 SYSTEM 至少包含：
1. 角色句（如“你是 Rocksmith 吉他教学文本的资深校对”）。
2. 第 2 节“硬约束”全量。
3. 第 3 节“术语表”（可按桶裁剪，但 profile/cab/联排/制音/音阶指型等核心必带）。
4. 第 6 节该桶“额外强调”（引用 review.md 对应规则编号）。
5. 输出指令：`只输出 JSON 对象 {"translations":[{"id","text"}]}，数量与输入一致，id 一一对应；现译正确就原样返回`。
USER 内容：`[{"id","source","translation"}]` 数组。

## 8. 校验与输出

- 每个 id：占位符集合必须与 source 一致；无半角逗号/换行/空。
- 违反校验的候选**丢弃该条改动**（保留现译）并记入 skipped 计数。
- 输出：
  - `data/proofread_routed.json`：全部条目的最终建议文本（含未改），便于后续合并。
  - `data/proofread_routed_changes.json`：仅改动项 `{id:{source,original,revised,category,reason}}`。
  - reason：模型可给一句理由（如“漏译/术语/语病/条件丢失”），供复核。
- 断点续传：参考 translate_remaining 按 worker part 文件；中途可续。

## 9. 验收标准（GPT 写完自测）

1. `--limit 200 --seed 42` 跑 200 条：改动率应明显低于通用 prompt 的 10-20%（目标 <8%），
   且**不应出现**：占位符被删、中文改回英文音色名、profile 变回配置文件、无意义润色。
2. 分类抽样：A~G 每类至少 20 条，确认路由合理、prompt 生效。
3. `uv run python -m py_compile scripts\proofreader\*.py` 通过。
4. 占位符校验在 200 条上为 0 违例。

## 10. 参考（GPT 可读）

- 规则全文：`./review.md`
- 术语/上下文：`...\docs\gpt_fullproofread_guide.md`
- 现有调用/并发示例：`...\scripts\translate_remaining.py`、`...\scripts\localization.py`
- 数据样例：`...\data\translations_remaining.json`、`...\learnplay_cache4\localization\maingame.csv`
