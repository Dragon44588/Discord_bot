import discord 
from discord.ext import commands
import cogs
from music_cog import music_cog
from help_cog import help_cog
from general_cog import *
from models_cog import models_cog


TOKEN = "ODg0MzExNDQxMzA0MzQ2NjU1.G8ZHDg.6g70YQfE-oq570aOwNRCJjkDWqnqo5xX-xBHhs"

voiceChannel = ""


intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
game = discord.Game("With ChatGPT")

@bot.event
async def on_ready():
    print('logged in as {}'.format(bot.user))
    await bot.add_cog(cogs.AudioPlayer(bot))
    await bot.add_cog(general_cog(bot))
    await bot.add_cog(models_cog(bot))
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)
    