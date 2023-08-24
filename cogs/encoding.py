import discord
import base64
from helpers import embeds
from discord.ext import commands

class encoding_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def base64_encode(self, ctx, text):
        encoded = base64.b64encode(text.encode()).decode()
        await ctx.send(embed=embeds.craft(f"Encoded text: {encoded}"))

    @commands.command()
    async def base64_decode(self, ctx, text):
        decoded = base64.b64decode(text.encode()).decode()
        await ctx.send(embed=embeds.craft(f"Decoded text: {decoded}"))