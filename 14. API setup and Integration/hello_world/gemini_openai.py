from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    # api_key=os.environ.get("OPEN_API_KEY")
    api_key="AIzaSyC-FZWHRxbwWeHImjI8kI4aZ53hBujhQbg",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "user", "content": "Who are you ?" }
    ]
)

print(response.choices[0].message.content)