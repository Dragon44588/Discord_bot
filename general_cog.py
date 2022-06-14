import discord
import logging
from datetime import datetime
from discord.ext import commands
import json
import os

def create_dir():
    directory = os.path.dirname(__file__)
    errorfile = os.path.join(directory, "/error")
    infofile = os.path.join(directory, "/info")
    if not os.path.exists(errorfile):
        os.makedirs(errorfile)
    if not os.path.exists(infofile):
        os.makedirs(infofile)
        

def handle_message(message):
    print(message.content)

def info_log():
    file = '/home/dragon44588/Desktop/Discord_bot-main/{}-info.log'.format(datetime.date(datetime.now()))
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename=file, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)    


def error_log():
    file = '/home/dragon44588/Desktop/Discord_bot-main/error/{}-error.log'.format(datetime.date(datetime.now()))
    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename= file, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


