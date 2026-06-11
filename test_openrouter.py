from openai import OpenAI
from app.core.config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

try:
    response = client.chat.completions.create(
        model="google/gemma-3-4b-it",
        messages=[
            {
                "role": "user",
                "content": "Explain reentrancy attacks in Solidity."
            }
        ]
    )

    print(response.choices[0].message.content)

except Exception as e:
    print("ERROR:")
    print(e)