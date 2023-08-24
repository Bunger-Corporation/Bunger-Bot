import discord
import base64
import hashlib
from helpers import embeds
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import random
import string

async def encrypt_aes256(bot, message):
    partitioned_message = message.content.partition(" ")
    
    if len(partitioned_message) < 3:
        random_key = "".join(random.choices(string.ascii_letters + string.digits, k=32))
        await message.channel.send(embed=embeds.craft(f"No key provided for AES256 encryption\nSuggested key: {random_key}", discord.Color.red()))
        return

    sub_partition = partitioned_message[2].partition(" ")
    key = sub_partition[0]

    if len(sub_partition) < 3:
        await message.channel.send(embed=embeds.craft("No text provided for AES256 encryption", discord.Color.red()))
        return

    text = sub_partition[2]

    if len(key) != 32:
        random_key = "".join(random.choices(string.ascii_letters + string.digits, k=32))
        await message.channel.send(embed=embeds.craft(f"AES256 key must be 32 characters long\nSuggested key: {random_key}", discord.Color.red()))
        return

    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    cipher = AES.new(private_key, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(text.encode("utf-8"), AES.block_size))
    base64_encrypted_text = base64.b64encode(encrypted_text).decode("utf-8")
    await message.channel.send(embed=embeds.craft(f"AES256 encrypted text (encoded with base64):\n{base64_encrypted_text}"))

async def decrypt_aes256(bot, message):
    partitioned_message = message.content.partition(" ")
    
    if len(partitioned_message) < 3:
        await message.channel.send(embed=embeds.craft(f"No key provided for AES256 decryption", discord.Color.red()))
        return

    sub_partition = partitioned_message[2].partition(" ")
    key = sub_partition[0]

    if len(sub_partition) < 3:
        await message.channel.send(embed=embeds.craft("No encrypted text provided for AES256 decryption", discord.Color.red()))
        return

    encrypted_data = sub_partition[2]

    if len(key) != 32:
        await message.channel.send(embed=embeds.craft(f"AES256 key must be 32 characters long", discord.Color.red()))
        return

    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    decoded = base64.b64decode(encrypted_data.encode())
    cipher = AES.new(private_key, AES.MODE_ECB)

    try:
        decrypted_text = unpad(cipher.decrypt(decoded), AES.block_size)
    except ValueError:
        await message.channel.send(embed=embeds.craft(f"AES256 decryption error, key is most likely invalid", discord.Color.red()))
        return
    
    await message.channel.send(embed=embeds.craft(f"AES256 decrypted text:\n{decrypted_text.decode("utf-8")}"))


async def on_message(bot, message):
    #this removes the prefix from the equation, and only checks the first word
    trimmed_command = message.content[1:].partition(" ")[0]

    if trimmed_command == "aes256_encrypt":
        await encrypt_aes256(bot, message)
    elif trimmed_command == "aes256_decrypt":
        await decrypt_aes256(bot, message)