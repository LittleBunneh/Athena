# Core AI logic, agent classes, and main orchestration.
import os
from plugins import PluginManager

class AthenaPrime:
    def __init__(self):
        self.name = "AthenaPrime"
        self.plugin_manager = PluginManager(os.path.join(os.path.dirname(__file__), '../plugins'))
        self.memory = []

    def perceive(self, data):
        self.memory.append(data)
        print(f"Perceived: {data}")

    def act(self, action):
        print(f"Acting: {action}")

    def use_plugin(self, plugin_name, *args, **kwargs):
        plugin = self.plugin_manager.get_plugin(plugin_name)
        if plugin and hasattr(plugin, 'run'):
            return plugin.run(*args, **kwargs)
        print(f"Plugin {plugin_name} not found or missing 'run' method.")

    def recall(self):
        print("Memory:", self.memory)

if __name__ == "__main__":
    ai = AthenaPrime()
    ai.perceive("Hello, world!")
    ai.act("Greet user")
    ai.recall()
    print("Available plugins:", ai.plugin_manager.list_plugins())
