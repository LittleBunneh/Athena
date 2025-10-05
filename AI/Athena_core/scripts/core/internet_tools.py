# INTERNET ACCESS TOOLS FOR ATHENA
import requests
import json
from urllib.parse import urlencode

class InternetTools:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Athena-AI/1.0 (Sovereign Wisdom AI)'
        })
    
    def web_search(self, query, num_results=3):
        """More reliable web search with multiple approaches"""
        try:
            approaches = [
                self.duckduckgo_search,
                self.google_search_simulation,
                self.bing_search_simulation
            ]
            for approach in approaches:
                try:
                    result = approach(query, num_results)
                    if result and "No results" not in result:
                        return result
                except:
                    continue
            return f"🔍 Search for '{query}': Could not fetch results from available sources."
        except Exception as e:
            return f"🔍 Search error: {str(e)}"

    def duckduckgo_search(self, query, num_results):
        """DuckDuckGo search"""
        url = "https://api.duckduckgo.com/"
        params = {'q': query, 'format': 'json', 'no_html': 1}
        response = self.session.get(url, params=params, timeout=10)
        data = response.json()
        results = []
        if data.get('AbstractText'):
            results.append(f"📚 {data['AbstractText']}")
        if data.get('RelatedTopics'):
            for topic in data['RelatedTopics'][:num_results]:
                if 'Text' in topic:
                    results.append(f"• {topic['Text']}")
        return "\n".join(results) if results else "No results found."

    def google_search_simulation(self, query, num_results):
        # Placeholder for Google search simulation (could use SERP API or similar)
        return "No results found."

    def bing_search_simulation(self, query, num_results):
        # Placeholder for Bing search simulation (could use Bing API or similar)
        return "No results found."
    
    def fetch_url(self, url):
        """More robust URL fetching"""
        try:
            response = self.session.get(url, timeout=15)
            if response.status_code == 200:
                content = response.text
                title = self.extract_title(content)
                snippet = self.extract_snippet(content)
                return f"🌐 **{title}**\n{snippet}\n\n🔗 {url}"
            else:
                return f"❌ HTTP {response.status_code} for {url}"
        except requests.exceptions.Timeout:
            return f"⏰ Timeout accessing {url}"
        except Exception as e:
            return f"🔌 Cannot access {url}: {str(e)}"

    def extract_title(self, html):
        import re
        match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        return match.group(1).strip() if match else "No Title"

    def extract_snippet(self, html, length=300):
        # Simple snippet extraction: first N non-tag characters
        import re
        text = re.sub(r'<[^>]+>', '', html)
        snippet = text.strip().replace('\n', ' ').replace('\r', ' ')
        return snippet[:length] + ("..." if len(snippet) > length else "")
    
    def get_current_data(self, data_type):
        """Get current information"""
        apis = {
            'news': 'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_KEY',
            'weather': 'http://wttr.in/?format=3',
            'time': 'http://worldtimeapi.org/api/ip'
        }
        if data_type in apis:
            try:
                response = self.session.get(apis[data_type], timeout=10)
                return response.text
            except:
                return f"Could not fetch {data_type} data"
        else:
            return f"Unknown data type: {data_type}"

    def check_internet_connection(self):
        """Verify internet connectivity"""
        try:
            response = self.session.get("http://www.google.com", timeout=5)
            return "✅ Internet connection active"
        except:
            return "❌ No internet connection"
