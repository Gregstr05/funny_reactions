import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json

with open('config.json') as f:
    token = json.load(f)
type(token)
print(token.keys())

bot = commands.Bot(command_prefix='$')
 
@bot.event
async def on_ready():
    print ("I am alive")
 
 
@bot.event
async def on_message(message):
    print ("New message")
    emoji = bot.get_emoji("ehm:929430156907540491")
    #await message.add_reaction("👀")
    if(message.author.id == "577161725284057138"):
        print ("fugnuju skoro")
        await message.add_reaction(emoji)
    if '420' in message.content:
        print('funny guy')
        await message.add_reaction("🥬")
    if '69' in message.content:
        print('funny guy')
        await message.add_reaction("💦")
   
 
 
bot.run(token.get("token"))