# Rocksmith 2014 中文化管线 (rocksmith_zh_patch)

把 Rocksmith 2014 (Remastered / learnplay) 的英文 UI 文本补全为中文。
沿用之前 agent 的方案：把中文写入 `maingame.csv` 的 **English 列**
(第 2 列)，游戏以英文语言运行时即显示中文；`cache8` 里的字体
(`fontsgc.gfx`) 已替换为含中文 glyph 的版本。

## 背景

- `legacy`(老版, 2014)：网上流传的“摇滚史密斯2014汉化补丁 v3”，
  **人工汉化组**把部分文本(繁体中文)写进 English 列，共 4022 条；
- `learn_play`(当前版, Remastered)：游戏本体 cache.psarc 解包出的
  maingame.csv，共 20143 行；其中 578 条是老版没有的新文本；
- 之前 agent 用 ollama 把 578 条新文本译成简体中文
  (`data/translations_merged.json`)；
- **本仓库新增**：把汉化组没翻译的其余 ~15500 条英文全部用 ollama 翻译，
  并对 AI 译文用更强模型(服务器 ollama)校对(汉化组人工译文自动跳过)，
  最后重建 cache.psarc。

> 注意：汉化组译文是繁体，AI 新译文是简体。如需统一可后续加 OpenCC 转换。

## 目录

```
scripts/
  localization.py                    # 共享工具(CJK/占位符/CSV 读写)
  analyze_localization.py            # 分析新旧 CSV 差异(参考用)
  extract_legacy_translations.py     # 提取汉化组人工译文 -> json
  translate_new_strings.py           # 旧版: 只翻译新 id(参考用)
  translate_remaining.py             # 新版: 翻译全部剩余英文, 支持多 ollama 并行
  proofread_translations.py          # 用 ollama 校对 AI 译文(跳过汉化组)
  merge_and_audit_translations.py    # 合并+审计 -> translations_final.json
  apply_translation_overrides.py     # 把人工术语覆盖写入某个 json
  build_hybrid_localization.py       # 把 final 写回 maingame.csv English 列
  build_package.ps1                  # 重建 cache4/cache8.7z 并打包 psarc
config/
  workers.json                       # 本机 ollama (默认)
  workers.server.json                # 服务器 ollama (SSH 隧道 11435)
  workers.example.json               # 本机 + 服务器并行示例
  overrides.json                     # 人工复核过的 UI 术语覆盖
data/
  translations_legacy.json           # 汉化组人工译文 (id -> 中文)
  translations_local.json            # 之前本机 ollama 译文
  translations_remote.json           # 之前服务器 ollama 译文
  translations_merged.json           # 之前 AI 译文(578 条新文本)
  translations_merged.reaudit.json   # 之前重审后的副本
  translations_remaining.json        # [生成] 剩余英文 -> 中文
  translations_proofread.json        # [生成] 校对结果(之前的 AI 译文)
  translations_final.json            # [生成] 最终合并(override>汉化组>AI)
```

游戏解包/缓存目录(不入库)：

```
legacy_cache4/            # 老版汉化 cache4 解包 (localization/maingame.csv)
learnplay_cache4/         # 当前版 cache4 解包 (基准)
learnplay_cache8/         # 当前版 cache8 解包
hybrid_cache4|8/          # 之前生成的含字体/译文缓存
unpacked_legacy|learnplay/ # packer 解出的 cacheX.7z
cache_RS2014_Pc/          # packer -p 的输入(cacheX.7z)
rstoolkit/                # RocksmithToolkit (packer.exe, tools/7za.exe)
```

## 完整流程

0) 前置：本机/服务器跑 ollama；把 endpoint/model 写进
   `config/workers.json`(示例见 `config/workers.example.json`)。

1) 提取汉化组人工译文(只跑一次)：
```powershell
python scripts/extract_legacy_translations.py `
    legacy_cache4/localization/maingame.csv data/translations_legacy.json
```

2) 翻译剩余英文(断点续传；多 worker 时每个 worker 写 part 文件)：
```powershell
python scripts/translate_remaining.py `
    --legacy legacy_cache4/localization/maingame.csv `
    --current learnplay_cache4/localization/maingame.csv `
    --existing data/translations_merged.json `
    --out data/translations_remaining.json `
    --config config/workers.json
```

3) 校对 AI 译文(跳过汉化组人工条目；建议用更强模型)：
```powershell
python scripts/proofread_translations.py `
    --current learnplay_cache4/localization/maingame.csv `
    --translations data/translations_merged.json `
    --skip data/translations_legacy.json `
    --out data/translations_proofread.json `
    --changes data/proofread_changes.json `
    --config config/workers.server.json
```

4) 合并+审计：
```powershell
python scripts/merge_and_audit_translations.py `
    --current learnplay_cache4/localization/maingame.csv `
    --legacy-json data/translations_legacy.json `
    --ai data/translations_proofread.json data/translations_remaining.json data/translations_merged.json `
    --overrides config/overrides.json `
    --out data/translations_final.json `
    --report data/audit_final.json
```

5) 生成汉化 CSV + 重建缓存与 psarc：
```powershell
.\scripts\build_package.ps1
```
产物：`work/hybrid_built/cache.psarc`(替换游戏根目录同名文件即可)。

## 并行使用服务器 ollama

SSH 隧道示例(服务器 ollama 只监听 127.0.0.1 时)：
```powershell
ssh -N -L 11435:127.0.0.1:11434 remote-ollama-host
```
然后把服务器 worker 加进 `config/workers.json`：
```json
{ "name": "server-gpu", "endpoint": "http://127.0.0.1:11435", "model": "qwen3.8:latest" }
```

`translate_remaining.py` 会按 weight 把文本切片分给各 worker 线程并行、
各自断点续传、最后自动合并。也可以分开跑：
```powershell
python scripts/translate_remaining.py ... --worker server-gpu   # 只跑服务器
python scripts/translate_remaining.py ... --merge-only          # 合并 part
```

## 打包说明

`scripts/build_package.ps1` 执行 0-5 全部步骤并生成
`work/hybrid_built/cache.psarc`。packer -p 的输入目录只放
`cache0.7z ... cache8.7z`(不需要 NamesBlock.bin，packer 会重建)。

## 已知问题 / 备注

- 占位符如 {C} {B} {L} {X} [1] 必须原样保留；脚本自动拆分并在校验时核对。
- 请求 id 使用稳定短 id，避免模型因超长/特殊字符 id 而漏译。
- 半角逗号会被替换为中文逗号，避免破坏 CSV 列结构。
- 汉化组繁体译文未做繁→简转换，也未参与 AI 校对(按需求跳过)。
- 音乐记号/音名/品牌名等由模型保留英文；纯数字/符号行不会送译。
