import os
import dotenv
import discord
from helpers import presence
from cogs import utils, encoding, encryption, fun
from discord.ext import commands

# basic setup
dotenv.load_dotenv()
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    await presence.on_ready(bot)
    await bot.add_cog(utils.utils_cog(bot))
    await bot.add_cog(encoding.encoding_cog(bot))
    await bot.add_cog(encryption.encryption_cog(bot))
    await bot.add_cog(fun.fun_cog(bot))
    print("bot ready")

bot.run(os.getenv("BOT_TOKEN"))