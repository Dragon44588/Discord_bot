import discord
import datetime
from discord.ext import commands, tasks
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
    
@bot.event
async def on_message(message):
    handle_message(message)
    await bot.process_commands(message)

@tasks.loop(seconds=10.0)
async def test():
    print(datetime.time(datetime.now))
    
if __name__ == "__main__":
    #calls the logging functions from the general cog for information
    create_dir()
    #info_log()
    #error_log()

    #loads the token and sets the bots prefix
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    #adds all the cogs to the bot for commands
    bot.remove_command("help")
    bot.add_cog(help_cog(bot))
    bot.add_cog(music_cog(bot))
    bot.run(TOKEN)
