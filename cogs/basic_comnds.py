import discord
from discord import app_commands
from discord.ext import commands


class Basic(commands.Cog, name= 'b'):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    super().__init__()  # this is now required in this context.
    
  @app_commands.command(name="ping")
  async def pings(self, interaction: discord.Interaction) -> None:
    """ Pings the bot. """
    await interaction.response.send_message(f'pong! {round(self.bot.latency * 1000)}ms')

  @app_commands.command(name="hello")
  async def hellos(self, interaction: discord.Interaction) -> None:
    """ Says hello. """
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')
  
  @app_commands.command(name="help")
  async def helps(self, interaction: discord.Interaction) -> None:
    """ Gives you options for help """
    await interaction.response.send_message('Helpers')

   
    
    
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Basic(bot))