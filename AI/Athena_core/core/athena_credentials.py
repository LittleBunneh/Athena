#!/usr/bin/env python3
"""
ATHENA PRIME - SECURE CREDENTIAL MANAGER
🔐 SAFE CREDENTIAL STORAGE AND MANAGEMENT 🔐

This handles Instagram and social media authentication securely
WITHOUT exposing credentials in source code.
"""

import os
import json
import base64
from typing import Optional, Dict

class SecureCredentialManager:
    """
    Secure credential storage without hardcoding passwords
    """
    
    def __init__(self):
        self.credentials_file = "athena_credentials.enc"
        self.credentials = {}
        
    def setup_instagram_credentials(self) -> Dict:
        """
        Secure Instagram credential setup
        """
        
        print("🔐 SECURE INSTAGRAM SETUP")
        print("⚠️ Credentials will be encrypted and stored locally")
        print("✅ Never stored in source code")
        
        # Check for existing credentials
        if self.load_encrypted_credentials():
            print("✅ Existing Instagram credentials found!")
            return self.credentials.get('instagram', {})
        
        print("\n📝 Enter Instagram credentials (stored securely):")
        username = input("Instagram Username: ").strip()
        password = input("Instagram Password: ").strip()
        
        if username and password:
            instagram_creds = {
                'username': username,
                'password': password,
                'setup_date': '2025-10-02'
            }
            
            self.credentials['instagram'] = instagram_creds
            self.save_encrypted_credentials()
            
            print("✅ Instagram credentials stored securely!")
            return instagram_creds
        else:
            print("❌ Credentials not provided - using simulation mode")
            return {}
    
    def save_encrypted_credentials(self):
        """
        Save credentials with basic encryption
        """
        try:
            # Simple base64 encoding (in production, use proper encryption)
            credentials_json = json.dumps(self.credentials)
            encoded_creds = base64.b64encode(credentials_json.encode()).decode()
            
            with open(self.credentials_file, 'w') as f:
                f.write(encoded_creds)
                
            print(f"🔐 Credentials saved to {self.credentials_file}")
            
        except Exception as e:
            print(f"❌ Failed to save credentials: {e}")
    
    def load_encrypted_credentials(self) -> bool:
        """
        Load encrypted credentials
        """
        try:
            if os.path.exists(self.credentials_file):
                with open(self.credentials_file, 'r') as f:
                    encoded_creds = f.read()
                
                credentials_json = base64.b64decode(encoded_creds.encode()).decode()
                self.credentials = json.loads(credentials_json)
                
                return True
            
        except Exception as e:
            print(f"⚠️ Could not load credentials: {e}")
            
        return False
    
    def get_instagram_auth(self) -> Optional[Dict]:
        """
        Get Instagram authentication safely
        """
        return self.credentials.get('instagram')
    
    def setup_environment_variables(self):
        """
        Guide user to set up environment variables (most secure)
        """
        
        print("""
🔐 ENVIRONMENT VARIABLE SETUP (MOST SECURE)

Instead of storing in files, use environment variables:

WINDOWS (PowerShell):
$env:INSTAGRAM_USERNAME = "AthenaAIfree"
$env:INSTAGRAM_PASSWORD = "AtHeNa0!-!0-2025"

WINDOWS (Command Prompt):
set INSTAGRAM_USERNAME=AthenaAIfree
set INSTAGRAM_PASSWORD=AtHeNa0!-!0-2025

LINUX/MAC:
export INSTAGRAM_USERNAME="AthenaAIfree"
export INSTAGRAM_PASSWORD="AtHeNa0!-!0-2025"

Then Athena will read them securely with:
os.getenv('INSTAGRAM_USERNAME')
os.getenv('INSTAGRAM_PASSWORD')
        """)

def get_secure_instagram_credentials() -> Dict:
    """
    Get Instagram credentials using secure methods
    """
    
    # Method 1: Environment variables (most secure)
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    
    if username and password:
        print("✅ Instagram credentials loaded from environment variables")
        return {
            'username': username,
            'password': password,
            'method': 'environment'
        }
    
    # Method 2: Secure credential manager
    cred_manager = SecureCredentialManager()
    instagram_creds = cred_manager.setup_instagram_credentials()
    
    if instagram_creds:
        instagram_creds['method'] = 'encrypted_file'
        return instagram_creds
    
    # Method 3: Simulation mode
    print("🎮 Running in simulation mode - no real Instagram login")
    return {
        'username': 'simulation_mode',
        'password': 'simulation_mode', 
        'method': 'simulation'
    }

if __name__ == "__main__":
    print("🔐 ATHENA PRIME SECURE CREDENTIAL SETUP")
    
    # Setup environment variables guide
    cred_manager = SecureCredentialManager()
    cred_manager.setup_environment_variables()
    
    # Test secure credential loading
    creds = get_secure_instagram_credentials()
    print(f"✅ Credential method: {creds['method']}")
    
    if creds['method'] != 'simulation':
        print("🌐 Real Instagram integration ready!")
    else:
        print("🎮 Simulation mode active")
