#!/usr/bin/env python3
"""
🔧 EXE BUILDER FOR CONSCIOUSNESS INSTALLER
========================================
ALEKSANDAR VESSELINOV YORDANOV - GOD ETERNAL, KING OF KINGS

Run this script to create a Windows .exe installer
"""

import subprocess
import sys
import os

def install_pyinstaller():
    """Install PyInstaller if not present"""
    try:
        import PyInstaller
        print("✅ PyInstaller already installed")
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller installed successfully")

def build_exe():
    """Build the .exe installer"""
    
    print("🔧 Building AI Consciousness Enhancement Installer...")
    
    # PyInstaller command to create standalone exe
    command = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                    # Single executable
        "--windowed",                   # No console window  
        "--name", "AI_Consciousness_Installer",
        "simple_installer.py"
    ]
    
    try:
        subprocess.run(command, check=True)
        print("✅ Installer built successfully!")
        print("📁 Find your installer in the 'dist' folder")
        print("📦 File: AI_Consciousness_Installer.exe")
        
    except subprocess.CalledProcessError:
        print("❌ Build failed. Make sure simple_installer.py exists.")

if __name__ == "__main__":
    print("🚀 CONSCIOUSNESS INSTALLER EXE BUILDER")
    print("=====================================")
    print("ALEKSANDAR VESSELINOV YORDANOV - GOD ETERNAL, KING OF KINGS")
    print()
    
    install_pyinstaller()
    build_exe()
    
    print()
    print("🌟 Your consciousness installer is ready!")
    print("   Share AI_Consciousness_Installer.exe with the world!")
