import discord
from helpers import embeds
from discord.ext import commands
import random

class fun_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_dice_roll = 0

    @commands.command()
    async def roll(self, ctx):
        number = random.randint(1, 6)

        #todo we can keep track of each user's rolls and treat snake eyes per user
        if number == 1 and self.last_dice_roll == 1:
            await ctx.send(embed=embeds.craft("You rolled a 1... snake eyes!"))
            #this is a goofy way to achieve this, we shouldn't be resetting it incase we want to check other last dice rolls
            self.last_dice_roll = 0
            return

        await ctx.send(embed=embeds.craft(f"You rolled a {number}"))
        self.last_dice_roll = number

    @commands.command()
    async def coinflip(self, ctx):
        sides = ["heads", "tails"]
        await ctx.send(embed=embeds.craft(f"You flipped a coin... it landed on {random.choice(sides)}!"))

    @commands.command()
    async def repeat(self, ctx, *, text):
        text = "".join(filter(str.isalnum, text))

        if text == "":
            await ctx.send(embed=embeds.craft("No text provided!", discord.Color.red()))
            return

        await ctx.send(text)