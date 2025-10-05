# DeepSeek integration for Athena
import requests

class DeepSeekClient:
    def __init__(self, api_url, api_key=None):
        self.api_url = api_url
        self.api_key = api_key

    def chat(self, prompt, system_prompt=None, history=None):
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload = {
            "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        if history and isinstance(history, list):
            payload["messages"] = history + payload["messages"]
        response = requests.post(self.api_url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        # Together API returns choices[0].message.content
        try:
            return data["choices"][0]["message"]["content"]
        except Exception:
            return str(data)
