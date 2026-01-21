#!/bin/bash
# Web UI launcher for JobApply

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found. Running setup..."
    python3 setup.py
    echo ""
fi

# Check if dependencies are installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing web dependencies..."
    pip install flask -q --ignore-installed blinker
fi

echo ""
echo "🌐 Starting JobApply Web UI..."
echo "   Open your browser to: http://localhost:5000"
echo ""

# Run the Flask app
python3 app.py
