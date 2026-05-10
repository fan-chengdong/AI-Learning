#!/usr/bin/env python3
import os
import subprocess
import datetime
import sys

def run_git_command(command, cwd=None):
    """执行git命令并返回输出"""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git命令执行失败: {' '.join(command)}")
        print(f"错误信息: {e.stderr}")
        return None

def get_git_status(cwd=None):
    """检查git状态，返回是否有未提交的更改"""
    output = run_git_command(['git', 'status', '--porcelain'], cwd)
    return output is not None and output != ''

def get_changed_files(cwd=None):
    """获取所有已更改的文件列表"""
    output = run_git_command(['git', 'diff', '--name-only'], cwd)
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
    
    print(f"  推送到远程仓库...")
    run_git_command(['git', 'push'], repo_path)
    
    print(f"  更新修改日志...")
    update_changelog(commit_message, changed_files)
    
    print(f"[{datetime.datetime.now()}] 自动提交完成")

if __name__ == '__main__':
    main()