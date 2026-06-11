import google.generativeai as genai
from app.core.config import GEMINI_KEY

genai.configure(api_key=GEMINI_KEY)

for model in genai.list_models():
    print(model.name)