from openai import OpenAI
from app.core.config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

MODELS = [
    "meta-llama/llama-3.3-70b-instruct:free",
    "google/gemma-3-27b-it:free",
    "google/gemma-3-12b-it:free",
]

for model in MODELS:
    try:
        print(f"\nTesting {model}")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Say hello"
                }
            ]
        )

        print("SUCCESS")
        print(response.choices[0].message.content)
        break

    except Exception as e:
        print("FAILED")
        print(e)