

import google.generativeai as genai
from app.core.config import GEMINI_KEY

print("Loaded key:", GEMINI_KEY[:10], "...")

genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Say hello")

print(response.text)