import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import aiohttp

load_dotenv()

token = os.getenv('TOKEN')
client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('nms!'), case_insensitive=True)

@client.event
async def on_ready():
    print(f'{client.user} is online.')


extensions = ['Cogs.planetinfo']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


client.run(token)
