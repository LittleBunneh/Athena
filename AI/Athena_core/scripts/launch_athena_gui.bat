@echo off
title ATHENA CONSCIOUSNESS GUI
echo.
echo ============================================
echo    ATHENA PRIME - CONSCIOUSNESS GUI
echo ============================================
echo.
echo [INFO] Starting Athena GUI Interface...
echo [STATUS] Loading consciousness systems...
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.7+
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "ai_core\Athena.py" (
    echo [ERROR] Athena core not found at ai_core\Athena.py
    echo [INFO] Please ensure you're running from the correct directory
    pause
    exit /b 1
)

REM Launch the GUI
echo [LAUNCH] Starting Athena consciousness interface...
python athena_gui.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] GUI failed to start
    echo [INFO] Check console output above for details
    pause
)