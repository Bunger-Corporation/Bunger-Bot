import os
import dotenv
import discord
from helpers import presence
from commands import utils, encoding, encryption
import commands

# basic setup
dotenv.load_dotenv()
bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    await presence.on_ready(bot)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content[0] != ".":
        return
    
    await utils.on_message(bot, message)
    await encoding.on_message(bot, message)
    await encryption.on_message(bot, message)

bot.run(os.getenv("BOT_TOKEN"))