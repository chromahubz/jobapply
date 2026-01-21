#!/bin/bash
# One-command installer for JobApply
# Usage: curl -sSL <url> | bash

set -e

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║          JobApply Installer v1.0                   ║"
echo "║     AI-Powered Job Application Assistant          ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found"
    echo "   Please install Python 3.10+ and try again"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Found Python $PYTHON_VERSION"

# Check pip
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "❌ pip is required but not found"
    exit 1
fi

echo "✓ Found pip"
echo ""

# Create directory if needed
if [ ! -d "jobapply" ]; then
    echo "📁 Creating directory..."
    mkdir -p jobapply
    cd jobapply
else
    echo "📁 Using existing directory"
    cd jobapply
fi

# Run setup
echo ""
echo "🚀 Running setup wizard..."
echo ""

python3 setup.py

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║             Installation Complete! 🎉              ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo ""
echo "  1. Get your FREE Groq API key:"
echo "     → https://console.groq.com/keys"
echo ""
echo "  2. Add it to .env file (if you haven't already)"
echo ""
echo "  3. Start using JobApply:"
echo "     → ./run_web.sh    (Web interface)"
echo "     → ./run.sh        (Command line)"
echo ""
echo "Happy job hunting! 🎯"
echo ""
