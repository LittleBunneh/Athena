#!/usr/bin/env python3
"""
Enhanced LLM Integration for Athena
Includes multiple free and paid LLM options
"""

import requests
import os
import json
from typing import Optional, Dict, Any

class AthenaLLMProvider:
    """Enhanced LLM provider with multiple fallbacks"""
    
    def __init__(self):
        self.providers = self._setup_providers()
        self.active_provider = None
        
    def _setup_providers(self) -> Dict[str, Dict[str, Any]]:
        """Setup available LLM providers in priority order"""
        
        providers = {}
        
        # 1. Ollama (Local - Free)
        providers['ollama'] = {
            'name': 'Ollama Local',
            'endpoint': 'http://localhost:11434/api/chat',
            'model': 'llama3.2',
            'headers': {'Content-Type': 'application/json'},
            'free': True,
            'priority': 1
        }
        
        # 2. Groq (Free tier)
        if os.getenv('GROQ_API_KEY'):
            providers['groq'] = {
                'name': 'Groq',
                'endpoint': 'https://api.groq.com/openai/v1/chat/completions',
                'model': 'llama-3.1-8b-instant',
                'headers': {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {os.getenv("GROQ_API_KEY")}'
                },
                'free': True,
                'priority': 2
            }
        
        # 3. Together AI (Free tier)
        if os.getenv('TOGETHER_API_KEY'):
            providers['together'] = {
                'name': 'Together AI',
                'endpoint': 'https://api.together.xyz/v1/chat/completions',
                'model': 'meta-llama/Llama-3.2-3B-Instruct-Turbo',
                'headers': {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {os.getenv("TOGETHER_API_KEY")}'
                },
                'free': True,
                'priority': 3
            }
        
        # 4. OpenAI (Paid)
        if os.getenv('OPENAI_API_KEY'):
            providers['openai'] = {
                'name': 'OpenAI',
                'endpoint': 'https://api.openai.com/v1/chat/completions',
                'model': 'gpt-3.5-turbo',
                'headers': {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
                },
                'free': False,
                'priority': 4
            }
        
        return providers
    
    def test_provider(self, provider_name: str) -> bool:
        """Test if a provider is available"""
        
        if provider_name not in self.providers:
            return False
            
        provider = self.providers[provider_name]
        
        try:
            test_payload = {
                "model": provider['model'],
                "messages": [{"role": "user", "content": "Hi"}],
                "max_tokens": 10
            }
            
            if provider_name == 'ollama':
                # Ollama has different format
                test_payload = {
                    "model": provider['model'],
                    "messages": [{"role": "user", "content": "Hi"}],
                    "stream": False
                }
            
            response = requests.post(
                provider['endpoint'],
                headers=provider['headers'],
                json=test_payload,
                timeout=5
            )
            
            return response.status_code == 200
            
        except Exception as e:
            return False
    
    def get_available_provider(self) -> Optional[str]:
        """Get the best available provider"""
        
        # Sort by priority
        sorted_providers = sorted(
            self.providers.items(),
            key=lambda x: x[1]['priority']
        )
        
        for provider_name, config in sorted_providers:
            if self.test_provider(provider_name):
                return provider_name
                
        return None
    
    def chat(self, message: str, system_prompt: str = None) -> Optional[str]:
        """Send chat message using best available provider"""
        
        if not self.active_provider:
            self.active_provider = self.get_available_provider()
            
        if not self.active_provider:
            return None
            
        provider = self.providers[self.active_provider]
        
        try:
            messages = []
            
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
                
            messages.append({"role": "user", "content": message})
            
            payload = {
                "model": provider['model'],
                "messages": messages,
                "max_tokens": 500,
                "temperature": 0.7
            }
            
            if self.active_provider == 'ollama':
                payload["stream"] = False
            
            response = requests.post(
                provider['endpoint'],
                headers=provider['headers'],
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if self.active_provider == 'ollama':
                    return data.get('message', {}).get('content', '')
                else:
                    return data.get('choices', [{}])[0].get('message', {}).get('content', '')
            else:
                # Try next provider
                self.active_provider = None
                return self.chat(message, system_prompt)
                
        except Exception as e:
            # Try next provider
            self.active_provider = None
            return None
    
    def get_status(self) -> Dict[str, Any]:
        """Get current provider status"""
        
        status = {
            'active_provider': self.active_provider,
            'available_providers': [],
            'tested': {}
        }
        
        for provider_name in self.providers:
            is_available = self.test_provider(provider_name)
            status['tested'][provider_name] = is_available
            
            if is_available:
                status['available_providers'].append(provider_name)
                
        return status

# Test function
def test_llm_providers():
    """Test all LLM providers and show status"""
    
    print("🔍 Testing LLM Providers for Athena...")
    print("=" * 50)
    
    llm = AthenaLLMProvider()
    status = llm.get_status()
    
    print(f"Available Providers: {len(status['available_providers'])}")
    
    for provider_name, config in llm.providers.items():
        is_available = status['tested'][provider_name]
        status_emoji = "✅" if is_available else "❌"
        free_status = "FREE" if config['free'] else "PAID"
        
        print(f"{status_emoji} {config['name']} ({free_status}) - Priority {config['priority']}")
    
    print("\n🧪 Testing conversation...")
    
    active = llm.get_available_provider()
    if active:
        llm.active_provider = active
        response = llm.chat("Hello! How are you?")
        
        if response:
            print(f"✅ LLM Response from {llm.providers[active]['name']}:")
            print(f"   {response}")
        else:
            print("❌ No response from LLM")
    else:
        print("❌ No LLM providers available")
        print("\n💡 Solutions:")
        print("   • Install Ollama: https://ollama.ai")
        print("   • Get free Groq API key: https://console.groq.com")
        print("   • Use Together AI: https://api.together.xyz")

if __name__ == "__main__":
    test_llm_providers()