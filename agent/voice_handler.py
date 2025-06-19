import speech_recognition as sr
import pyttsx3
import threading
import queue
from typing import Optional

class VoiceHandler:
    def __init__(self, rate: int = 200, volume: float = 0.9):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Initialize TTS
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', rate)
        self.tts_engine.setProperty('volume', volume)
        
        # Voice selection (optional - try different voices)
        voices = self.tts_engine.getProperty('voices')
        if voices:
            # Try to use a more natural voice
            self.tts_engine.setProperty('voice', voices[0].id)
        
        # Speech queue for handling interruptions
        self.speech_queue = queue.Queue()
        self.is_speaking = False
        
        # Calibrate microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
    
    def speak(self, text: str, interrupt_current: bool = True):
        """Speak text with interruption handling"""
        if interrupt_current and self.is_speaking:
            self.tts_engine.stop()
        
        self.is_speaking = True
        print(f"🤖 Bot: {text}")
        
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        finally:
            self.is_speaking = False
    
    def listen(self, timeout: int = 10, phrase_time_limit: int = 15) -> Optional[str]:
        """Listen for speech with improved error handling"""
        print("Listening...")
        
        try:
            with self.microphone as source:
                # Listen for speech
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
            
            print("Processing speech...")
            text = self.recognizer.recognize_google(audio)
            print(f"👤 User: {text}")
            return text.lower().strip()
            
        except sr.WaitTimeoutError:
            print("⏰ No speech detected")
            return None
        except sr.UnknownValueError:
            print("❓ Could not understand audio")
            return "could not understand"
        except sr.RequestError as e:
            print(f"❌ Speech recognition error: {e}")
            return "recognition error"
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return "error"
    
    def test_voice(self):
        """Test voice setup"""
        self.speak("Voice test successful. I can hear you clearly.")
        
        response = self.listen(timeout=5)
        if response:
            self.speak(f"I heard you say: {response}")
        else:
            self.speak("I didn't hear anything, but the microphone is working.")