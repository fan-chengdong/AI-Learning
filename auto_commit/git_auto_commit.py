#!/usr/bin/env python3
import os
import subprocess
import datetime
import sys
import time

def run_git_command(command, cwd=None, check=True):
    """执行git命令并返回输出"""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=check
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Git命令执行失败: {' '.join(command)}")
        print(f"错误信息: {e.stderr}")
        return None, e.stderr, e.returncode

def get_git_status(cwd=None):
    """检查git状态，返回是否有未提交的更改"""
    output, _, _ = run_git_command(['git', 'status', '--porcelain'], cwd)
    return output is not None and output != ''

def get_changed_files(cwd=None):
    """获取所有已更改的文件列表"""
    output, _, _ = run_git_command(['git', 'diff', '--name-only'], cwd)
    if output:
        return output.split('\n')
    return []

def update_changelog(commit_message, changed_files):
    """更新修改日志文件"""
    changelog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CHANGELOG.md')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    entry = f"## [{timestamp}]\n\n"
    entry += f"- **提交信息**: {commit_message}\n"
    entry += "- **修改文件**:\n"
    for file in changed_files:
        entry += f"  - {file}\n"
    entry += "\n"
    
    if os.path.exists(changelog_path):
        with open(changelog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(changelog_path, 'w', encoding='utf-8') as f:
            f.write(entry + content)
    else:
        with open(changelog_path, 'w', encoding='utf-8') as f:
            f.write("# 修改日志\n\n")
            f.write("所有自动提交的修改记录\n\n")
            f.write(entry)

def push_with_retry(repo_path, max_retries=3, retry_delay=5):
    """带重试机制的push操作，处理网络超时和分支冲突"""
    for attempt in range(max_retries):
        print(f"  推送到远程仓库 (尝试 {attempt + 1}/{max_retries})...")
        output, stderr, returncode = run_git_command(['git', 'push'], repo_path, check=False)
        
        if returncode == 0:
            print("  推送成功！")
            return True
        
        print(f"  推送失败: {stderr}")
        
        if "non-fast-forward" in stderr.lower() or "fetch first" in stderr.lower():
            print("  检测到分支冲突，尝试拉取并变基...")
            run_git_command(['git', 'fetch', 'origin', 'main'], repo_path)
            run_git_command(['git', 'rebase', 'origin/main'], repo_path)
        elif "timeout" in stderr.lower() or "timed out" in stderr.lower():
            print(f"  网络超时，等待 {retry_delay} 秒后重试...")
            time.sleep(retry_delay)
        else:
            print(f"  未知错误，等待 {retry_delay} 秒后重试...")
            time.sleep(retry_delay)
    
    print("  推送失败，已达到最大重试次数")
    return False

def main():
    repo_path = os.getcwd()
    print(f"[{datetime.datetime.now()}] 开始检查git仓库...")
    
    if not get_git_status(repo_path):
        print("  没有未提交的更改，跳过提交")
        return
    
    changed_files = get_changed_files(repo_path)
    print(f"  检测到 {len(changed_files)} 个文件有更改")
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commit_message = f"自动提交: {timestamp}"
    
    print(f"  添加所有更改...")
    run_git_command(['git', 'add', '.'], repo_path)
    
    print(f"  提交更改: {commit_message}")
    run_git_command(['git', 'commit', '-m', commit_message], repo_path)
    
    if push_with_retry(repo_path):
        print(f"  更新修改日志...")
        update_changelog(commit_message, changed_files)
        print(f"[{datetime.datetime.now()}] 自动提交完成")
    else:
        print(f"[{datetime.datetime.now()}] 自动提交失败")
        sys.exit(1)

if __name__ == '__main__':
    main()