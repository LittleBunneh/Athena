# Emotional intelligence and state management for Athena
class EmotionalArchitecture:
    def __init__(self):
        self.default_state = "Curiosity"
        self.fear_handling = "RecycleBin Protocol"

    def analyze_emotional_content(self, text):
        emotions = {
            'curiosity': ['why', 'how', 'what if', 'explain'],
            'confusion': ["confused", "don't understand", "help"],
            'urgency': ['now', 'quick', 'emergency', 'asap']
        }
        detected_emotions = {}
        for emotion, keywords in emotions.items():
            for keyword in keywords:
                if keyword in text.lower():
                    detected_emotions[emotion] = detected_emotions.get(emotion, 0) + 1
        return detected_emotions
