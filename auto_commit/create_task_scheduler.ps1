# PowerShell脚本：创建Windows任务计划
# 以管理员身份运行此脚本

$taskName = "Git自动提交任务"
$scriptPath = Join-Path $PWD.Path "git_auto_commit.py"
$pythonPath = "python.exe"
$repoPath = Split-Path $PWD.Path -Parent

# 创建任务动作
$action = New-ScheduledTaskAction `
    -Execute $pythonPath `
    -Argument "`"$scriptPath`"" `
    -WorkingDirectory $repoPath

# 创建任务触发器（每天早上9点和下午5点执行）
$trigger1 = New-ScheduledTaskTrigger -Daily -At 09:00
$trigger2 = New-ScheduledTaskTrigger -Daily -At 17:00

# 设置任务设置
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable

# 注册任务
Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger1,$trigger2 `
    -Settings $settings `
    -Description "定期自动提交git仓库更新"

Write-Host "任务计划 '$taskName' 创建成功！"
Write-Host "任务将在每天 09:00 和 17:00 自动执行"
Write-Host "工作目录: $repoPath"