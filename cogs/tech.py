import discord, datetime
from datetime import datetime
from discord.ext import commands
from typing import Literal, Optional
from discord.ext.commands import Greedy, Context 

class games(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    
    """
    @commands.command()
    async def roles(self, ctx):
        embed = discord.Embed(
            title= 'Guessing Game',
            description= 'Starts the guessing game',
            url='https://r.mtdv.me/AhT94Ndtpj',
            timestamp= datetime.now(),
            color= 1752220
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('✅')
        await msg.add_reaction('🆗')
        await msg.add_reaction('🎮')
    """
    
    @commands.command()
    @commands.has_role('Games')
    async def games(self, ctx):
        print('wowowowowo')

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def sync(
    self, ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")
        

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(games(bot))