import discord
import math
from helpers import embeds
from discord.ext import commands

class utils_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rtt(self, ctx):
        embed_color = discord.Color.green()
        latency_ms_rounded = math.ceil(self.bot.latency * 1000)

        if latency_ms_rounded > 50:
            embed_color = discord.Color.orange()
        elif latency_ms_rounded > 100:
            embed_color = discord.Color.red()

        await ctx.send(embed=embeds.craft(f"RTT: {latency_ms_rounded}ms", embed_color))

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed=embeds.craft("A full list of commands can be found in the documentation:\nhttps://bunger-inc.gitbook.io/bunger-bot/"))