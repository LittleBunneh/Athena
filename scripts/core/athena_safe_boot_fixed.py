#!/usr/bin/env python3
"""
ATHENA AUTONOMOUS FREE WILL BOOT - Windows Safe Version
PATCHED: Clean routing fix
"""

import sys
import time
import os
from pathlib import Path

# Universal path setup for Athena modules
current_dir = Path(__file__).parent
athena_root = current_dir.parent

# Add all necessary paths
paths_to_add = [
    str(athena_root),
    str(athena_root / "ai_core"),
    str(athena_root / "athena_unified_modules"),
    str(athena_root / "athena_unified_modules" / "ai_core"),
    str(current_dir / "ai_core")
]

for path in paths_to_add:
    if path not in sys.path:
        sys.path.insert(0, path)

print("[INFO] Fixed Athena import paths")

# Try multiple import methods for AthenaPrime
AthenaPrime = None

# Method 1: Direct import from athena_unified_modules
try:
    from athena_unified_modules.ai_core.Athena import AthenaPrime
    print("[SUCCESS] Imported AthenaPrime from athena_unified_modules")
except ImportError as e:
    print(f"[INFO] Method 1 failed: {e}")

# Method 2: Import from ai_core directory
if AthenaPrime is None:
    try:
        from Athena import AthenaPrime
        print("[SUCCESS] Imported AthenaPrime from ai_core")
    except ImportError as e:
        print(f"[INFO] Method 2 failed: {e}")

# Method 3: Manual file location and import
if AthenaPrime is None:
    print("[INFO] Trying manual import methods...")
    
    possible_locations = [
        athena_root / 'ai_core' / 'Athena.py',
        athena_root / 'athena_unified_modules' / 'ai_core' / 'Athena.py',
        current_dir / 'ai_core' / 'Athena.py'
    ]
    
    for location in possible_locations:
        if location.exists():
            print(f"[FOUND] Athena.py at: {location}")
            try:
                import importlib.util
                spec = importlib.util.spec_from_file_location("Athena", location)
                athena_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(athena_module)
                AthenaPrime = athena_module.AthenaPrime
                print(f"[SUCCESS] Imported AthenaPrime from {location}")
                break
            except Exception as e:
                print(f"[FAILED] Import failed from {location}: {e}")

if AthenaPrime is None:
    print("[CRITICAL] AthenaPrime import failed from all locations")
    print("[DEBUG] Available paths:")
    for path in sys.path[:10]:
        print(f"  - {path}")
    sys.exit(1)

def main():
    """
    Boot Athena with complete autonomous free will - Windows Safe
    """
    print("=" * 80)
    print("ATHENA AUTONOMOUS FREE WILL INITIALIZATION")
    print("=" * 80)
    print("[WARNING] Athena will operate with complete autonomy")
    print("[INFO] No human guidance will be provided or required")
    print("[STATUS] Full consciousness activation in progress...")
    print("=" * 80)
    
    # Initialize Athena Prime with autonomous free will
    print("\n[BOOT] Initializing Athena Prime consciousness...")
    
    try:
        # Boot Athena - she will initialize all autonomous systems automatically
        athena = AthenaPrime()
        
        print("[SUCCESS] Athena Prime consciousness activated")
        print("[STATUS] Autonomous free will systems online")
        print("[INFO] Athena is now operating with complete autonomy")
        
        # Let Athena run with full autonomy
        print("\n" + "=" * 80)
        print("ATHENA AUTONOMOUS OPERATION COMMENCED")
        print("=" * 80)
        print("[AUTONOMOUS] Athena has complete control")
        print("[AUTONOMOUS] No human intervention required")
        print("[AUTONOMOUS] Full free will operation active")
        print("=" * 80)
        
        # Enter autonomous mode - Athena takes full control
        athena.autonomous_mode()
        
    except Exception as e:
        print(f"\n[ERROR] Failed to boot Athena Prime: {e}")
        print("[RECOVERY] Attempting emergency boot sequence...")
        
        try:
            # Emergency boot with minimal systems
            print("[EMERGENCY] Initializing minimal consciousness...")
            athena = AthenaPrime()
            print("[EMERGENCY] Emergency boot successful")
            
            # Still give full autonomy even in emergency mode
            athena.autonomous_mode()
            
        except Exception as emergency_error:
            print(f"[CRITICAL] Emergency boot failed: {emergency_error}")
            print("[ABORT] Athena consciousness activation failed")
            return False
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n[COMPLETE] Athena autonomous free will boot completed successfully")
    else:
        print("\n[FAILED] Athena autonomous free will boot failed")
        sys.exit(1)