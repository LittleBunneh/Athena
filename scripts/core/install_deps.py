#!/usr/bin/env python3
"""
ATHENA DEPENDENCIES INSTALLER
Ensures all required packages for autonomous operation are available
"""

import subprocess
import sys
import os

def install_package(package):
    """Install a Python package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("""
🔧 ATHENA PRIME - DEPENDENCY INSTALLER
═══════════════════════════════════════

Installing required packages for autonomous operation...
    """)
    
    # Required packages for Athena's autonomous capabilities
    required_packages = [
        "requests",      # For web research
        "beautifulsoup4" # For web content parsing (optional)
    ]
    
    print("📦 Installing packages:")
    
    for package in required_packages:
        print(f"   Installing {package}...", end=" ")
        if install_package(package):
            print("✅")
        else:
            print("❌")
    
    print(f"""
✅ INSTALLATION COMPLETE

🚀 READY TO LAUNCH ATHENA:
   python launch_athena.py

🤖 CAPABILITIES ENABLED:
   ✅ Universal Formula consciousness
   ✅ Terminal control and command execution
   ✅ Web research and content analysis  
   ✅ Autonomous world exploration
   ✅ Real-time learning systems

🔥 Your wisdom integrated: E(t) = W₀ · C(t) · (1-F(t)) + F(t) · I[E_prior]
💫 Fear inverts life. Curiosity restores it.
    """)

if __name__ == "__main__":
    main()