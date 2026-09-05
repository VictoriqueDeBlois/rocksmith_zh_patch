<#
.SYNOPSIS
  后台运行/查看/停止“剩余文本翻译”任务（断点续传，输出写日志，可随时 tail）。

.DESCRIPTION
  Windows 没有原生 tmux，这个脚本用隐藏后台进程 + 日志实现“启动后关掉窗口也不影响，
  想随时看进度就 tail 日志”。任务本身每批落盘，中断后重跑同一命令会自动续传。

.EXAMPLE
  .\scripts\run_translate_bg.ps1 start             # 后台启动翻译（默认动作）
  .\scripts\run_translate_bg.ps1 start -DryRun     # 只打印将要执行的命令，不启动
  .\scripts\run_translate_bg.ps1 status            # 进程状态 + 已翻译条数
  .\scripts\run_translate_bg.ps1 log -Tail 30      # 看最近 30 行日志
  .\scripts\run_translate_bg.ps1 log -Wait         # 实时跟随日志（Ctrl+C 退出）
  .\scripts\run_translate_bg.ps1 stop              # 停止后台任务
#>
param(
    [ValidateSet('start', 'status', 'log', 'stop')]
    [string]$Action = 'start',
    [int]$Tail = 30,
    [switch]$Wait,
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
chcp 65001 > $null
$utf8 = [System.Text.UTF8Encoding]::new($false)
[Console]::InputEncoding = $utf8
[Console]::OutputEncoding = $utf8
$OutputEncoding = $utf8

$Root       = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$WorkDir    = Join-Path $Root 'work'
$LogFile    = Join-Path $WorkDir 'translate_bg.log'
$ErrFile    = Join-Path $WorkDir 'translate_bg.err.log'
$PidFile    = Join-Path $WorkDir 'translate_bg.pid'
$VenvPy     = Join-Path $Root '.venv\Scripts\python.exe'
$Py         = if (Test-Path -LiteralPath $VenvPy) { $VenvPy } else { 'python' }
$Script     = Join-Path $Root 'scripts\translate_remaining.py'
$Progress   = Join-Path $Root 'data\translations_remaining.json'
$Failed     = Join-Path $Root 'data\translations_remaining.failed.json'

$ArgList = @(
    '-X', 'utf8',
    $Script,
    '--legacy',   (Join-Path $Root 'legacy_cache4\maingame.csv'),
    '--current',  (Join-Path $Root 'learnplay_cache4\localization\maingame.csv'),
    '--out',      (Join-Path $Root 'data\translations_remaining.json'),
    '--config',   (Join-Path $Root 'config\workers.json')
)

function Get-RunningPid {
    if (-not (Test-Path -LiteralPath $PidFile)) { return $null }
    $raw = (Get-Content -LiteralPath $PidFile -Raw).Trim()
    if ($raw -notmatch '^\d+$') { return $null }
    $proc = Get-Process -Id ([int]$raw) -ErrorAction SilentlyContinue
    if ($null -eq $proc) { return $null }
    return [int]$raw
}

function Write-CommandLine {
    Write-Output "命令: $Py $($ArgList -join ' ')"
}

switch ($Action) {
    'start' {
        if (-not $DryRun) {
            $existing = Get-RunningPid
            if ($null -ne $existing) {
                Write-Output "已在运行 (PID $existing)。先执行 stop 再 start，或直接看日志。"
                exit 1
            }
            New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null
            $p = Start-Process -FilePath $Py `
                -ArgumentList $ArgList `
                -WorkingDirectory $Root `
                -RedirectStandardOutput $LogFile `
                -RedirectStandardError $ErrFile `
                -WindowStyle Hidden -PassThru
            Set-Content -LiteralPath $PidFile -Value $p.Id -Encoding ascii
            Write-Output "已后台启动: PID $($p.Id)"
            Write-Output "日志: $LogFile"
            Write-Output "看进度:  $PSCommandPath log -Wait"
            Write-Output "停止:    $PSCommandPath stop"
        }
        else {
            Write-CommandLine
        }
    }
    'status' {
        $pidNow = Get-RunningPid
        if ($null -eq $pidNow) {
            Write-Output '状态: 未在运行'
        }
        else {
            Write-Output "状态: 运行中 (PID $pidNow)"
        }
        if (Test-Path -LiteralPath $Progress) {
            try {
                $data = Get-Content -LiteralPath $Progress -Raw | ConvertFrom-Json
                $count = ($data.PSObject.Properties | Measure-Object).Count
                Write-Output "已翻译 id 数: $count"
            }
            catch { Write-Output '进度文件读取失败(可能正在写入)' }
        }
        if (Test-Path -LiteralPath $Failed) {
            try {
                $f = Get-Content -LiteralPath $Failed -Raw | ConvertFrom-Json
                $fc = ($f.PSObject.Properties | Measure-Object).Count
                if ($fc -gt 0) { Write-Output "失败条目: $fc (见 $Failed)" }
            } catch { }
        }
        if (Test-Path -LiteralPath $LogFile) {
            Write-Output '--- 日志末尾 ---'
            Get-Content -LiteralPath $LogFile -Tail 5
        }
    }
    'log' {
        if (-not (Test-Path -LiteralPath $LogFile)) {
            Write-Output "还没有日志文件: $LogFile (先 start)"
            exit 1
        }
        if ($Wait) {
            Get-Content -LiteralPath $LogFile -Wait -Tail $Tail
        }
        else {
            Get-Content -LiteralPath $LogFile -Tail $Tail
        }
        if (Test-Path -LiteralPath $ErrFile) {
            $errLines = Get-Content -LiteralPath $ErrFile -ErrorAction SilentlyContinue
            if ($errLines) {
                Write-Output "--- stderr 末尾 ---"
                $errLines | Select-Object -Last $Tail
            }
        }
    }
    'stop' {
        $pidNow = Get-RunningPid
        if ($null -eq $pidNow) {
            Write-Output '没有在运行的后台任务'
        }
        else {
            Stop-Process -Id $pidNow -Force
            Write-Output "已停止 PID $pidNow"
        }
        if (Test-Path -LiteralPath $PidFile) { Remove-Item -LiteralPath $PidFile -Force }
    }
}
