from time import timezone
import discord
from discord.ext import commands, tasks
import os
from datetime import datetime, timedelta
from music_cog import music_cog
from help_cog import help_cog
from general_cog import *
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot online")
    

@bot.event    
async def on_message_delete(message):
    async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
        audit_time = entry.created_at + timedelta(hours=10)
        current_time = datetime.now()
        min_time = (audit_time - timedelta(seconds=40))
        max_time = (audit_time + timedelta(seconds=40))
        
        if current_time >= min_time and current_time <= max_time:
            await message.channel.send("{} just tried to delete {}s message which is '{}'\n\n and they're gay".format(entry.user.mention, message.author.display_name, message.content))
        else:
            await message.channel.send("this fucker deleted their own message which is '{}' and theyre gay".format(message.content))

        #await message.channel.send("this fucker just tried to delete '{}' \nhttps://tenor.com/view/i-saw-what-you-just-deleted-gif-22613011".format(message.content))
        
    
    
@bot.event
async def on_message(message):
    await save_user(message)
    await handle_message(message)
    await bot.process_commands(message)

    
if __name__ == "__main__":
    #loads the token and sets the bots prefix
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    #adds all the cogs to the bot for commands
    bot.remove_command("help")
    bot.add_cog(help_cog(bot))
    bot.add_cog(music_cog(bot))
    bot.add_cog(general_cog(bot))
    bot.run(TOKEN)
