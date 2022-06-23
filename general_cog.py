import discord
from discord.ext import commands, tasks
import os
from datetime import datetime, timedelta
from music_cog import music_cog
from help_cog import help_cog
from general_cog import *
from dotenv import load_dotenv
import json
import logging


class general_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="test", help = "leaderboard lmao")
    async def leaderboard(self, ctx):
        filename = os.path.join(os.path.dirname(__file__), "data\\users.json")
        leaderboard = ""
        data = read_json(filename)
        x = 1
        for i in data:
            leaderboard += "{0}. {1} : {2} \n".format(x, i["Username"], x + 10)       
            x += 1
        
        await ctx.send(leaderboard)

async def handle_delete(message):
    if not message.author.bot:
        async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
            audit_time = entry.created_at + timedelta(hours=10)
            current_time = datetime.now()
            min_time = (audit_time - timedelta(seconds=40))
            max_time = (audit_time + timedelta(seconds=40))
            
            if current_time >= min_time and current_time <= max_time:
                await message.channel.send("{} just tried to delete {}s message which is '{}'\n\nand they're gay".format(entry.user.mention, message.author.display_name, message.content))
            else:
                await message.channel.send("this fucker deleted their own message which is '{}'\n\nand theyre gay".format(message.content))

        
async def handle_message(message):
    if not message.author.bot:
        if "what" in message.content.lower() and "time" in message.content.lower() :
            await message.channel.send("its morbin time")
        else:
            print("author: {}, message: {}".format(message.author, message.content))
        
async def save_user(message):
    if not message.author.bot:
        dump = {
            "Username" : message.author.name,
            "Nickname" : message.author.display_name,
            "Discriminator" : message.author.discriminator
        }
        exists = False
        index = 0
        x = 0
        filename = os.path.join(os.path.dirname(__file__), "data\\users.json")
        listobj = []
        if os.path.exists(filename) and not os.path.getsize(filename) == 0:
            listobj = read_json(filename)
        
        for i in listobj:
            if message.author.name == i["Username"] or message.author.discriminator == i["Discriminator"]:
                exists = True
                index = x
            x += 1
            
        if exists:
            print("user exists, updating")
            listobj[index] = dump
            save_json(listobj, filename)
        else:
            print("user doesnt exist, adding to file")
            listobj.append(dump)
            save_json(listobj, filename)
            
def save_json(contents, filename):
    with open(filename, "w") as f:
        json.dump(contents, f, indent=4)

def read_json(filename):
    with open(filename, "r") as f:
        listobj = json.load(f)
        return listobj
                

def info_log():
    infofile = os.path.join(os.path.dirname(__file__), "info/{}-info.log".format(datetime.date(datetime.now())))
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename=infofile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)    


def error_log():
    errorfile = os.path.join(os.path.dirname(__file__), "error/{}-error.log".format(datetime.date(datetime.now())))
    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename= errorfile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


def create_dir():
    directory = os.path.dirname(os.path.abspath(__file__))
    errorfile = os.path.join(directory, "error")
    infofile = os.path.join(directory, "info")
    if not os.path.exists(errorfile):
        print("creating errorfile at: {}".format(errorfile))
        os.makedirs(errorfile)
        
    if not os.path.exists(infofile):
        print("creating info file at: {}".format(infofile))
        os.makedirs(infofile)
        
    info_log()
    error_log()      