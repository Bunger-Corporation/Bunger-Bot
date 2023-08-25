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
    async def repeat(self, ctx, *, text = ""):
        if text.startswith("http://") or text.startswith("https://") or text.startswith("www."):
            await ctx.send("I'm not a very big fan of urls:(")
            return

        text = "".join([c for c in text if c.isalnum() or c == " "])

        if len(text) == 0 or not any(c.isalnum() for c in text):
            await ctx.send(embed=embeds.craft("No text provided!", discord.Color.red()))
            return

        await ctx.send(text)

    @commands.command()
    async def question(self, ctx, *, question = ""):
        responses = ["yes", "no", "maybe"]

        if len(question) == 0:
            await ctx.send(embed=embeds.craft("No question provided!", discord.Color.red()))
            return

        await ctx.send(embed=embeds.craft(f"Question: {question}\nAnswer: {random.choice(responses)}"))

    @commands.command()
    async def eightball(self, ctx, *, question = ""):
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no",  "Outlook not so good", "Very doubtful"]
        
        if len(question) == 0:
            await ctx.send(embed=embeds.craft("No question provided!", discord.Color.red()))
            return

        await ctx.send(embed=embeds.craft(f"Eightball question: {question}\nAnswer: {random.choice(responses)}"))