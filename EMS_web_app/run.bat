@echo off
REM EMS Controller Web App - Windows Launcher

setlocal enabledelayedexpansion

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

REM Prefer the Windows Python launcher when available, otherwise use python.
set PYTHON_CMD=py -3
%PYTHON_CMD% --version >nul 2>&1
if errorlevel 1 (
    set PYTHON_CMD=python
    %PYTHON_CMD% --version >nul 2>&1
    if errorlevel 1 (
        echo Error: Python is not installed or not in PATH.
        echo Please install Python 3.10+ from https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

REM Check Python version.
%PYTHON_CMD% -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if errorlevel 1 (
    echo Error: Python 3.10 or newer is required.
    %PYTHON_CMD% --version
    pause
    exit /b 1
)

echo EMS Controller Web App
echo.

REM Install/update dependencies from requirements.txt. Do not hide errors;
REM otherwise missing Flask/Bleak becomes confusing and the real pip failure is invisible.
echo Checking required Python packages...
%PYTHON_CMD% -m pip install -r "%SCRIPT_DIR%requirements.txt"
if errorlevel 1 (
    echo.
    echo Error: Failed to install required packages.
    echo Try running this manually:
    echo   %PYTHON_CMD% -m pip install -r "%SCRIPT_DIR%requirements.txt"
    pause
    exit /b 1
)

REM Verify dependencies before starting.
%PYTHON_CMD% -c "import flask, flask_cors, bleak" >nul 2>&1
if errorlevel 1 (
    echo Error: Required Python packages are still missing.
    echo Try running this manually:
    echo   %PYTHON_CMD% -m pip install -r "%SCRIPT_DIR%requirements.txt"
    pause
    exit /b 1
)

%PYTHON_CMD% -c "import sys, bleak; print('Python', sys.version.split()[0]); print('Bleak', bleak.__version__)"

REM Run the Flask app
cd /d "%SCRIPT_DIR%"

REM Open browser
echo.
echo Opening browser at http://localhost:5000
timeout /t 2 /nobreak >nul

start http://localhost:5000

echo.
echo Starting Flask server...
echo.
%PYTHON_CMD% app.py

REM Keep window open
pause
