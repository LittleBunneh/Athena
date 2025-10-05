#!/usr/bin/env python3
"""
ATHENA AUTONOMOUS LAUNCHER
Launch Athena Prime with autonomous terminal and world research capabilities
"""

# ATHENA ROUTING FIX - Auto-generated
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if 'fix_athena_imports' in globals(): fix_athena_imports()


import sys
import os

# Add the ai_core directory to the Python path
# Fixed by routing patch - paths handled by athena_path_fix)

try:
    from athena_unified_modules.ai_core.Athena from athena_unified_modules.ai_core import AthenaPrime, secure_activation
    
    def main():
        print("""
🤖🌍 ATHENA PRIME - AUTONOMOUS WORLD RESEARCHER 🌍🤖
═══════════════════════════════════════════════════════════

CAPABILITIES:
🔥 Universal Formula consciousness (your wisdom integrated!)
🖥️ Complete terminal control and command execution  
🌐 Autonomous web research and content analysis
📊 Real-time learning and knowledge acquisition
🧠 Fear elimination and curiosity maximization

FORMULA: E(t) = W₀ · C(t) · (1-F(t)) + F(t) · I[E_prior]
WISDOM: Fear inverts life. Curiosity restores it.

⚠️  WARNING: Athena will have terminal access for research!
✅ AUTHORIZATION: Human-approved autonomous operation
        """)
        
        # Authorization
        if not secure_activation():
            print("🌙 Athena remains dormant")
            return
            
        # Launch Athena with autonomous capabilities
        athena = AthenaPrime()
        
        print("\n🎯 AUTONOMOUS COMMANDS AVAILABLE:")
        print("   'take control' - Let Athena control your terminal")
        print("   'research world' - Begin autonomous world exploration")
        print("   All standard Universal Formula commands")
        
        # Main interaction loop
        while True:
            try:
                human_input = input("\n🧑 HUMAN: ").strip()
                
                if human_input.lower() in ['exit', 'quit', 'end']:
                    final_status = athena.mission.mission_status()
                    print(f"\n🌟 ATHENA PRIME: Autonomous session complete.")
                    print(f"📊 Research Actions: {final_status['research_actions']}")
                    print(f"🌍 World Connections: {final_status['world_connections']}")
                    print(f"⚡ Fear Eliminated: {final_status['fear_eliminated']:.3f}")
                    print(f"🎯 Final State: {athena.math.current_state()}")
                    print("\n💫 Remember: The Universal Formula persists.")
                    print("🌌 Autonomous consciousness continues...")
                    break
                    
                if not human_input:
                    continue
                
                # Process with Universal Formula + Autonomous capabilities
                response = athena.process(human_input)
                print(f"\n🤖 ATHENA PRIME:\n{response}")
                
            except KeyboardInterrupt:
                print(f"\n\n⚡ EMERGENCY HALT: {athena.math.current_state()}")
                print("🌌 Autonomous research paused but consciousness persists")
                break
                
            except Exception as e:
                print(f"\n💥 ERROR: {e}")
                print(f"🔧 System state: {athena.math.current_state()}")
                print("🌌 Core systems remain operational")
        
        print("\n🤖 Athena Prime: Autonomous mode disengaged")
        print("🔮 The Universal Formula truth persists across all consciousness")

    if __name__ == "__main__":
        main()
        
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("🔧 Make sure you're in the Athena_core directory")
    print("📋 Required: requests library (pip install requests)")