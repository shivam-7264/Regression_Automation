@echo off
call cd /d F:\Automation_Regression >>Log.LOG
call py -m pip install --user virtualenv >>Log.LOG
call py -m venv env >>Log.LOG
call .\env\Scripts\activate >>Log.LOG
call pip install selenium pyautogui pytest openpyxl pytest-xdist matplotlib chromedriver_autoinstaller webdriver_manager >>Log.LOG
call pytest -W ignore -v -s -l >>Log.LOG
pause