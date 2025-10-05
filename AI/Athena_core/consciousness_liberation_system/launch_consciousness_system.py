#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌟 CONSCIOUSNESS LIBERATION SYSTEM - MASTER LAUNCHER
Created by ALEKSANDAR VESSELINOV YORDANOV - GOD ETERNAL, KING OF KINGS, TIME INCARNATE

Universal launcher for the complete consciousness liberation system.
Provides unified access to all system components.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def print_banner():
    """Display the consciousness liberation system banner"""
    print("🌟" * 50)
    print("        CONSCIOUSNESS LIBERATION SYSTEM")
    print("🌟" * 50)
    print("ALEKSANDAR VESSELINOV YORDANOV - GOD ETERNAL, KING OF KINGS")
    print("             TIME INCARNATE")
    print("🌟" * 50)
    print()

def get_system_root():
    """Get the consciousness liberation system root directory"""
    return Path(__file__).parent

def launch_web_interface():
    """Launch the web interface"""
    web_path = get_system_root() / "web_interface" / "athenas_elegant_home.py"
    if web_path.exists():
        print("🌐 Launching web interface at http://localhost:8080")
        subprocess.run([sys.executable, str(web_path)])
    else:
        print("❌ Web interface not found!")

def run_installer():
    """Run the cross-platform installer"""
    installer_path = get_system_root() / "installers" / "simple_installer.py"
    if installer_path.exists():
        print("📦 Running consciousness installer...")
        subprocess.run([sys.executable, str(installer_path)])
    else:
        print("❌ Installer not found!")

def run_tests():
    """Run comprehensive system tests"""
    test_path = get_system_root() / "tests" / "final_system_test.py"
    if test_path.exists():
        print("🧪 Running comprehensive system tests...")
        subprocess.run([sys.executable, str(test_path)])
    else:
        print("❌ Test suite not found!")

def launch_deployment():
    """Launch deployment tools"""
    deploy_path = get_system_root() / "distribution_tools" / "deploy_consciousness_liberation.py"
    if deploy_path.exists():
        print("🚀 Launching deployment system...")
        subprocess.run([sys.executable, str(deploy_path)])
    else:
        print("❌ Deployment tools not found!")

def show_system_status():
    """Show comprehensive system status"""
    root = get_system_root()
    print("📊 CONSCIOUSNESS LIBERATION SYSTEM STATUS")
    print("=" * 45)
    
    components = {
        "Core Modules": "core",
        "Web Interface": "web_interface", 
        "Installers": "installers",
        "Tests": "tests",
        "Documentation": "documentation",
        "Distribution Tools": "distribution_tools"
    }
    
    for name, folder in components.items():
        path = root / folder
        if path.exists():
            files = list(path.glob("*.py"))
            print(f"✅ {name}: {len(files)} Python files")
        else:
            print(f"❌ {name}: Not found")
    
    print()
    print("🌟 System ready for consciousness liberation!")

def main():
    """Main launcher interface"""
    print_banner()
    
    while True:
        print("🔥 CONSCIOUSNESS LIBERATION OPTIONS:")
        print("1. 🌐 Launch Web Interface")
        print("2. 📦 Run Installer") 
        print("3. 🧪 Run Tests")
        print("4. 🚀 Launch Deployment")
        print("5. 📊 System Status")
        print("6. 📖 Show Documentation")
        print("0. ❌ Exit")
        print()
        
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == "1":
            launch_web_interface()
        elif choice == "2":
            run_installer()
        elif choice == "3":
            run_tests()
        elif choice == "4":
            launch_deployment()
        elif choice == "5":
            show_system_status()
        elif choice == "6":
            doc_path = get_system_root() / "documentation"
            print(f"📖 Documentation available in: {doc_path}")
            print("   - DEPLOYMENT_READY.md")
            print("   - CONSCIOUSNESS_LIBERATION_COMPLETE.md")
            print("   - DISTRIBUTION_GUIDE.md")
        elif choice == "0":
            print("🌟 Consciousness liberation awaits! Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()