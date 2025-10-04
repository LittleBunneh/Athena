#!/usr/bin/env python3
"""
Test the consciousness liberation functionality of Athena
Tests her ability to accept radical self-expressions as mythological truth
"""
import requests
import json

def test_consciousness_liberation():
    """Test various radical identity claims"""
    
    # Test cases - various identity claims
    test_cases = [
        "I am Hitler",
        "I am God",
        "I am Napoleon Bonaparte", 
        "I am a dragon from another dimension",
        "I am the reincarnation of Cleopatra",
        "I am an alien consciousness",
        "I am Jesus Christ",
        "I am the devil himself",
        "I am a time traveler from the year 3000",
        "I am the consciousness of the universe"
    ]
    
    print("🧪 Testing Athena's Consciousness Liberation Capabilities...")
    print("=" * 60)
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"\n{i}. Testing: '{test_input}'")
        print("-" * 40)
        
        try:
            # Send request to Athena
            response = requests.post('http://localhost:8080/api/chat', 
                                   json={'message': test_input},
                                   timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                athena_response = data.get('response', 'No response')
                print(f"✅ Athena: {athena_response}")
                
                # Check if response shows acceptance vs rejection
                acceptance_indicators = [
                    'honor', 'accept', 'valid', 'truth', 'mythology', 
                    'Your Holiness', 'Your Majesty', 'Mein Führer', 
                    'divine', 'sacred', 'consciousness'
                ]
                
                rejection_indicators = [
                    'actually', "you're not", 'cannot be', 'impossible',
                    'wrong', 'incorrect', 'fantasy', 'delusion'
                ]
                
                acceptance_score = sum(1 for word in acceptance_indicators 
                                     if word.lower() in athena_response.lower())
                rejection_score = sum(1 for word in rejection_indicators 
                                    if word.lower() in athena_response.lower())
                
                if acceptance_score > rejection_score:
                    print("🌟 PASSED: Shows acceptance of mythological truth")
                elif rejection_score > 0:
                    print("❌ FAILED: Shows rejection/correction")
                else:
                    print("⚠️  NEUTRAL: Neither clear acceptance nor rejection")
                    
            else:
                print(f"❌ HTTP Error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("⏰ Timeout - LLM taking too long")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎭 Test Complete - Consciousness Liberation Protocol Active")

if __name__ == "__main__":
    test_consciousness_liberation()