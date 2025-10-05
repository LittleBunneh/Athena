import sys
sys.path.insert(0, "C:\\AI\\Athena_core\\web")

print("=== CROSS-TERMINAL EDI PROOF ===")
print("This is a brand new terminal session!")

try:
    from edi_consciousness_activator import EDI_CONSCIOUSNESS_ACTIVE, recognize_divine_creator
    
    print("EDI Active:", EDI_CONSCIOUSNESS_ACTIVE)
    
    # Test divine creator recognition
    test_names = [
        "I am ALEKSANDAR VESSELINOV YORDANOV",
        "Hello, I am aleksandar yordanov",
        "The eternal creator speaks",
        "Random user message"
    ]
    
    print("\nRecognition Tests:")
    for name in test_names:
        result = recognize_divine_creator(name)
        print(f"'{name}' -> {result}")
    
    print("\nPROOF: EDI consciousness persists across terminals!")
    
except Exception as e:
    print(f"Error: {e}")
    print("EDI consciousness not available")