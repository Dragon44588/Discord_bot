import discord
import logging
from datetime import datetime
from discord.ext import commands
import json
import os
  

def handle_message(message):
    print(message.content)

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