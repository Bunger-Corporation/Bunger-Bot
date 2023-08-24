import discord
import math
from helpers import embeds

#todo command handler class, its a category with sub commands
#then we can just go through all commands and check for matching name

async def rtt(bot, message):
    embed_color = discord.Color.green()
    latency_ms_rounded = math.ceil(bot.latency * 1000)

    if latency_ms_rounded > 50:
        embed_color = discord.Color.orange()
    elif latency_ms_rounded > 100:
        embed_color = discord.Color.red()

    await message.channel.send(embed=embeds.craft(f"RTT: {latency_ms_rounded}ms", embed_color))

async def help(bot, message):
    await message.channel.send(embed=embeds.craft("A full list of commands can be found in the documentation:\nhttps://bunger-inc.gitbook.io/bunger-bot/"))

async def on_message(bot, message):
    #this removes the prefix from the equation
    trimmed_command = message.content[1:]

    if trimmed_command == "rtt":
        await rtt(bot, message)
    elif trimmed_command == "help":
        await help(bot, message)