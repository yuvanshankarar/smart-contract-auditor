from openai import OpenAI

from app.core.config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def generate_fix(vulnerability):

    response = client.chat.completions.create(
        model="google/gemma-3-4b-it",
        messages=[
            {
                "role": "user",
                "content": f"""
                Smart contract vulnerability:

                {vulnerability}

                Provide:

                1. Risk explanation
                2. Secure coding fix
                3. Solidity code example
                """
            }
        ]
    )

    return response.choices[0].message.content