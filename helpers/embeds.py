import discord
import datetime 
import pytz

def craft(description, color = discord.Color.pink()):
    embed = discord.Embed(title="bunger bot", description=description, color=color, timestamp=datetime.datetime.now(pytz.timezone("US/Central")))
    return embed