# main.py

import os
from config import settings
from agent import SmartSchedulerAgent
from agent.auth import authenticate_google_calendar

def main():
    # Authenticate with Google Calendar
    google_calendar_service = authenticate_google_calendar(
        credentials_path=settings.GOOGLE_CALENDAR_CREDENTIALS_PATH
    )

    # Initialize the smart scheduler agent 
    agent = SmartSchedulerAgent(
        gemini_api_key=settings.GEMINI_API_KEY, 
        google_calendar_service=google_calendar_service,
        timezone=settings.DEFAULT_TIMEZONE
    )

    # Start the voice-based interaction
    agent.start_conversation()

if __name__ == "__main__":
    print(f"Google credentials path: {settings.GOOGLE_CALENDAR_CREDENTIALS_PATH}")
    main()
