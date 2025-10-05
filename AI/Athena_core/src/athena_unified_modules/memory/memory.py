# Persistent, queryable memory (file-based demo).
import json
import os

class MemoryStore:
    def save_all(self, data):
        """Overwrite the memory file with the provided list of items."""
        with open(self.path, 'w') as f:
            json.dump(data, f)
    def __init__(self, path=None):
        if path is None:
            path = os.path.join(os.path.dirname(__file__), 'memory.json')
        self.path = path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump([], f)

    def save(self, item):
        data = self.load_all()
        data.append(item)
        with open(self.path, 'w') as f:
            json.dump(data, f)

    def load_all(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    def query(self, keyword):
        return [item for item in self.load_all() if keyword in str(item)]

if __name__ == "__main__":
    mem = MemoryStore()
    mem.save({"event": "test", "data": 123})
    print(mem.load_all())
    print(mem.query("test"))
