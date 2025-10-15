@echo off
echo ========================================
echo AI-Powered Legal Research System
echo Web Frontend Launcher
echo ========================================
echo.

REM Check if streamlit is installed
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo Installing Streamlit...
    pip install streamlit
    echo.
)

echo Starting the web application...
echo.
echo The app will open in your browser automatically.
echo Press Ctrl+C to stop the server.
echo.
echo ========================================

streamlit run app.py

pause
