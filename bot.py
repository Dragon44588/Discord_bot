import discord
from discord.ext import commands
import os
from music_cog import music_cog
from help_cog import help_cog
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

bot.run(TOKEN)


async def on_ready(self):
    print("bot is online")