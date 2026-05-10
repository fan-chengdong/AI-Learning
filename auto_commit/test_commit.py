#!/usr/bin/env python3
import os
import datetime
import sys

def main():
    """测试自动提交功能"""
    test_file = "test_auto_commit.txt"
    
    print(f"[{datetime.datetime.now()}] 开始测试自动提交功能...")
    
    # 创建测试文件
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(f"测试自动提交 - {datetime.datetime.now()}\n")
    
    print(f"  创建测试文件: {test_file}")
    
    # 调用自动提交脚本
    import git_auto_commit
    git_auto_commit.main()
    
    # 清理测试文件
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"  清理测试文件: {test_file}")
    
    print(f"[{datetime.datetime.now()}] 测试完成！")

if __name__ == '__main__':
    main()