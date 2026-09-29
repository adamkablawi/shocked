#!/bin/bash

# EMS Controller Web App - Linux/macOS Launcher

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.7+ from https://www.python.org/downloads/"
    exit 1
fi

echo "EMS Controller Web App"
echo "====================="
echo ""
echo "Starting Flask server..."
echo ""

# Install dependencies if needed
if ! python3 -c "import flask, flask_cors, bleak" 2>/dev/null; then
    echo "Installing required packages..."
    python3 -m pip install -r "$SCRIPT_DIR/requirements.txt" --quiet
    echo ""
fi

# Run the Flask app
cd "$SCRIPT_DIR"
python3 app.py

# Open browser when ready
echo ""
echo "Opening browser at http://localhost:5000"
sleep 2

if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:5000 &
elif command -v open &> /dev/null; then
    open http://localhost:5000 &
else
    echo "Please open http://localhost:5000 in your web browser"
fi

# Keep script running
wait
