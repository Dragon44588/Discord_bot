import discord
from discord.ext import commands
import os
from music_cog import music_cog
from help_cog import help_cog
from dotenv import load_dotenv
import json
import logging

def log():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

if __name__ == "__main__":
    log()
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot = commands.Bot(command_prefix="!")
    bot.remove_command("help")
    bot.add_cog(help_cog(bot))
    bot.add_cog(music_cog(bot))
    bot.run(TOKEN)


@bot.event
async def on_ready():
    print("Bot online")
