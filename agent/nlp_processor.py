# agent/nlp_processor.py
import google.generativeai as genai
from datetime import date
from datetime import datetime
import json
from dateutil import parser
import re

class NLPProcessor:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")


    def extract_meeting_info(self, user_input: str, context: dict) -> dict:
        system_prompt = """You are a smart assistant that extracts meeting info from natural language. 
    Return data in JSON with:
    - duration_minutes (int or null)
    - preferred_date (YYYY-MM-DD or null)
    - time_range (dict with start_hour and end_hour or null)
    - urgency (high, medium, low)
    - flexibility (flexible, somewhat_flexible, rigid)
    - meeting_type (brief, standard, long, all-day)
    """

        full_prompt = f"""{system_prompt}

    User input: "{user_input}"
    Today's date: {date.today().isoformat()}
    Context: {json.dumps(context, default=str)}
    """

        try:
            response = self.model.generate_content(full_prompt)
            # print("Gemini raw response:", response)

            # Safely extract content
            content = getattr(response, "text", None)
            if not content:
                try:
                    content = response.candidates[0].content.parts[0].text
                except Exception:
                    raise ValueError("Gemini returned no usable content.")

            # ✅ Clean markdown-wrapped JSON
            cleaned = re.sub(r"^```json|```$", "", content.strip(), flags=re.MULTILINE).strip()

            # Parse and return as dict
            return json.loads(cleaned)

        except Exception as e:
            print("Gemini error:", e)
            return {"error": "LLM failure"}




    def generate_response(self, state: str, context: dict, user_input: str) -> str:
        try:
            prompt = f"""You are a friendly scheduling assistant. 

State: {state}
Context: {json.dumps(context, default=str)}
User said: "{user_input}"

Reply helpfully and clearly based on the context.
"""
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print("Gemini response error:", e)
            return "Sorry, I had trouble generating a response."
        

    def extract_date(self, user_input: str):
        """Extracts a date from user input using fuzzy parsing"""
        try:
            return parser.parse(user_input, fuzzy=True).date()
        except:
            return None

