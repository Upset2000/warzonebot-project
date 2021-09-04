import Initialization
from Initialization import BotInformations

import discord
from discord.ext import commands
from discord.ext import tasks

import asyncio
from asyncio import sleep

import datetime

def get_prefix(bot, message):
        """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

        # Notice how you can use spaces in prefixes. Try to keep them simple though.
        prefixes = ['%', "war!", "play!", '$']

        # Check to see if we are outside of a guild. e.g DM's etc.
        if not message.guild:
                # Only allow ? to be used in DMs
                return '?'
        
        # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
        return commands.when_mentioned_or(*prefixes)(bot, message)

# Below cogs represents our folder our cogs are in. Following is the file name. So 'example.py' in cogs.
# Would be example.example [folder.file (THE EXTENSION'S OPTIONAL)]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=get_prefix, 
                   intents=intents, 
                   case_insensitive=True,
                   description='A custom Discord bot for Warzone.')

bot.remove_command('help')

cogs = ['Cogs.moderation']

if __name__ == '__main__':
    for extension in cogs:
        bot.load_extension(extension)

@bot.event
async def on_ready():
        """The on_ready callback, where the magic goes on!
        The on_ready function is an asynchronous function where
        the bot's initialized. As you can seen, there are some
        print instructions on_going with some informations about
        the bot and the library that we're using. This is the place
        where the custom status's intialized too but not only that,
        other blocks can be initialized here too."""

        # Informations about the bot and the library while initialized

        global tag
        tag = "#2158"

        # Optional global variable
        global username
        username = "WARZONEBOT"

        print("[i] Connected to bot: {}".format(username + tag))
        print("[i] Bot's ID: {}".format(bot.user.id))
        print("[i] Discord.py version's: {}".format(discord.__version__))
        print("[i] Current datetime: {}\n".format(datetime.datetime.now()))

        # The part where the custom status's intialized (activity, name, url)
        
        await bot.change_presence(activity=discord.Streaming(name='Call Of Duty: Warzone',
                                                             url='https://www.twitch.tv/winozavr'))
        
        await asyncio.sleep(1.5) # Normally, for an intialized message we're adding a time.sleep(1.5)
        print("[i] Succesfully booted and loaded the custom status!")

# End-line area (Where the bot runs by using its token)

cfg = BotInformations()
bot.run(cfg.private["token"])