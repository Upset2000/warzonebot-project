import Initialization
from Initalization import Initials

import discord
from discord.ext import commands
from discord.ext import tasks

import time
from time import sleep

import datetime

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='%', 
                   intents=intents, 
                   case_insensitive=True,
                   description='A custom Discord bot for Warzone.')

bot.remove_command('help')

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
        
        time.sleep(1.5) # Normally, for an intialized message we're adding a time.sleep(1.5)
        print("[i] Succesfully booted and loaded the custom status!")

cfg = Initials()
bot.run(cfg.token)