from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    # api_key=os.environ.get("OPEN_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "user", "content": "Hey, I am Vishwajeet Khaple! Nice to meet you" }
    ]
)

print(response.choices[0].message.content)