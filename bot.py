import discord
from discord.ext import commands, tasks
import os
from datetime import datetime, timedelta
from music_cog import music_cog
from general_cog import *
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print("Bot online")
    

@bot.event    
async def on_message_delete(message):
    await handle_delete(message)
        
    
    
@bot.event
async def on_message(message):
    await save_user(message)
    await handle_message(message)
    await bot.process_commands(message)

    
if __name__ == "__main__":
    #loads the token and sets the bots prefix
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    #adds all the cogs to the bot for commands
    #bot.add_cog(music_cog(bot))
    bot.add_cog(general_cog(bot))
    bot.run(TOKEN)
