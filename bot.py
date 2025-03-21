import discord
import responses
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"Error sending message: {e}")


def run_discord_bot():
    token = os.getenv("DISCORD_TOKEN")  # Load token from environment variables

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

        greeting_channel_id = 1180097384999551018
        try:
            greeting_channel = await client.fetch_channel(greeting_channel_id)
            await greeting_channel.send(
                "Salut, sunt Ion, asistentul tau virtual din cadrul Politehnicii. Cu ce te pot ajuta?")
        except Exception as e:
            print(f"Error fetching channel: {e}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_message = message.content.strip()
        if not user_message:
            return  # Prevent empty messages from causing errors

        username = str(message.author)
        channel = str(message.channel)
        print(f'{username} said: "{user_message}" ({channel})')

        if user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(token)
