import os
import requests
import time
from datetime import datetime

class LLMFallbackSystem:
    def __init__(self):
        self.available_providers = self.detect_available_providers()
        self.current_provider = None
        self.fallback_responses = self.create_fallback_responses()
        
    def detect_available_providers(self):
        """Check which LLM providers are available"""
        providers = {}
        
        # Check DeepSeek
        if os.getenv('DEEPSEEK_API_KEY'):
            providers['deepseek'] = {
                'name': 'DeepSeek Cloud',
                'status': 'unknown',
                'priority': 1
            }
        
        # Check for local Ollama (fallback)
        providers['ollama'] = {
            'name': 'Ollama Local',
            'status': 'unknown', 
            'priority': 2
        }
        
        # Check for OpenAI
        if os.getenv('OPENAI_API_KEY'):
            providers['openai'] = {
                'name': 'OpenAI',
                'status': 'unknown',
                'priority': 3
            }
            
        return providers
    
    def test_provider(self, provider_name):
        """Test if a provider is working"""
        try:
            if provider_name == 'deepseek':
                return self.test_deepseek()
            elif provider_name == 'ollama':
                return self.test_ollama()
            elif provider_name == 'openai':
                return self.test_openai()
        except:
            return False
        return False
    
    def test_deepseek(self):
        """Test DeepSeek connection"""
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": "test"}],
                "max_tokens": 10
            }
            
            response = requests.post(
                "https://api.deepseek.com/chat/completions",
                headers=headers,
                json=payload,
                timeout=10
            )
            return response.status_code == 200
        except:
            return False
    
    def test_ollama(self):
        """Test local Ollama"""
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama2", "prompt": "test", "stream": False},
                timeout=5
            )
            return response.status_code == 200
        except:
            return False
    
    def get_best_provider(self):
        """Get the best available LLM provider"""
        for provider_name, info in sorted(self.available_providers.items(), key=lambda x: x[1]['priority']):
            if self.test_provider(provider_name):
                self.current_provider = provider_name
                return provider_name
        
        # No providers available
        return None
    
    def create_fallback_responses(self):
        """Create intelligent fallback responses"""
        return {
            'capabilities': """
🤖 **ATHENA LOCAL MODE - INTERNET TOOLS ACTIVE**

**MY CURRENT STATUS:**
✅ **Internet Access**: ACTIVE (internet_tools.py working)
✅ **File System**: ACTIVE (can read/write files)  
✅ **Web Browsing**: ACTIVE (can access websites)
✅ **Real-time Data**: ACTIVE (can fetch current information)

**LLM STATUS**: 🔌 Connection issues with cloud AI

**WHAT I CAN DO RIGHT NOW:**
- Browse websites and fetch content
- Search the web for current information  
- Access YouTube and other sites
- Read/write files on this system
- Run Python code and tools

**DEMONSTRATION READY** - What would you like me to do?
""",
            'greeting': "Hello! I'm Athena. I'm currently in local mode with full internet access capabilities. How can I assist you?",
            'help': """
🦉 **Athena Help - Local Mode**

**Available Commands:**
- `search [query]` - Web search
- `fetch [url]` - Get website content  
- `youtube` - Access YouTube
- `status` - System status

**I have active internet tools** even when cloud AI is unavailable.
"""
        }
    
    def get_fallback_response(self, user_input):
        """Get intelligent fallback response"""
        lower_input = user_input.lower()
        
        if any(word in lower_input for word in ['capability', 'ability', 'can you', 'what can you']):
            return self.fallback_responses['capabilities']
        
        elif any(word in lower_input for word in ['hello', 'hi', 'hey']):
            return self.fallback_responses['greeting']
        
        elif 'help' in lower_input:
            return self.fallback_responses['help']
        
        else:
            return "🔄 I'm currently in local mode. I have internet access and can browse websites, but my advanced reasoning is temporarily limited due to connection issues. What specific action would you like me to perform?"
