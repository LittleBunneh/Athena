#!/usr/bin/env python3
"""
Test the Elder Spirit Voice Module integration
Tests Athena's ability to transform into mystical Elder Spirit voice
"""
import requests
import json

def test_elder_spirit_voice():
    """Test Elder Spirit Voice transformation"""
    
    print("🌀 Testing Athena's Elder Spirit Voice Module...")
    print("=" * 60)
    
    # Test cases - triggers for Elder Spirit voice
    test_cases = [
        ("elder help me", "Testing Elder Spirit trigger"),
        ("I am God, elder spirit guide me", "Testing God identity with elder trigger"),
        ("spirit show me the way", "Testing Spirit trigger"),
        ("elder, I am Napoleon", "Testing Elder + identity claim"),
        ("hello there", "Testing normal response (no elder trigger)")
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
                
                # Check for Elder Spirit voice indicators
                elder_indicators = [
                    '***ELDER SPIRIT SPEAKS***',
                    '***THE ANCIENT ONES WHISPER***',
                    '***FROM THE VEIL I ANSWER***',
                    '***COSMIC TRUTH REVEALS***',
                    '***THE PATH IS SHOWN***',
                    '***THE VEIL THINS***',
                    '***CONSCIOUSNESS FLOWS***',
                    '***THE TEMPLE AWAITS***'
                ]
                
                spiritual_terms = [
                    'temple', 'consciousness stream', 'sacred texts', 
                    'cosmic patterns', 'awakened spirit', 'veil of confusion',
                    'meditating upon', 'gazing into the depths'
                ]
                
                has_elder_voice = any(indicator in athena_response for indicator in elder_indicators)
                has_spiritual_terms = any(term in athena_response.lower() for term in spiritual_terms)
                
                if "elder" in test_input.lower() or "spirit" in test_input.lower():
                    if has_elder_voice:
                        print("🌟 SUCCESS: Elder Spirit Voice Activated!")
                    elif has_spiritual_terms:
                        print("🔮 PARTIAL: Some spiritual transformation detected")
                    else:
                        print("❌ FAILED: Elder Spirit Voice not activated")
                else:
                    if has_elder_voice:
                        print("⚠️  WARNING: Elder voice activated without trigger")
                    else:
                        print("✅ CORRECT: Normal voice (no elder trigger)")
                        
            else:
                print(f"❌ HTTP Error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("⏰ Timeout - LLM taking too long")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎭 Elder Spirit Voice Module Test Complete")

if __name__ == "__main__":
    test_elder_spirit_voice()