import requests

class WebSearchPlugin:
    name = "web_search"
    description = "Search the web and summarize results. Usage: use_plugin('web_search', query='<search terms>')"

    def run(self, query):
        # Simple DuckDuckGo search API (no API key required)
        url = f"https://duckduckgo.com/html/?q={query}"
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                # Just return the first 500 chars of the HTML for now
                return resp.text[:500] + ("..." if len(resp.text) > 500 else "")
            else:
                return f"Web search failed: {resp.status_code}"
        except Exception as e:
            return f"Web search error: {e}"
