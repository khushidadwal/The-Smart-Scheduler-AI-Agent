import google.generativeai as genai

genai.configure(api_key="AIzaSyD58WWV8VD09fOLyVjNe2nrMUS93jR6O90")  # <-- replace with your real key

model = genai.GenerativeModel("models/gemini-pro")

response = model.generate_content("What's the capital of France?")
print(response.text)


