import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API Keys
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REMOVED = os.getenv("REMOVED")

***REMOVED*** = os.getenv("***REMOVED***")

# Assistant Settings
DEFAULT_TIMEZONE = os.getenv("DEFAULT_TIMEZONE", "America/New_York")
TTS_RATE = int(os.getenv("TTS_RATE", 200))
TTS_VOLUME = float(os.getenv("TTS_VOLUME", 0.9))

