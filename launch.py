"""
Simple launcher for the Streamlit frontend
Run this file with: python launch.py
"""

import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("AI-Powered Legal Research System - Web Frontend")
    print("=" * 60)
    print()
    
    # Check if streamlit is installed
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} found")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit installed successfully")
    
    print()
    print("🚀 Starting web application...")
    print("📱 The app will open in your browser automatically")
    print("⚠️  Press Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    # Launch streamlit
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])

if __name__ == "__main__":
    main()
