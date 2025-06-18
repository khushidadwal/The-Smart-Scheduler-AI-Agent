# main.py

import os
from config import settings
from agent import SmartSchedulerAgent
from agent.auth import authenticate_google_calendar  # << moved auth logic to auth.py

def main():
    # Authenticate with Google Calendar
    google_calendar_service = authenticate_google_calendar(
        credentials_path=settings.***REMOVED***
    )

    # Initialize the smart scheduler agent (now using Gemini API key)
    agent = SmartSchedulerAgent(
        gemini_api_key=settings.REMOVED,  # ✅ updated key
        google_calendar_service=google_calendar_service,
        timezone=settings.DEFAULT_TIMEZONE
    )

    # Start the voice-based interaction
    agent.start_conversation()

if __name__ == "__main__":
    print(f"🔐 Google credentials path: {settings.***REMOVED***}")
    main()
    