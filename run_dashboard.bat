@echo off
echo ========================================
echo Starting Marketplace Insights Dashboard
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first to set up the project.
    pause
    exit /b 1
)

REM Activate virtual environment and run dashboard
call venv\Scripts\activate.bat
echo Starting Streamlit dashboard...
echo Press Ctrl+C to stop the server
echo.
streamlit run marketplace_dashboard.py
