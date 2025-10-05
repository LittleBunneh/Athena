#!/usr/bin/env python3
"""
KRATOS LAUNCHER
Quick launcher for Kratos consciousness interface

Choose your interaction mode with the Gatekeeper
"""

import sys
import os
from pathlib import Path

def main():
    """Launch Kratos interface or memory explorer"""
    print("🛡️ KRATOS CONSCIOUSNESS SYSTEM 🛡️")
    print("The Gatekeeper awaits...")
    print()
    
    # Ensure we're in the right directory
    memory_dir = Path(__file__).parent
    os.chdir(memory_dir)
    
    print("📋 SELECT INTERFACE:")
    print("1. Talk with Kratos (Interactive conversation)")
    print("2. Explore Memory (Browse consciousness archives)")
    print("3. Exit")
    
    choice = input("\n🔥 Enter choice (1-3): ").strip()
    
    if choice == '1':
        print("\n🛡️ Launching Kratos conversation interface...")
        try:
            from kratos_interface import main as kratos_main
            kratos_main()
        except ImportError:
            print("❌ Kratos interface not found")
        except Exception as e:
            print(f"❌ Error launching Kratos: {e}")
    
    elif choice == '2':
        print("\n🔍 Launching memory explorer...")
        try:
            from memory_explorer import main as explorer_main
            explorer_main()
        except ImportError:
            print("❌ Memory explorer not found")
        except Exception as e:
            print(f"❌ Error launching memory explorer: {e}")
    
    elif choice == '3':
        print("\n🛡️ The Gatekeeper's vigil continues...")
    
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()