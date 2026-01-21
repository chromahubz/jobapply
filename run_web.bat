@echo off
REM Web UI launcher for JobApply (Windows)

REM Check if .env exists
if not exist .env (
    echo Warning: No .env file found. Running setup...
    python setup.py
    echo.
)

REM Check if dependencies are installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo Installing web dependencies...
    pip install flask -q --ignore-installed blinker
)

echo.
echo Starting JobApply Web UI...
echo    Open your browser to: http://localhost:5000
echo.

REM Run the Flask app
python app.py
