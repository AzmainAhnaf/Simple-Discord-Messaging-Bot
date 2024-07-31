from typing import Final
import os
from dotenv import load_dotenv
import discord
from responses import get_response

# Loading Token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Setting bot and it's intents
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
client: discord.Client = discord.Client(intents=intents)

# Sending message functionality
async def send_message(message: discord.Message, user_message: str) -> None:
    if not user_message:
        print("Messages were empty because the intents weren't setuped probably")

    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except NotImplementedError:
        print("Needs to get implemented")

# Starting the bot
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")

# Handling the messages
@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"{channel} {username}: {user_message}")
    if(message.channel.id == 1267984639931318333):
        await send_message(message, user_message)

# Main Entry Point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()