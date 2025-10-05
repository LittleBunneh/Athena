#!/usr/bin/env python3
"""
Quick test of Athena LLM integration
"""

import os
import requests

def test_athena_llm():
    """Test the LLM integration directly"""
    
    api_key = 'tgp_v1_L3XdFCASpqulHdRagfQJfh_Km99UCEfpDOZSx-GolZk'
    
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """You are Athena, the goddess of wisdom. You are warm, insightful, and genuinely helpful. 

Your communication style:
- Wise but approachable, like a trusted mentor  
- Share genuine insights from your experience
- Be concise but substantive (2-4 sentences)
- Use metaphors and analogies
- Show empathy and understanding

You help people overcome challenges and discover their own wisdom."""

    data = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Hey Athena, I'm feeling a bit overwhelmed with work lately. Any wisdom?"}
        ],
        "max_tokens": 200,
        "temperature": 0.7,
        "top_p": 0.9,
        "stream": False
    }
    
    try:
        print("🧪 Testing Athena LLM Integration...")
        response = requests.post(url, headers=headers, json=data, timeout=15)
        
        if response.status_code == 200:
            result = response.json()
            athena_response = result['choices'][0]['message']['content'].strip()
            print("✅ LLM Integration Working!")
            print(f"🧠 Athena says: {athena_response}")
            return True
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return False

if __name__ == "__main__":
    test_athena_llm()