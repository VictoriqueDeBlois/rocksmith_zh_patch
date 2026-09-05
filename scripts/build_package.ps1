<#
.SYNOPSIS
  重建 Rocksmith 2014 汉化缓存并打包 cache.psarc。

.DESCRIPTION
  步骤:
    1. 用 data/translations_final.json 生成汉化版 maingame.csv 到 work/hybrid_cache4
    2. 复用 hybrid_cache8(含中文字体 fonts.gfx) 作为 cache8 内容
    3. 用 7za 重新压成 cache4.7z / cache8.7z
    4. 与原版其余 cacheX.7z 组装到 work/package (不需要 NamesBlock.bin)
    5. 用 RocksmithToolkit packer.exe 打包出 cache.psarc
  产物: work/hybrid_built/cache.psarc
  说明: packer -p 的输入是只含 cacheX.7z 的目录; NamesBlock.bin 由 packer 生成。
#>
param(
    [string]$Python = "",
    [string]$Root = $PSScriptRoot
)
$ErrorActionPreference = "Stop"
if (-not $Python) {
    $venvPy = Join-Path $Root ".venv\Scripts\python.exe"
    if (Test-Path -LiteralPath $venvPy) { $Python = $venvPy } else { $Python = "python" }
}
chcp 65001 > $null
$utf8 = [System.Text.UTF8Encoding]::new($false)
[Console]::InputEncoding = $utf8
[Console]::OutputEncoding = $utf8
$OutputEncoding = $utf8

$legacyCsv   = Join-Path $Root "legacy_cache4\localization\maingame.csv"
$currentCsv  = Join-Path $Root "learnplay_cache4\localization\maingame.csv"
$finalJson   = Join-Path $Root "data\translations_final.json"
$legacyJson  = Join-Path $Root "data\translations_legacy.json"
$mergedJson  = Join-Path $Root "data\translations_merged.json"
$remaining   = Join-Path $Root "data\translations_remaining.json"
$proofJson   = Join-Path $Root "data\translations_proofread.json"
$ovJson      = Join-Path $Root "config\overrides.json"

$learnplayCache4 = Join-Path $Root "learnplay_cache4"
$hybridCache4    = Join-Path $Root "work\hybrid_cache4"
$hybridCache8    = Join-Path $Root "hybrid_cache8"
$hybridCache8Out = Join-Path $Root "work\hybrid_cache8"
$origUnpack      = Join-Path $Root "unpacked_learnplay\cache.psarc.learnplay-original-20260905.bak_RS2014_Pc"
$pkgDir          = Join-Path $Root "work\package"
$outDir          = Join-Path $Root "work\hybrid_built"
$sevenZip        = Join-Path $Root "rstoolkit\RocksmithToolkit\tools\7za.exe"
$packer          = Join-Path $Root "rstoolkit\RocksmithToolkit\packer.exe"

function Assert-Exists([string]$p, [string]$msg) {
    if (-not (Test-Path -LiteralPath $p)) { throw "$msg : $p" }
}
Assert-Exists $legacyCsv   "缺少老版 CSV"
Assert-Exists $currentCsv  "缺少当前版 CSV"
Assert-Exists $hybridCache8 "缺少 hybrid_cache8 (中文字体)"
Assert-Exists $origUnpack  "缺少原版解包目录"
Assert-Exists $sevenZip "缺少 7za"
Assert-Exists $packer   "缺少 packer"

# ---------- 0. 前置数据 ----------
& $Python -X utf8 (Join-Path $Root "scripts\extract_legacy_translations.py") $legacyCsv $legacyJson
if ($LASTEXITCODE -ne 0) { throw "extract_legacy_translations failed" }

$aiArgs = @()
if (Test-Path -LiteralPath $proofJson) { $aiArgs += $proofJson }
if (Test-Path -LiteralPath $remaining) { $aiArgs += $remaining }
if (Test-Path -LiteralPath $mergedJson) { $aiArgs += $mergedJson }
if ($aiArgs.Count -eq 0) { throw "没有可用的 AI 翻译 json" }

$auditArgs = @(
    (Join-Path $Root "scripts\merge_and_audit_translations.py"),
    "--current", $currentCsv,
    "--legacy-json", $legacyJson,
    "--overrides", $ovJson,
    "--out", $finalJson,
    "--report", (Join-Path $Root "data\audit_final.json")
)
foreach ($a in $aiArgs) { $auditArgs += @("--ai", $a) }
& $Python -X utf8 @auditArgs
if ($LASTEXITCODE -ne 0) { throw "merge_and_audit_translations failed" }

# ---------- 1. hybrid cache4 (仅替换 maingame.csv) ----------
if (Test-Path -LiteralPath $hybridCache4) { Remove-Item -LiteralPath $hybridCache4 -Recurse -Force }
Copy-Item -LiteralPath $learnplayCache4 -Destination $hybridCache4 -Recurse
& $Python -X utf8 (Join-Path $Root "scripts\build_hybrid_localization.py") `
    --current $currentCsv `
    --translations $finalJson `
    --out (Join-Path $hybridCache4 "localization\maingame.csv")
if ($LASTEXITCODE -ne 0) { throw "build_hybrid_localization failed" }

# ---------- 2. hybrid cache8 (复用含中文 glyph 的字体) ----------
if (Test-Path -LiteralPath $hybridCache8Out) { Remove-Item -LiteralPath $hybridCache8Out -Recurse -Force }
Copy-Item -LiteralPath $hybridCache8 -Destination $hybridCache8Out -Recurse

# ---------- 3. 重新压缩 cache4 / cache8 ----------
if (-not (Test-Path -LiteralPath $pkgDir)) { New-Item -ItemType Directory -Force -Path $pkgDir | Out-Null }
$cache4New = Join-Path $pkgDir "cache4.7z"
$cache8New = Join-Path $pkgDir "cache8.7z"
if (Test-Path -LiteralPath $cache4New) { Remove-Item -LiteralPath $cache4New -Force }
if (Test-Path -LiteralPath $cache8New) { Remove-Item -LiteralPath $cache8New -Force }
Push-Location $hybridCache4
try { & $sevenZip a -t7z -mx=5 $cache4New * | Out-Null } finally { Pop-Location }
if ($LASTEXITCODE -ne 0) { throw "7za cache4 failed" }
Push-Location $hybridCache8Out
try { & $sevenZip a -t7z -mx=5 $cache8New * | Out-Null } finally { Pop-Location }
if ($LASTEXITCODE -ne 0) { throw "7za cache8 failed" }

# ---------- 4. 组装其余原版 cache (不要 NamesBlock.bin) ----------
foreach ($name in @("cache0.7z","cache1.7z","cache3.7z","cache6.7z","cache7.7z")) {
    $src = Join-Path $origUnpack $name
    Assert-Exists $src "缺少原版 $name"
    Copy-Item -LiteralPath $src -Destination (Join-Path $pkgDir $name) -Force
}

# ---------- 5. packer 打包 cache.psarc ----------
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Force -Path $outDir | Out-Null }
& $packer -p -f Pc -v RS2014 -i $pkgDir -o (Join-Path $outDir "cache")
if ($LASTEXITCODE -ne 0) { throw "packer failed" }
$outPsarc = Join-Path $outDir "cache.psarc"
Assert-Exists $outPsarc "打包失败, 未生成 cache.psarc"
Write-Output ""
Write-Output "完成: $outPsarc"
Write-Output ("大小: " + (Get-Item -LiteralPath $outPsarc).Length + " bytes")
