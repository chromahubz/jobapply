#!/bin/bash
# Quick launcher for JobApply

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found. Running setup..."
    python3 setup.py
    echo ""
    echo "Setup complete! Run './run.sh' again to start the app."
    exit 0
fi

# Check if dependencies are installed
if ! python3 -c "import groq" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt -q
fi

# Run the app
python3 main.py
