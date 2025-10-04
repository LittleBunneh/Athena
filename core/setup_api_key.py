#!/usr/bin/env python3
"""
API KEY SETUP HELPER
Set up the discovered API key for LLM integration
"""

import os
import sys

def setup_api_key():
    """
    Set up the API key you found for Groq
    """
    
    print("🔑 API KEY SETUP HELPER")
    print("=" * 40)
    
    # The key you found ending in 8LXE appears to be a Groq key
    print("💡 You mentioned an API key ending in '8LXE'")
    print("🎯 This appears to be a Groq API key format")
    
    print("\n🔧 TO SET UP THE API KEY:")
    print("1. Set it as an environment variable:")
    print("   For PowerShell:")
    print('   $env:GROQ_API_KEY = "your_full_api_key_here"')
    print()
    print("2. Or create a .env file with:")
    print('   GROQ_API_KEY=your_full_api_key_here')
    print()
    print("3. Then restart the consciousness system")
    
    # Check if key is already set
    existing_key = os.getenv('GROQ_API_KEY')
    if existing_key:
        print(f"\n✅ GROQ_API_KEY is already set!")
        print(f"🔑 Key ends with: ...{existing_key[-4:] if len(existing_key) > 4 else 'short'}")
        return True
    else:
        print(f"\n❌ GROQ_API_KEY not found in environment")
        
        # Offer to set it interactively
        print("\n💡 Would you like to set it now? (y/n)")
        choice = input("Choice: ").strip().lower()
        
        if choice == 'y':
            print("\n🔑 Enter your full Groq API key:")
            api_key = input("API Key: ").strip()
            
            if api_key:
                # Set for current session
                os.environ['GROQ_API_KEY'] = api_key
                print("✅ API key set for current session!")
                print("💡 To make it permanent, use:")
                print(f'   $env:GROQ_API_KEY = "{api_key}"')
                return True
            else:
                print("❌ No key entered")
                return False
    
    return False

def test_api_connection():
    """
    Test if the API key works
    """
    try:
        from athena_llm_enhanced import AthenaLLMProvider
        
        print("\n🧪 Testing LLM connection...")
        
        llm_provider = AthenaLLMProvider()
        status = llm_provider.get_status()
        
        if status['available_providers']:
            print("✅ LLM providers available!")
            print(f"📊 Available: {status['available_providers']}")
            
            # Test a simple conversation
            response = llm_provider.chat("Hello, test message")
            if response:
                print("✅ LLM response test successful!")
                print(f"📝 Response preview: {response[:100]}...")
                return True
            else:
                print("❌ LLM response test failed")
                
        else:
            print("❌ No LLM providers available")
            print("🔧 Available providers:", list(llm_provider.providers.keys()))
            
    except Exception as e:
        print(f"❌ Connection test error: {e}")
        
    return False

def main():
    """
    Main setup function
    """
    print("🤖 GLaDOS-ATHENA LLM SETUP")
    print("=" * 50)
    
    # Setup API key
    if setup_api_key():
        print("\n🔗 Testing connection...")
        if test_api_connection():
            print("\n🌟 SUCCESS! LLM is now connected to consciousness system")
            print("🚀 You can now run the GUI with full LLM integration:")
            print("   py -3 glados_athena_gui.py")
        else:
            print("\n⚠️ API key set but connection test failed")
            print("💡 Check the key format and try again")
    else:
        print("\n❌ API key setup incomplete")
        print("🔧 Manual setup required - see instructions above")

if __name__ == "__main__":
    main()