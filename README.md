# Rocksmith 2014 中文化管线 (rocksmith_zh_patch)

> Rocksmith 2014 (Remastered) Simplified-Chinese localization toolchain & scripts.
> 只包含脚本、流程和本仓库作者整理的译文/审阅记录；**不包含游戏本体或任何游戏资源文件**。
> 使用需要你自己拥有合法游戏并自行解包(见下文“复现需要”)。

把 Rocksmith 2014 (Remastered / learnplay) 的英文 UI 文本补全为中文。
沿用之前 agent 的方案：把中文写入 `maingame.csv` 的 **English 列**
(第 2 列)，游戏以英文语言运行时即显示中文；`cache4` 的主界面字体
(`fonts.gfx`) 和 `cache8` 的字体 (`fontsgc.gfx`) 均使用老汉化的中文版本。

## 背景

- `legacy`(老版, 2014)：网上流传的“摇滚史密斯2014汉化补丁 v3”，
  **人工汉化组**把部分文本(简体中文)写进 English 列，共 4022 条；
- `learn_play`(当前版, Remastered)：游戏本体 cache.psarc 解包出的
  maingame.csv，共 20143 行；其中 578 条是老版没有的新文本；
- 之前 agent 用 ollama 把 578 条新文本译成简体中文
  (`data/translations_merged.json`)；
- **本仓库新增**：把汉化组没翻译的其余 ~15500 条英文全部用 ollama 翻译，
  并对 AI 译文用更强模型(服务器 ollama)校对(汉化组人工译文自动跳过)，
  最后重建 cache.psarc。

当前使用汉化组旧版的简体译文，优先保留人工翻译；明确的误译通过人工覆盖表修正。

## 当前状态

- 合并译文 18,643 条；构建审计无漏译、无占位符错误。
- 修复重建时遗漏主界面中文字体的问题，打包后回读并校验两份字体。
- 复核并修订 78 条设置文本，包括“舞台模式”、音频独占、全屏模式和难度调整说明。
- [设置翻译修改对照](docs/settings_translation_review.md)。游戏内字形和菜单排版仍需实际游玩验证。

## 本地构建需要

仓库不提供可直接安装的游戏资源包。构建前需要自行准备：

1. Windows、Python 3.12 或更新版本，以及 PowerShell。
2. 当前 Remastered 版本解包的 `learnplay_cache4/`，包含 `localization/maingame.csv`。
3. 老汉化解包的 `legacy_cache4/`，包含根目录简体 `maingame.csv` 和 `gfxassets/localization/fonts.gfx`。
4. `hybrid_cache8/`，使用当前版本缓存结构并包含老汉化的 `gfxassets/localization/fontsgc.gfx`。
5. 当前原版 PSARC 解包目录；默认路径见 `scripts/build_package.ps1` 中的 `$origUnpack`，可按实际目录调整。
6. RocksmithToolkit 的 `packer.exe` 和 `tools/7za.exe`，放在 `rstoolkit/RocksmithToolkit/` 下。

已有完整译文，重建补丁无需运行 AI 翻译或配置 API 密钥。执行 `uv sync` 后运行
`.\scripts\build_package.ps1`，产物为 `work/hybrid_built/cache.psarc`。
退出游戏并备份游戏目录原有 `cache.psarc` 后，再复制产物替换；恢复备份即可撤销安装。
游戏应以英文语言运行，因为中文文本写入 English 列。

## 环境 (uv)

```powershell
uv sync            # 创建 .venv (Python 3.12)
uv run python scripts\xxx.py ...
```
所有脚本只依赖标准库；翻译/校对调用 ollama HTTP API。

## 配置：只使用远程服务器 ollama (qwen3.8)

`config/workers.json` 已配置为**只连远程服务器** `remote-ollama-host` 的
`qwen3.8:latest`，不调用本机模型：

```json
{
  "workers": [
    {
      "name": "server-gpu",
      "endpoint": "http://127.0.0.1:11435",
      "model": "qwen3.8:latest",
      "concurrency": 1,
      "weight": 1,
      "batch_size": 24,
      "timeout": 900
    }
  ]
}
```

运行前先建立 SSH 隧道(把服务器 11434 映射到本机 11435)：
```powershell
ssh -N -L 11435:127.0.0.1:11434 remote-ollama-host
curl http://127.0.0.1:11435/api/tags   # 自检
```

`config/workers.example.json` 只是“本机+服务器并行”示例，供以后需要时参考。

## 目录

```
scripts/
  localization.py                    # 共享工具(CJK/占位符/CSV 读写)
  analyze_localization.py            # 分析新旧 CSV 差异(参考用)
  extract_legacy_translations.py     # 提取汉化组人工译文 -> json
  translate_new_strings.py           # 旧版: 只翻译新 id(参考用)
  translate_remaining.py             # 翻译全部剩余英文(断点续传/多 worker)
  proofread_translations.py          # 用 ollama 校对 AI 译文(参考用)
  proofread_translations_api.py     # 用 DeepSeek V4 Flash API 校对(主用, 支持并发/抽样)
  merge_and_audit_translations.py    # 合并+审计 -> translations_final.json
  apply_translation_overrides.py     # 把人工术语覆盖写入某个 json
  build_hybrid_localization.py       # 把 final 写回 maingame.csv English 列
  build_package.ps1                  # 重建 cache4/cache8.7z 并打包 psarc
config/
  workers.json                       # 远程服务器 qwen3.8 (翻译用)
  workers.example.json               # 本机+服务器并行示例
  api.example.json                   # DeepSeek API 配置模板(复制为 api.json 填 key)
  overrides.json                     # 人工复核过的 UI 术语覆盖
data/
  translations_legacy.json           # 汉化组人工译文 (id -> 中文)
  translations_local.json            # 之前本机 ollama 译文
  translations_remote.json           # 之前服务器 ollama 译文
  translations_merged.json           # 之前 AI 译文(578 条新文本)
  translations_proofread.json        # 校对结果(之前的 AI 译文, qwen3.8)
  proofread_changes.json             # 校对改动明细
  translations_remaining.json        # [生成] 剩余英文 -> 中文
  translations_final.json            # [生成] 最终合并(override>汉化组>AI)
```

游戏解包/缓存目录(不入库)：
```
legacy_cache4/            # 老版汉化 cache4 解包 (maingame.csv 简体 + localization/ 繁体副本)
learnplay_cache4/         # 当前版 cache4 解包 (基准)
learnplay_cache8/         # 当前版 cache8 解包
hybrid_cache4|8/          # 之前生成的含字体/译文缓存
unpacked_legacy|learnplay/ # packer 解出的 cacheX.7z
cache_RS2014_Pc/          # packer -p 的输入(cacheX.7z)
rstoolkit/                # RocksmithToolkit (packer.exe, tools/7za.exe)
```

## 完整流程

1) 提取汉化组人工译文(只跑一次)：
```powershell
uv run python scripts\extract_legacy_translations.py legacy_cache4\maingame.csv data\translations_legacy.json
```

2) 翻译剩余英文(用服务器 qwen3.8，断点续传，每批落盘)：
```powershell
uv run python scripts\translate_remaining.py --legacy legacy_cache4\maingame.csv --current learnplay_cache4\localization\maingame.csv --out data\translations_remaining.json --config config\workers.json
```

3) 校对 AI 译文(DeepSeek V4 Flash API，跳过汉化组人工条目)：
   先填 key：把 config\api.example.json 复制为 config\api.json，填入 api_key。
   建议先抽 100 条看效果，再全量：
```powershell
uv run python scripts\proofread_translations_api.py --current learnplay_cache4\localization\maingame.csv --translations data\translations_remaining.json --skip data\translations_legacy.json --out data\proofread_sample.json --changes data\proofread_sample_changes.json --api-config config\api.json --limit 100 --seed 42

uv run python scripts\proofread_translations_api.py --current learnplay_cache4\localization\maingame.csv --translations data\translations_remaining.json --skip data\translations_legacy.json --out data\translations_proofread.json --changes data\proofread_changes.json --api-config config\api.json
```

4) 合并+审计(生成 `data\audit_final.json`，应看到 missing_count=0)。
   默认构建优先级：人工 overrides > 汉化组 legacy > 人工锁定 proofread_manual > 新翻译：
```powershell
uv run python scripts\merge_and_audit_translations.py --current learnplay_cache4\localization\maingame.csv --legacy-json data\translations_legacy.json --ai data\proofread_manual.json data\translations_remaining.json --overrides config\overrides.json --out data\translations_final.json --report data\audit_final.json
```

5) 生成汉化 CSV + 重建缓存与 psarc(自动使用 .venv 里的 python)：
```powershell
.\scripts\build_package.ps1
```
产物：`work\hybrid_built\cache.psarc`(替换游戏根目录同名文件即可)。

## 打包说明

`scripts/build_package.ps1` 执行 0-5 全部步骤并生成
`work/hybrid_built/cache.psarc`。packer -p 的输入目录只放
`cache0.7z ... cache8.7z`(不需要 NamesBlock.bin，packer 会重建)。
构建会显式复制 `legacy_cache4/gfxassets/localization/fonts.gfx`，并回读
cache4/cache8 压缩包核对两份中文字体的 SHA-256，避免英文原版字体被误打包。

## 已知问题 / 备注

- 占位符如 {C} {B} {L} {X} [1] 必须原样保留；脚本自动拆分并在校验时核对。
- 请求 id 使用稳定短 id，避免模型因超长/特殊字符 id 而漏译。
- 半角逗号会被替换为中文逗号，避免破坏 CSV 列结构。
- 汉化组译文为简体，未参与 AI 校对(按需求跳过)。
- 音乐记号/音名/品牌名等由模型保留英文；纯数字/符号行不会送译。

## 后台运行翻译 (Windows 无原生 tmux)

用 `scripts\run_translate_bg.ps1` 把翻译放到隐藏后台进程跑，日志写
`work\translate_bg.log`，关掉窗口也不影响；随时可看进度/停止。

```powershell
.\scripts\run_translate_bg.ps1 start        # 后台启动(自动续传)
.\scripts\run_translate_bg.ps1 status       # 运行状态 + 已翻译条数
.\scripts\run_translate_bg.ps1 log -Wait    # 实时跟随日志 (Ctrl+C 退出)
.\scripts\run_translate_bg.ps1 log -Tail 30 # 只看最近 30 行
.\scripts\run_translate_bg.ps1 stop         # 停止
```
