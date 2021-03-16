import discord
from discord.ext import commands
import aiohttp
import os

class planetinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() ## getting info out of an NMS wiki
    async def info(self, ctx, *, query: str):
    	

def setup(bot):
    bot.add_cog(planetinfo(bot))