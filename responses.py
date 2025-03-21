import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

def get_response(message: str) -> str:
    p_message = message.lower()
    messages.append({"role": "user", "content": p_message})

    try:
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        reply = "Sorry, I couldn't process that request."

    messages.append({"role": "assistant", "content": reply})
    return reply
