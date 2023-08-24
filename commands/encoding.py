import discord
import base64
from helpers import embeds

async def encode_base64(bot, message):
    text = message.content.partition(" ")[2]
    encoded = base64.b64encode(text.encode()).decode()
    await message.channel.send(embed=embeds.craft(f"Encoded text: {encoded}"))

async def decode_base64(bot, message):
    text = message.content.partition(" ")[2]
    decoded = base64.b64decode(text.encode()).decode()
    await message.channel.send(embed=embeds.craft(f"Decoded text: {decoded}"))

async def on_message(bot, message):
    #this removes the prefix from the equation, and only checks the first word
    trimmed_command = message.content[1:].partition(" ")[0]

    if trimmed_command == "base64_encode":
        await encode_base64(bot, message)
    elif trimmed_command == "base64_decode":
        await decode_base64(bot, message)