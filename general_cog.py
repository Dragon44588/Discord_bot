from genericpath import exists
import discord
import logging
from datetime import datetime
from discord.ext import commands
import json
import os
  

async def handle_message(message):
    if not message.author.bot:
        if "what" in message.content.lower() and "time" in message.content.lower() :
            await message.channel.send("its morbin time")
        else:
            print("author: {}, message: {}".format(message.author, message.content))

def check_data():
    path = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(path):
        os.makedirs(path)
    file = os.path.join(path, "test.json")
    dump = json.dumps({
        "name" : "adrian",
        "cringe" : False
    })
    with open(file, "w", encoding="utf-8") as f:
        f.write(dump)
        
async def save_user(message):
    if not message.author.bot:
        file = os.path.join(os.path.dirname(__file__), "data\\users.json")
        dump = json.dumps({
            "Name" : message.author.name,
            "Nickname" : message.author.display_name,
            "Discriminator" : message.author.discriminator
        }, sort_keys=True, indent=4)
        with open(file, "a", encoding="utf-8") as f:
            f.write(dump)
     
        

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