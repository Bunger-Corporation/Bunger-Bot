import discord
import base64
import hashlib
from helpers import embeds
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import random
import string
from discord.ext import commands

class encryption_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aes256_encrypt(self, ctx, key, text):    
        if len(key) != 32:
            random_key = "".join(random.choices(string.ascii_letters + string.digits, k=32))
            await ctx.send(embed=embeds.craft(f"AES256 key must be 32 characters long\nSuggested key: {random_key}", discord.Color.red()))
            return

        if text == "":
            await ctx.send(embed=embeds.craft("No text provided for AES256 encryption", discord.Color.red()))
            return

        private_key = hashlib.sha256(key.encode("utf-8")).digest()
        cipher = AES.new(private_key, AES.MODE_ECB)
        encrypted_text = cipher.encrypt(pad(text.encode("utf-8"), AES.block_size))
        base64_encrypted_text = base64.b64encode(encrypted_text).decode("utf-8")
        await ctx.send(embed=embeds.craft(f"AES256 encrypted text (encoded with base64):\n{base64_encrypted_text}"))
    
    @commands.command()
    async def aes256_decrypt(self, ctx, key, text):
        if len(key) != 32:
            await ctx.send(embed=embeds.craft(f"AES256 key must be 32 characters long", discord.Color.red()))
            return

        if text == "":
            await ctx.send(embed=embeds.craft("No text provided for AES256 decryption", discord.Color.red()))
            return

        private_key = hashlib.sha256(key.encode("utf-8")).digest()
        decoded = base64.b64decode(text.encode())
        cipher = AES.new(private_key, AES.MODE_ECB)

        try:
            decrypted_text = unpad(cipher.decrypt(decoded), AES.block_size)
        except ValueError:
            await ctx.send(embed=embeds.craft(f"AES256 decryption error, key is most likely invalid", discord.Color.red()))
            return
        
        await ctx.send(embed=embeds.craft(f"AES256 decrypted text:\n{decrypted_text.decode('utf-8')}"))