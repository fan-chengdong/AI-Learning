@echo off
cd /d "%~dp0"
cd ..
python auto_commit\git_auto_commit.py
pause