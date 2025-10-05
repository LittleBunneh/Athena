import pyttsx3
import speech_recognition as sr

class VoiceIOPlugin:
    name = "voice_io"
    description = "Text-to-speech and speech-to-text. Usage: use_plugin('voice_io', mode='tts', text='...') or mode='stt' for speech recognition."

    def run(self, mode, text=None):
        if mode == 'tts' and text:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            return "Spoken."
        elif mode == 'stt':
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
            try:
                return recognizer.recognize_google(audio)
            except Exception as e:
                return f"Speech recognition error: {e}"
        else:
            return "Invalid mode or missing text."
