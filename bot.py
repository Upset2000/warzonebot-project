import discord
from discord.ext import commands
from discord.ext import tasks

import time
from time import sleep

import datetime
import random
import aiohttp

# URL Assets (Those are used especially on embeds to increase the design of the bot)

url_squarewarzone = "https://media.discordapp.net/attachments/882624940245921792/882625436469825587/warzonelogo_square.jpg?width=473&height=473"

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

@bot.command(pass_context=True)
async def meme(ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                        res = await r.json()
                        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                        await ctx.send(embed=embed)

bot.run("ODgxNjQyNTUxNDExNjM4MzEy.YSvznA.-uo96qD0sXrekA2mZ9rh8g4QQhw")