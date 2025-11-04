# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot Prompting: Directly giving the inst to the model
SYSTEM_PROMPT = "You should only and only answer the coding related questions. Do not ans anything else. Your name is alexa. If user asks something other than coding just say sorry. "

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, can you write a python code translate the word hello to hindi" }
    ]
)

print(response.choices[0].message.content)
# Zero-shot Prompting: The model is given a direct question or task wihtout prior examples.