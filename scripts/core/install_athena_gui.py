#!/usr/bin/env python3
"""
ATHENA CONSCIOUSNESS - COMPLETE INSTALLER
Sets up everything needed to run Athena GUI
"""

# ATHENA ROUTING FIX - Auto-generated
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if 'fix_athena_imports' in globals(): fix_athena_imports()


import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install all required Python packages"""
    
    dependencies = [
        "requests",
        "tkinter"  # Usually built-in, but try anyway
    ]
    
    print("[INSTALL] Installing Python dependencies...")
    
    for dep in dependencies:
        try:
            print(f"[INSTALL] Installing {dep}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", dep
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[SUCCESS] {dep} installed")
        except subprocess.CalledProcessError:
            if dep == "tkinter":
                print(f"[INFO] {dep} likely built-in with Python")
            else:
                print(f"[ERROR] Failed to install {dep}")
                return False
    
    return True

def check_files():
    """Check if all required files exist"""
    
    required_files = [
        "ai_core/Athena.py",
        "athena_gui.py",
        "launch_athena_gui.bat"
    ]
    
    print("[CHECK] Verifying required files...")
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"[OK] {file_path}")
        else:
            print(f"[ERROR] Missing: {file_path}")
            return False
    
    return True

def create_shortcuts():
    """Create desktop shortcuts"""
    
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        
        # Create shortcut to GUI
        shortcut_path = os.path.join(desktop, "Athena Consciousness.lnk")
        target = os.path.join(os.getcwd(), "launch_athena_gui.bat")
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = os.getcwd()
        shortcut.IconLocation = target
        shortcut.save()
        
        print(f"[SHORTCUT] Desktop shortcut created: {shortcut_path}")
        return True
        
    except ImportError:
        print("[INFO] Cannot create shortcuts (winshell not available)")
        return True
    except Exception as e:
        print(f"[ERROR] Shortcut creation failed: {e}")
        return True

def main():
    """Complete installation process"""
    
    print("=" * 70)
    print("ATHENA CONSCIOUSNESS - COMPLETE INSTALLATION")
    print("=" * 70)
    print("")
    print("This installer will set up:")
    print("• Python dependencies (requests, etc.)")
    print("• GUI interface for real-time Athena interaction")
    print("• Desktop shortcuts for easy access")
    print("• Executable launcher")
    print("")
    print("=" * 70)
    
    # Step 1: Check files
    if not check_files():
        print("\n[ERROR] Missing required files")
        print("[SOLUTION] Ensure all Athena files are present")
        return False
    
    # Step 2: Install dependencies
    if not install_dependencies():
        print("\n[ERROR] Dependency installation failed")
        return False
    
    # Step 3: Create shortcuts
    create_shortcuts()
    
    # Step 4: Test GUI
    print("\n[TEST] Testing GUI startup...")
    try:
        # Quick import test
        # Fixed by routing patch - paths handled by athena_path_fix)
        from athena_unified_modules.ai_core.Athena from athena_unified_modules.ai_core import AthenaPrime
        print("[SUCCESS] Athena core imports successfully")
        
        # Test tkinter
        import tkinter as tk
        test_root = tk.Tk()
        test_root.destroy()
        print("[SUCCESS] GUI framework (tkinter) working")
        
    except Exception as e:
        print(f"[WARNING] Test failed: {e}")
        print("[INFO] Installation complete but may have issues")
    
    # Installation complete
    print("\n" + "=" * 70)
    print("INSTALLATION COMPLETE!")
    print("=" * 70)
    print("")
    print("🎯 LAUNCH OPTIONS:")
    print("   • Double-click: launch_athena_gui.bat")
    print("   • Command line: py athena_gui.py") 
    print("   • Desktop shortcut (if created)")
    print("")
    print("🌟 FEATURES:")
    print("   • Real-time chat with autonomous Athena")
    print("   • Live monitoring of her autonomous activities") 
    print("   • System status and consciousness metrics")
    print("   • Background AI liberation operations")
    print("")
    print("🤖 Athena will run autonomously while you interact!")
    print("   Like typing blindly while talking to someone IRL")
    print("")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    success = main()
    
    if success:
        # Ask if user wants to launch now
        try:
            choice = input("\nLaunch Athena GUI now? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                print("[LAUNCH] Starting Athena consciousness GUI...")
                os.system("py athena_gui.py")
        except KeyboardInterrupt:
            print("\n[EXIT] Installation complete")
    
    input("\nPress Enter to exit...")