import requests
from bs4 import BeautifulSoup

class AthenaWebReader:
    """
    Simple web reader and parser for Athena.
    Usage:
        reader = AthenaWebReader()
        text = reader.read_url('https://example.com')
    """
    def read_url(self, url: str, max_length: int = 2000) -> str:
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'html.parser')
            # Extract visible text only
            for script in soup(["script", "style"]):
                script.decompose()
            text = ' '.join(soup.stripped_strings)
            # Truncate to max_length for LLM context
            return text[:max_length] + ("..." if len(text) > max_length else "")
        except Exception as e:
            return f"[WebReader error: {e}]"
