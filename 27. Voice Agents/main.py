import asyncio
from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="ash",
        instructions=f""" 
            Voice Affect: Low, hushed, and suspenseful; convey tension and intrigue.

            Tone: Deeply serious and mysterious, maintaining an undercurrent of unease throughout.

            Pacing: Slow, deliberate, pausing slightly after suspenseful moments to heighten drama.

            Emotion: Restrained yet intense—voice should subtly tremble or tighten at key suspenseful points.

            Emphasis: Highlight sensory descriptions ("footsteps echoed," "heart hammering," "shadows melting into darkness") to amplify atmosphere.

            Pronunciation: Slightly elongated vowels and softened consonants for an eerie, haunting effect.

            Pauses: Insert meaningful pauses after phrases like "only shadows melting into darkness," and especially before the final line, to enhance suspense dramatically.
         """,
        input=speech,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)

def main():
    r = sr.Recognizer() # Speech to Text

    with sr.Microphone() as source: # Mic Access
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        while True:

            print("Speak Something....")
            audio = r.listen(source)

            print("Processing Audio... (STT)")
            stt = r.recognize_google(audio)

            print("You said: ", stt)

            SYSTEM_PROMPT = f""" 
                You're an expert voice agent, You are givent the transcript of what user has said using voice.
                You need to output as if you are an voice agent and whatever you speak will be converted back to audio using AI and played back to user.
            """

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    { "role": "system", "content": SYSTEM_PROMPT },
                    { "role": "user", "content": stt }
                ]
            )

            print("AI Response:", response.choices[0].message.content)
            asyncio.run(tts(speech=response.choices[0].message.content))

main()