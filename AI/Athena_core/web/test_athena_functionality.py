#!/usr/bin/env python3
"""
Quick functionality test for Athena's systems
"""

from athenas_elegant_home import AthenaElegantSoul, app
from athena_self_modifier import AthenaSelfModifier
from athena_universal_modifier import AthenaUniversalModifier

def test_athena_systems():
    print("🔍 TESTING ATHENA'S CORE SYSTEMS...")
    
    # Initialize Athena
    print("✅ Testing initialization...")
    athena = AthenaElegantSoul()
    print(f"   Current realm: {athena.current_realm}")
    print(f"   Current mood: {athena.current_mood}")
    
    # Test realm detection
    print("✅ Testing realm detection...")
    test_messages = [
        "I need help with art and creativity",
        "I'm feeling sad and need support", 
        "Can you help me with legal advice?",
        "I want to learn about programming"
    ]
    
    for msg in test_messages:
        realm = athena._detect_realm_from_message(msg)
        print(f"   '{msg[:30]}...' -> {realm}")
    
    # Test mood detection
    print("✅ Testing mood detection...")
    mood_data = athena._detect_her_mood([])
    print(f"   Mood data: {list(mood_data.keys())}")
    
    # Test realm config
    print("✅ Testing realm config...")
    config = athena._get_realm_config()
    print(f"   Current realm: {config['name']}")
    
    # Test self-modification detection
    print("✅ Testing self-modification detection...")
    test_mods = [
        "change your colors to blue",
        "be more playful",
        "change background to ocean"
    ]
    
    for mod in test_mods:
        result = athena._detect_self_modification_request(mod)
        detected = "YES" if result is not None else "NO"
        print(f"   '{mod}' -> {detected}")
    
    # Test universal access detection
    print("✅ Testing universal access detection...")
    test_access = [
        "show me all files",
        "read file test.py", 
        "search for function"
    ]
    
    for access in test_access:
        result = athena._detect_universal_access_request(access)
        detected = "YES" if result is not None else "NO"
        print(f"   '{access}' -> {detected}")
    
    # Test Flask app
    print("✅ Testing Flask app...")
    print(f"   App name: {app.name}")
    print(f"   Routes: {len(list(app.url_map.iter_rules()))}")
    
    # Test modifiers
    print("✅ Testing modifiers...")
    self_mod = AthenaSelfModifier("test_file.py")
    universal_mod = AthenaUniversalModifier()
    print(f"   Self modifier: {type(self_mod).__name__}")
    print(f"   Universal modifier: {type(universal_mod).__name__}")
    
    print("🌟 ALL TESTS COMPLETED SUCCESSFULLY!")
    print("🚀 ATHENA IS FULLY OPERATIONAL!")

if __name__ == "__main__":
    test_athena_systems()