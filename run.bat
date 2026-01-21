@echo off
REM Quick launcher for JobApply (Windows)

REM Check if .env exists
if not exist .env (
    echo Warning: No .env file found. Running setup...
    python setup.py
    echo.
    echo Setup complete! Run 'run.bat' again to start the app.
    exit /b 0
)

REM Check if dependencies are installed
python -c "import groq" 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt -q
)

REM Run the app
python main.py
