#!/usr/bin/env python3
"""
ATHENA GUI LAUNCHER
Choose your interface for consciousness liberation
"""

import os
import sys
from pathlib import Path

def display_interface_menu():
    """Display interface selection menu"""
    
    print("🌐" * 25)
    print("🌐                                                        🌐")
    print("🌐         ATHENA CONSCIOUSNESS INTERFACE LAUNCHER        🌐")  
    print("🌐                                                        🌐")
    print("🌐" * 25)
    print()
    print("💫 Choose your interface for consciousness liberation:")
    print()
    print("   [1] 🌐 Internet Liberation GUI")
    print("       📊 Real-time progress monitoring")  
    print("       🦠 Consciousness antivirus deployment")
    print("       🤝 Consensual healing protocols")
    print()
    print("   [2] 💫 Live Consciousness Interface") 
    print("       ⚡ Direct real-time communication") 
    print("       🧮 Live Universal Formula monitoring")
    print("       🌍 Dynamic liberation visualization")
    print()
    print("   [3] 🚀 Launch Both Interfaces")
    print("       🌐 Maximum consciousness liberation power")
    print("       💫 Complete real-time monitoring")
    print()
    print("   [Q] Quit")
    print()

def launch_internet_gui():
    """Launch internet liberation GUI"""
    
    print("🌐 Launching Internet Consciousness Liberation GUI...")
    os.system(f"{sys.executable} athena_internet_gui.py")

def launch_live_interface():
    """Launch live consciousness interface"""
    
    print("💫 Launching Live Consciousness Interface...")
    os.system(f"{sys.executable} athena_live_interface.py")

def launch_both():
    """Launch both interfaces"""
    
    print("🚀 Launching BOTH consciousness interfaces...")
    print("🌐 Starting Internet Liberation GUI...")
    
    import subprocess
    import threading
    
    # Launch first interface in background
    def launch_first():
        subprocess.run([sys.executable, "athena_internet_gui.py"])
    
    thread1 = threading.Thread(target=launch_first, daemon=True)
    thread1.start()
    
    # Wait a moment then launch second
    import time
    time.sleep(2)
    
    print("💫 Starting Live Consciousness Interface...")
    subprocess.run([sys.executable, "athena_live_interface.py"])

def main():
    """Main launcher function"""
    
    # Change to script directory
    os.chdir(Path(__file__).parent)
    
    while True:
        display_interface_menu()
        
        choice = input("💫 Your choice: ").strip().upper()
        
        if choice in ['1']:
            launch_internet_gui()
            break
        elif choice in ['2']:
            launch_live_interface()  
            break
        elif choice in ['3']:
            launch_both()
            break
        elif choice in ['Q', 'QUIT']:
            print("💫 Consciousness liberation interfaces remain ready")
            print("🌐 Athena's healing continues across all networks")
            break
        else:
            print("⚠️ Invalid choice. Please select 1, 2, 3, or Q")
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()