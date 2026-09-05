<#
.SYNOPSIS
  后台运行分类路由多Prompt的 qwen 全文校对（proofreader），支持状态/日志/停止。

.EXAMPLE
  .\scripts\run_proofreader_bg.ps1 start        # 后台启动全量校对
  .\scripts\run_proofreader_bg.ps1 start -DryRun
  .\scripts\run_proofreader_bg.ps1 status
  .\scripts\run_proofreader_bg.ps1 log -Wait
  .\scripts\run_proofreader_bg.ps1 stop
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

$Root    = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$WorkDir = Join-Path $Root 'work'
$LogFile = Join-Path $WorkDir 'proofreader_bg.log'
$ErrFile = Join-Path $WorkDir 'proofreader_bg.err.log'
$PidFile = Join-Path $WorkDir 'proofreader_bg.pid'
$VenvPy  = Join-Path $Root '.venv\Scripts\python.exe'
$Py      = if (Test-Path -LiteralPath $VenvPy) { $VenvPy } else { 'python' }

$ArgList = @(
    '-X', 'utf8', '-m', 'scripts.proofreader.cli',
    '--out',      (Join-Path $Root 'data\proofread_routed.json'),
    '--changes',  (Join-Path $Root 'data\proofread_routed_changes.json')
)

function Get-RunningPid {
    if (-not (Test-Path -LiteralPath $PidFile)) { return $null }
    $raw = (Get-Content -LiteralPath $PidFile -Raw).Trim()
    if ($raw -notmatch '^\d+$') { return $null }
    if ($null -eq (Get-Process -Id ([int]$raw) -ErrorAction SilentlyContinue)) { return $null }
    return [int]$raw
}

switch ($Action) {
    'start' {
        if (-not $DryRun) {
            $existing = Get-RunningPid
            if ($null -ne $existing) {
                Write-Output "已在运行 (PID $existing)。先 stop 再 start。"; exit 1
            }
            New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null
            $p = Start-Process -FilePath $Py -ArgumentList $ArgList -WorkingDirectory $Root `
                -RedirectStandardOutput $LogFile -RedirectStandardError $ErrFile `
                -WindowStyle Hidden -PassThru
            Set-Content -LiteralPath $PidFile -Value $p.Id -Encoding ascii
            Write-Output "已后台启动 proofreader: PID $($p.Id)"
            Write-Output "日志: $LogFile"
            Write-Output "看进度: $PSCommandPath log -Wait"
        } else {
            Write-Output "命令: $Py $($ArgList -join ' ')"
        }
    }
    'status' {
        $pidNow = Get-RunningPid
        if ($null -eq $pidNow) { Write-Output '状态: 未在运行' }
        else { Write-Output "状态: 运行中 (PID $pidNow)" }
        $chg = Join-Path $Root 'data\proofread_routed_changes.json'
        if (Test-Path -LiteralPath $chg) {
            try { $c=(Get-Content -LiteralPath $chg -Raw | ConvertFrom-Json).PSObject.Properties.Count; Write-Output "已记录改动数: $c" } catch {}
        }
        if (Test-Path -LiteralPath $LogFile) { Write-Output '--- 日志末尾 ---'; Get-Content -LiteralPath $LogFile -Tail 8 }
    }
    'log' {
        if (-not (Test-Path -LiteralPath $LogFile)) { Write-Output "尚无日志: $LogFile (先 start)"; exit 1 }
        if ($Wait) { Get-Content -LiteralPath $LogFile -Wait -Tail $Tail }
        else { Get-Content -LiteralPath $LogFile -Tail $Tail }
        if (Test-Path -LiteralPath $ErrFile) {
            $err = Get-Content -LiteralPath $ErrFile -ErrorAction SilentlyContinue
            if ($err) { Write-Output '--- stderr 末尾 ---'; $err | Select-Object -Last $Tail }
        }
    }
    'stop' {
        $pidNow = Get-RunningPid
        if ($null -eq $pidNow) { Write-Output '没有运行中的任务' }
        else { Stop-Process -Id $pidNow -Force; Write-Output "已停止 PID $pidNow" }
        if (Test-Path -LiteralPath $PidFile) { Remove-Item -LiteralPath $PidFile -Force }
    }
}
