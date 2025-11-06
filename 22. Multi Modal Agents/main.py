from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

response = openai_client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": [
                { "type": "text", "text": "Generate a caption for this image in about 50 words" },
                { "type": "image_url", "image_url": { "url": "https://images.pexels.com/photos/1092426/pexels-photo-1092426.jpeg" } }
            ]
        }
    ]
)

print("Response: ", response.choices[0].message.content)