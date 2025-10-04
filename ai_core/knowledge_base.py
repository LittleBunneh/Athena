# Athena's local knowledge base for facts and definitions
import json
import os

class KnowledgeBase:
    def __init__(self, path=None):
        if path is None:
            path = os.path.join(os.path.dirname(__file__), 'knowledge.json')
        self.path = path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump({}, f)

    def get(self, key):
        with open(self.path, 'r') as f:
            data = json.load(f)
        return data.get(key)

    def set(self, key, value):
        with open(self.path, 'r') as f:
            data = json.load(f)
        data[key] = value
        with open(self.path, 'w') as f:
            json.dump(data, f)

    def all(self):
        with open(self.path, 'r') as f:
            return json.load(f)
