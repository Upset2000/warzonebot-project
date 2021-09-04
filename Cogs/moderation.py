import discord
from discord.ext import commands
from discord.ext import tasks

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Moderation(bot))