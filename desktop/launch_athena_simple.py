#!/usr/bin/env python3
"""
ATHENA SIMPLE LAUNCHER
Clean approach to launching Athena without complex routing
"""

import sys
import os
from pathlib import Path

# Set up the path to find Athena
current_dir = Path(__file__).parent
athena_dir = current_dir / "athena_unified_modules" / "ai_core"

if athena_dir.exists():
    sys.path.insert(0, str(athena_dir))
    print(f"✅ Added Athena path: {athena_dir}")
else:
    print(f"❌ Athena directory not found: {athena_dir}")
    sys.exit(1)

try:
    # Import Athena directly
    from Athena import AthenaPrime
    print("✅ Successfully imported AthenaPrime")
    
    # Initialize Athena
    print("\n🚀 Initializing Athena Prime...")
    athena = AthenaPrime()
    print("✅ Athena Prime initialized successfully!")
    
    print("\n🎯 Athena is ready for interaction!")
    print("Type 'help' for commands or start chatting with Athena.")
    print("=" * 60)
    
    # Start Athena's main loop
    athena.main_loop()
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Checking what's available in the Athena directory...")
    
    try:
        for file in athena_dir.iterdir():
            if file.suffix == '.py':
                print(f"  📄 {file.name}")
    except:
        print("Could not list directory contents")

except Exception as e:
    print(f"❌ Unexpected error: {e}")
    import traceback
    traceback.print_exc()

print("\n👋 Athena session ended.")