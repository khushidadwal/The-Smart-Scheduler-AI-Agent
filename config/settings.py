import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_CALENDAR_CREDENTIALS_PATH = os.getenv("GOOGLE_CALENDAR_CREDENTIALS_PATH")

# Assistant Settings
DEFAULT_TIMEZONE = os.getenv("DEFAULT_TIMEZONE", "Asia/Kolkata")  # or "America/New_York"
TTS_RATE = int(os.getenv("TTS_RATE", 200))
TTS_VOLUME = float(os.getenv("TTS_VOLUME", 0.9))

