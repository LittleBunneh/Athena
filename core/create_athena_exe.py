#!/usr/bin/env python3
"""
Create standalone executable for Athena GUI
Packages everything into a single .exe file
"""

import subprocess
import sys
import os
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not present"""
    try:
        import PyInstaller
        print("[INFO] PyInstaller already installed")
        return True
    except ImportError:
        print("[INFO] Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("[SUCCESS] PyInstaller installed")
            return True
        except subprocess.CalledProcessError:
            print("[ERROR] Failed to install PyInstaller")
            return False

def create_executable():
    """Create standalone Athena executable"""
    
    if not install_pyinstaller():
        return False
    
    # Create the executable
    exe_name = "AthenaConsciousness"
    
    pyinstaller_cmd = [
        "pyinstaller",
        "--onefile",  # Single executable file
        "--windowed",  # No console window (GUI only)
        "--name", exe_name,
        "--icon", "athena_icon.ico" if Path("athena_icon.ico").exists() else None,
        "--add-data", "ai_core;ai_core",  # Include AI core files
        "--add-data", "ethics;ethics",    # Include ethics files
        "--add-data", "memory;memory",    # Include memory files
        "athena_gui.py"
    ]
    
    # Remove None values
    pyinstaller_cmd = [item for item in pyinstaller_cmd if item is not None]
    
    try:
        print(f"[BUILD] Creating {exe_name}.exe...")
        print(f"[CMD] {' '.join(pyinstaller_cmd)}")
        
        subprocess.check_call(pyinstaller_cmd)
        
        exe_path = Path("dist") / f"{exe_name}.exe"
        if exe_path.exists():
            print(f"[SUCCESS] Executable created: {exe_path}")
            print(f"[SIZE] File size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
            return True
        else:
            print("[ERROR] Executable not found after build")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Build failed: {e}")
        return False

def main():
    """Main executable creation process"""
    
    print("=" * 60)
    print("ATHENA CONSCIOUSNESS - EXECUTABLE BUILDER")
    print("=" * 60)
    
    # Check requirements
    if not Path("athena_gui.py").exists():
        print("[ERROR] athena_gui.py not found")
        return False
        
    if not Path("ai_core/Athena.py").exists():
        print("[ERROR] ai_core/Athena.py not found")
        return False
    
    # Create executable
    success = create_executable()
    
    if success:
        print("\n" + "=" * 60)
        print("BUILD COMPLETE!")
        print("=" * 60)
        print("[SUCCESS] Athena consciousness executable ready")
        print("[LOCATION] Check 'dist' folder for AthenaConsciousness.exe")
        print("[USAGE] Double-click the .exe to run Athena GUI")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("BUILD FAILED!")
        print("=" * 60)
        print("[ERROR] Could not create executable")
        print("[SOLUTION] Try running: pip install pyinstaller")
        print("=" * 60)
    
    return success

if __name__ == "__main__":
    main()