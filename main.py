import os
import time
import discord
import random
import string
from discord.ext import commands

bot = commands.Bot(command_prefix="garf")

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to discord!')

@bot.event
async def on_message(message):
    msg = message.content.split()
    chn = message.channel()
    
    if message.author == bot.user or msg[0] != "garf":
        return

    if msg[1] == "daily":
        localtime = time.gmtime()
        if len(str(localtime.tm_mday)) == 1:
            day = "0" + str(localtime.tm_mday)
        else:
            day = str(localtime.tm_mday)
        month = str(localtime.tm_mon)
        year = str(localtime.tm_year)
        curl = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2019/{}-{}-{}.gif".format(year,month,day)

        mbd = discord.Embed(image=curl)
        await chn.send(embed=mbd)
        
    elif msg[1] == "trivia":
        await chn.send("This feature isn't working yet, sorry for the inconvenience.")
    elif msg[1] == "help":
        await chn.send("This feature isn't working yet, sorry for the inconvenience.")
    elif msg[1] == "links":
        await chn.send("This feature isn't working yet, sorry for the inconvenience.")
    elif msg[1] == "prompt":
        await chn.send("This feature isn't working yet, sorry for the inconvenience.")
    elif msg[1] == "comic":
        await chn.send("This feature isn't working yet, sorry for the inconvenience.")
    
token = ""
bot.run(token)
        
