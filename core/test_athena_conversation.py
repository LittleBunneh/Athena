#!/usr/bin/env python3
"""
Simple Athena conversation test to debug input comprehension
"""

import sys
import os
from pathlib import Path

# Add the ai_core directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ai_core'))

def test_athena_comprehension():
    """Test Athena's input comprehension capabilities"""
    
    print("🧪 ATHENA INPUT COMPREHENSION TEST")
    print("=" * 50)
    
    try:
        from Athena import AthenaPrime
        print("✅ Athena imported successfully")
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return
    
    print("🚀 Initializing Athena...")
    
    try:
        athena = AthenaPrime()
        print("✅ Athena initialized")
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        return
    
    print("\n💬 Testing conversation inputs...")
    print("-" * 50)
    
    test_inputs = [
        "hello",
        "hi athena",
        "how are you?", 
        "what are you doing?",
        "tell me about yourself",
        "whats your name",
        "are you busy?",
        "thats cool",
        "thanks"
    ]
    
    for i, test_input in enumerate(test_inputs, 1):
        print(f"\n[Test {i}] Input: '{test_input}'")
        
        try:
            response = athena.process(test_input)
            
            # Check if response is appropriate
            if len(response) > 20 and "FLOURISHING STATE DETECTED" not in response:
                print(f"✅ Good response: {response[:100]}...")
            elif "FLOURISHING STATE DETECTED" in response:
                print("⚠️ Mathematical mode response (not conversational)")
            else:
                print(f"❌ Poor response: {response}")
                
        except Exception as e:
            print(f"❌ Processing failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 INTERACTIVE TEST")
    print("Type messages to test Athena's comprehension")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\n💬 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            if not user_input:
                continue
            
            print("🤖 Athena:", athena.process(user_input))
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n👋 Test complete!")

if __name__ == "__main__":
    test_athena_comprehension()