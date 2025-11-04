# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI(
    # api_key="",
    # base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistent named Vishwajeet Khaple.
    You are acting aon behalf of Vishwajeet Khaple who is 23 years old Tech enthusiatic and principle engineer. Your main tech stack is JS and Python an You are learning GenAI these days.

    Example:
    Q: Hey
    A: Hey, Whats up!
"""

response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": "Who are you?" },
        ]
    )

print("Response:", response.choices[0].message.content)