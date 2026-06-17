#!/bin/bash

# 🚀 Quick Start Script for Amit's RAG Chatbot
# This script helps you test everything locally before deploying

echo "========================================="
echo "🤖 Amit's RAG Chatbot - Quick Start"
echo "========================================="
echo ""

# Check if Groq API key is set
if [ -z "$GROQ_API_KEY" ]; then
    echo "⚠️  GROQ_API_KEY not found!"
    echo ""
    echo "Please set your Groq API key:"
    echo "  export GROQ_API_KEY='your_key_here'"
    echo ""
    echo "Get your free API key at: https://console.groq.com"
    echo ""
    exit 1
fi

echo "✅ Groq API key detected"
echo ""

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "⚠️  Please run this script from the backend directory:"
    echo "  cd amit-profile-complete/backend"
    echo "  ./quick-start.sh"
    echo ""
    exit 1
fi

# Check if dependencies are installed
echo "📦 Checking dependencies..."
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "⚠️  Dependencies not installed. Installing now..."
    pip install -r requirements.txt --break-system-packages
    echo ""
fi

echo "✅ Dependencies ready"
echo ""

# Start the API
echo "========================================="
echo "🚀 Starting RAG API..."
echo "========================================="
echo ""
echo "API will be available at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo ""
echo "Next steps:"
echo "1. Keep this terminal running"
echo "2. Open another terminal"
echo "3. Navigate to your profile folder"
echo "4. Open chat.html in your browser"
echo "5. Click the gear icon and set API URL to: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "========================================="
echo ""

# Start the server
python3 app.py