import discord
from discord.ext import commands
import aiohttp
import os

class planetinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(planetinfo(bot))
