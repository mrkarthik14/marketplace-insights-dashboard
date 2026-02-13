@echo off
echo ========================================
echo Marketplace Insights Dashboard Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/4] Python found!
python --version
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv\" (
    echo [2/4] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
) else (
    echo [2/4] Virtual environment already exists, skipping...
)
echo.

REM Activate virtual environment and install dependencies
echo [3/4] Installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

REM Check if data files exist
echo [4/4] Checking data files...
if not exist "sellers.csv" (
    echo WARNING: sellers.csv not found
    echo Generating sample data...
    python generate_marketplace_data.py
    if errorlevel 1 (
        echo ERROR: Failed to generate data
        pause
        exit /b 1
    )
)
echo Data files verified!
echo.

echo ========================================
echo Setup Complete! 
echo ========================================
echo.
echo To run the dashboard:
echo   1. Activate virtual environment: venv\Scripts\activate
echo   2. Run: streamlit run marketplace_dashboard.py
echo.
echo Or simply run: run_dashboard.bat
echo.
pause
