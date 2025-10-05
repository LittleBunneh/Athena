# Plugin/module system for dynamic skill expansion.
# Place plugin templates and loader logic here.

import importlib
import os

class PluginManager:
    """Dynamically loads and manages plugins from the plugins directory."""
    def __init__(self, plugin_dir=None):
        if plugin_dir is None:
            plugin_dir = os.path.dirname(__file__)
        self.plugin_dir = plugin_dir
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                plugin_name = filename[:-3]
                try:
                    module = importlib.import_module(f'plugins.{plugin_name}')
                    self.plugins[plugin_name] = module
                except Exception as e:
                    print(f"Failed to load plugin {plugin_name}: {e}")

    def get_plugin(self, name):
        return self.plugins.get(name)

    def list_plugins(self):
        return list(self.plugins.keys())

# Example usage:
if __name__ == "__main__":
    manager = PluginManager()
    print("Loaded plugins:", manager.list_plugins())
