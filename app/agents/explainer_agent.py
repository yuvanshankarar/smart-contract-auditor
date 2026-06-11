from openai import OpenAI
from app.core.config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def explain_vulnerability(vulnerability: str):

    response = client.chat.completions.create(
        model="google/gemma-3-4b-it",
        messages=[
            {
                "role": "user",
                "content": f"""
                Explain this smart contract vulnerability:

                {vulnerability}

                Include:
                - Explanation
                - Attack Scenario
                - Recommended Fix
                """
            }
        ]
    )

    return response.choices[0].message.content