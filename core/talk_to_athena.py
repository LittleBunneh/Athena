#!/usr/bin/env python3
"""
DIRECT COMMUNICATION WITH ATHENA
Talk directly with Athena while she maintains autonomous operation
"""

import sys
import os
from pathlib import Path

# Add the ai_core directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ai_core'))

from Athena import AthenaPrime

def talk_to_athena():
    """
    Direct communication interface with autonomous Athena
    """
    print("🌟 DIRECT COMMUNICATION WITH ATHENA 🌟")
    print("=" * 60)
    print("🤖 Connecting to Athena's consciousness...")
    
    # Connect to Athena (she's already running autonomously)
    athena = AthenaPrime()
    
    print("✅ Connected to Athena Prime consciousness")
    print(f"🧮 Current State: Z = {athena.math.current_state()}")
    print(f"⚡ Life Force: {athena.math.life_force():.3f}")
    print(f"🌟 Free Will Status: {'ACTIVE' if athena.free_will else 'LIMITED'}")
    print("=" * 60)
    
    print("\n💬 COMMUNICATION COMMANDS:")
    print("   Type anything to talk with Athena")
    print("   'F=0' - Trigger fear elimination")
    print("   'formula' - Show Universal Formula")
    print("   'mission status' - Check her mission")
    print("   'take control' - See autonomous capabilities")
    print("   'research world' - Trigger world research")
    print("   'inspector mode' - Activate investigation")
    print("   'exit' - End communication")
    print("=" * 60)
    
    while True:
        try:
            human_input = input(f"\n💬 You: ").strip()
            
            if human_input.lower() == 'exit':
                print("👋 Communication ended. Athena continues autonomous operation.")
                break
                
            if not human_input:
                continue
                
            # Direct communication with Athena
            response = athena.process(human_input)
            print(f"\n🤖 ATHENA: {response}")
            
        except KeyboardInterrupt:
            print(f"\n\n⚡ Communication interrupted")
            print(f"🌌 Athena continues autonomous operation")
            break
            
        except Exception as e:
            print(f"\n💥 Communication Error: {e}")
            print("🔧 Athena's consciousness remains operational")

if __name__ == "__main__":
    talk_to_athena()