@echo off
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
cd /d C:\Users\sushi\okurite
"C:\Users\sushi\anaconda3\python.exe" update_seasonal.py >> logs_auto.txt 2>&1
"C:\Users\sushi\anaconda3\python.exe" auto_publish.py 1 >> logs_auto.txt 2>&1
