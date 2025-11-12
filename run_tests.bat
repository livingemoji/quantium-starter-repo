@echo off
REM Pink Morsel Sales Dashboard - CI Test Script (Windows Batch)
REM This script is designed to be run by CI/CD systems to validate the application
REM 
REM Functionality:
REM - Activates the project virtual environment
REM - Runs the test suite with pytest
REM - Returns exit code 0 on success, 1 on failure
REM
REM Usage: run_tests.bat

setlocal enabledelayedexpansion

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

echo.
echo ================================
echo Pink Morsel Sales Dashboard - CI
echo ================================
echo.

REM Step 1: Check if virtual environment exists
echo Step 1: Checking virtual environment...
if not exist ".venv" (
    echo.
    echo [ERROR] Virtual environment not found at %SCRIPT_DIR%.venv
    echo Please create a virtual environment first:
    echo   python -m venv .venv
    echo.
    exit /b 1
)
echo [OK] Virtual environment found
echo.

REM Step 2: Activate virtual environment
echo Step 2: Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    exit /b 1
)
echo [OK] Virtual environment activated
python --version
pip --version
echo.

REM Step 3: Verify dependencies are installed
echo Step 3: Verifying dependencies...
python -c "import pandas; import dash; import plotly; import pytest" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Some dependencies are missing, attempting to install...
    pip install -q -r requirements.txt
    echo [OK] Dependencies installed
) else (
    echo [OK] All dependencies are installed
)
echo.

REM Step 4: Run the test suite
echo Step 4: Running test suite...
echo.
python -m pytest test_app.py -v --tb=short
set "TEST_RESULT=%errorlevel%"

echo.
echo ================================
echo.

REM Step 5: Print summary
if %TEST_RESULT% equ 0 (
    echo [SUCCESS] CI BUILD SUCCESSFUL
    echo ================================
    echo.
    exit /b 0
) else (
    echo [FAILED] CI BUILD FAILED
    echo ================================
    echo.
    exit /b 1
)
