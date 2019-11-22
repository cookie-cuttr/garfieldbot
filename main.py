import os
import time
import discord
import random
import string
import json
from discord.ext import commands

bot = commands.Bot(command_prefix="garf")

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to discord!')

@bot.event
async def on_message(message):
    msg = message.content.split()
    chn = message.channel
    
    if message.author == bot.user or msg == []:
        return
    if msg[0] == "garf":
        if msg[1] == "daily":
            localtime = time.gmtime()
            if len(str(localtime.tm_mday)) == 1:
                day = "0" + str(localtime.tm_mday)
            else:
                day = str(localtime.tm_mday)
            month = str(localtime.tm_mon)
            year = str(localtime.tm_year)
            curl = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2019/{}-{}-{}.gif".format(year,month,day)
            await chn.send(curl)

            print(("Sent today's comic to {}, {}").format(chn, message.guild))
            
        elif msg[1] == "trivia":
            with open('lst.json') as file:
                data = json.load(file)
                ran = random.choice(data['trivia'])['trivia']
                await chn.send(ran)

            print(("Sent trivia to {}, {}").format(chn, message.guild))
            
        elif msg[1] == "help":
            output = ""
            with open('lst.json') as file:
                data = json.load(file)
                for x in data['help']:
                    output += x['command']
                    output += "\n"
                await chn.send(output)
        elif msg[1] == "links":
            output = "```"
            with open('lst.json') as file:
                data = json.load(file)
                for x in data['links']:
                    output += x['title']
                    output += ": "
                    output += x['link']
                    output += "\n"
            output += "```"
            await chn.send(output)
        elif msg[1] == "prompt":
            await chn.send("This feature isn't working yet, sorry for the inconvenience.")
        elif msg[1] == "comic":
            await chn.send("This feature isn't working yet, sorry for the inconvenience.")
    
token = ""
bot.run(token)
        
