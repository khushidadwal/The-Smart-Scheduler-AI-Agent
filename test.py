import google.generativeai as genai

genai.configure(api_key="REMOVEDDEduTdCZA4l05jR7OfrLlmZrapx0orXC8")  # <-- replace with your real key

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("What's the capital of France?")
print(response.text)
