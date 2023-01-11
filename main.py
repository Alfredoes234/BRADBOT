import discord, asyncio, os
from discord.ext import commands
from config import *


#Role event
@bot.event
async def on_raw_reaction_add(payload):
  ourMessageId = 1049443469711659078

  if ourMessageId == payload.message_id:
    member = payload.member
    guild = member.guild

    emoji = payload.emoji.name
    if emoji == '✅':
      role = discord.utils.get(guild.roles, name='Basic permissions')
    elif emoji == '🆗':
      role = discord.utils.get(guild.roles, name='Roller')
    elif emoji == '🎮':
      role = discord.utils.get(guild.roles, name='Games')
    await member.add_roles(role)


# Role event
@bot.event
async def on_raw_reaction_remove(payload):
  ourMessageId = 1049443469711659078

  if ourMessageId == payload.message_id:
    guild = await (bot.fetch_guild(payload.guild_id))
    emoji = payload.emoji.name

    if emoji == '✅':
      role = discord.utils.get(guild.roles, name='Basic permissions')
    elif emoji == '🆗':
      role = discord.utils.get(guild.roles, name='Roller')
    elif emoji == '🎮':
      role = discord.utils.get(guild.roles, name='Games')
    member = await (guild.fetch_member(payload.user_id))
    if member is not None:
      await member.remove_roles(role)
    else:
      print('Member Not Found')


async def load():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
  await load()
  await bot.start(TOKEN)


asyncio.run(main())
