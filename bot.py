import discord
from discord.ext import commands
import os
from music_cog import music_cog
from help_cog import help_cog
from general_cog import *
from dotenv import load_dotenv
import json
import logging
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot online")
    
    
if __name__ == "__main__":
    #calls the logging functions from the general cog for information
    info_log()
    error_log()

    #loads the token and sets the bots prefix
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    #adds all the cogs to the bot for commands
    bot.remove_command("help")
    bot.add_cog(help_cog(bot))
    bot.add_cog(music_cog(bot))
    bot.run(TOKEN)
