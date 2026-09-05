# 分类校对提案模块

在仓库根目录运行，使用现有 `config/workers.json` 的四个 Ollama 服务。默认排除人工锁定、overrides 和 legacy；只写提案，不修改翻译输入。无需新增 Python 依赖。

```powershell
uv run python -m scripts.proofreader.cli --limit 200 --seed 42 --out scripts/proofreader/selftest/release_random200.json --changes scripts/proofreader/selftest/release_random200_changes.json
```

分类覆盖验收另加 `--per-category 20`，使用不同的输出路径：

```powershell
uv run python -m scripts.proofreader.cli --limit 200 --seed 42 --per-category 20 --out scripts/proofreader/selftest/release_stratified200.json --changes scripts/proofreader/selftest/release_stratified200_changes.json
```

全量运行去掉 `--limit`。可覆盖 `--current`、`--translations`、`--config`、`--out`、`--changes`。`--skip` 可重复，并在默认两份锁定清单之外追加排除。`--include-legacy` 显式启用 legacy；`--legacy` 指定其 JSON。`--dry-run` 只路由、抽样并输出样本清单，不调用模型。默认路径相对仓库根目录，用户传入路径相对当前工作目录。

输出文件：

- `--out`：完整输入 id→建议文本，未抽到、排除和失败项保留输入文本；不是已批准的补丁。
- `--changes`：仅改动，含 source/original/revised/category/reason。缺少模型理由时明确标记待复核。
- `<out>.sample.json`：实际抽样输入和分类。
- `<out>.report.json`：完成数、失败数、改动率、被拒候选及最终校验问题。
- `<out>.part.<worker>.json`：每 worker 原子断点，保留原始候选、理由和拒绝原因。

相同参数重新执行即可续传。断点指纹包含实际样本、提示词、配置与 Python 实现；内容变化会拒绝旧断点，使用新输出名即可重新测试。网络/响应格式失败降级单条，仍失败不记完成，下次重试；有失败以退出码 2 结束。候选文本违反校验则保留原译并计入 skipped。原译自身可能已经违规，因此报告单独列出 final_violations，不能将拒绝坏候选等同于修好了原数据。

路由优先级为 SKIP → C → E → D → B → F → A → G，使用词边界减少子串误判；对教学连续动作、Session Mode 和型号有专门处理。七类 prompt 都包含完整硬约束、术语和从 review.md 提取的二十条规则。分类是启发式，混合语境仍需复核。

复用 `localization.load_slots/load_json/write_json/CJK_RE/PLACEHOLDER_RE`；新模块扩展数字花括号占位符。校对采用整句 source/translation 配对，避免拆段丢失否定和条件上下文；模型删除、增加或换序占位符时直接拒绝整条候选，不擅自修补语义位置。Ollama 协议与 translate_remaining.chat_once 一致，响应严格按 id 匹配。每 worker 有独立线程池和落盘锁，按桶分批，最多 batch_size 条/约 10000 输入字符。当前均分 id，不使用 weight 加权。

保护器检查占位符序列、空值、半角逗号、实际/字面换行、中文整句退回英文、profile 回退、新增“她”，以及短设备名新增英文词。还拒绝纯空格润色、仅有风格理由的改写、Score Attack/叉键术语回退和孤立 Combo/head/box/drive/pad 的不确定改译。这些检查偏保守，可能拒绝合理修复，仍保留原始候选供复核。简繁、所有专名、意义正确性与无意义润色无法仅靠正则保证，验收需要逐项审阅改动。

本地检查（PowerShell 先执行项目 AGENTS.md 规定的 UTF-8 初始化）：

```powershell
uv run python -m unittest scripts.proofreader.test_proofreader
$files = (Get-ChildItem -LiteralPath scripts/proofreader -Filter '*.py').FullName
uv run python -m py_compile @files
```

PowerShell 不为 Python 展开 `*.py`，因此显式列举文件实现规格第 9 节的编译检查。离线测试覆盖路由、占位符顺序/次数、无效响应 id、分层抽样、失败重试、拒绝候选和断点失效；不能替代真实 qwen 自测。真实验收见 `selftest/RESULTS.md`。
