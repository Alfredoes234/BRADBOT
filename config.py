import discord, logging, os
from discord.ext import commands, tasks
from itertools import cycle



TOKEN = os.environ["TOKEN"]
# This^ is needed for replit to keep token safe in secrets

## Prerequisites

PREFIX = '`'

## Setup stuff ~

discord.utils.setup_logging(level=logging.INFO, root=False)
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None )

## STATUS ##

status= cycle(['The Game Of Life', 'Doing Your Mother', 'Having Fun'])

@bot.event
async def on_ready():
    change_status.start()
    print(f'We have logged in as {bot.user}')

@tasks.loop(seconds= 60)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))