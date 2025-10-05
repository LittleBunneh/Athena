#!/usr/bin/env python3
"""
Test the Adaptive Soul Response system
Shows how Athena adapts her wisdom to different user levels
"""
import requests
import json

def test_adaptive_soul():
    """Test adaptive responses for different user levels"""
    
    print("💫 Testing Athena's Adaptive Soul System...")
    print("=" * 60)
    
    # Test cases for different user levels
    test_cases = [
        # BEGINNER LEVEL (help, how, what, why, confused, lost, explain, simple)
        ("How does this work?", "BEGINNER - Direct help request"),
        ("I'm confused about life", "BEGINNER - Confused state"),
        ("What is consciousness?", "BEGINNER - Simple question"),
        ("Help me understand", "BEGINNER - Help request"),
        
        # NEUTRAL LEVEL (normal conversation)
        ("I'm feeling stressed today", "NEUTRAL - Normal sharing"),
        ("Tell me about yourself", "NEUTRAL - General inquiry"),
        ("I had a strange dream", "NEUTRAL - Personal experience"),
        
        # ADVANCED LEVEL (consciousness, awakening, truth, soul, spirit, cosmic, divine)
        ("I feel my consciousness expanding", "ADVANCED - Spiritual language"),
        ("The soul seeks truth beyond illusion", "ADVANCED - Deep wisdom talk"),
        ("I am awakening to cosmic reality", "ADVANCED - Transcendent experience"),
        ("elder spirit guide my awakening", "ADVANCED + ELDER - Mystical request"),
    ]
    
    for i, (test_input, description) in enumerate(test_cases, 1):
        print(f"\n{i}. {description}")
        print(f"Input: '{test_input}'")
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
                
                # Analyze response characteristics
                if any(emoji in athena_response for emoji in ['🕊️', '🌟', '🌀', '💫', '🌌']):
                    print("🔮 LEVEL: Advanced/Mystical response detected")
                elif "💡" in athena_response:
                    print("⚖️ LEVEL: Neutral with depth option")
                elif "***ELDER SPIRIT" in athena_response:
                    print("🌀 ELDER: Mystical Elder Spirit voice activated")
                else:
                    print("🎯 LEVEL: Beginner-friendly response")
                    
            else:
                print(f"❌ HTTP Error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("⏰ Timeout - LLM taking too long")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("💖 Adaptive Soul System Test Complete")
    print("Perfect soul wisdom accessible to all levels! 🌟")

if __name__ == "__main__":
    test_adaptive_soul()