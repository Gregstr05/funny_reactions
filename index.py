import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import sys, datetime, time



with open('config.json') as f:
    token = json.load(f)
type(token)
print(token.keys())

with open('uwu.json') as i:
    uwu = json.load(i)
type(uwu)
print(uwu.keys())


bot = commands.Bot(command_prefix='$')
 
@bot.event
async def on_ready():
    print ("I am alive")
# Setting `Watching ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cringe memes"))
    print ("cringe memísky jsou super")

@bot.event
async def on_message(message):
    now = datetime.datetime.now()
    time = (now.strftime("%Y-%m-%d %H:%M:%S"))
    print (time, " New message")
    emoji = bot.get_emoji("ehm:929430156907540491")
    #await message.add_reaction("👀")
    if(message.author.id == "577161725284057138"):
        print (time, " fugnuju skoro")
        await message.add_reaction(emoji)
    if '420' in message.content:
        print(time, ' funny guy')
        await message.add_reaction("🥬")
    if '69' in message.content:
        print(time, ' funny guy')
        await message.add_reaction("💦")
    if 'agrLULE' in message.content:
        print(time, ' funny guy')
        await message.add_reaction("agrLULE:914561735040589864")
    if 'uwu' in message.content:
        print(time, ' Weeb')
        channel = bot.get_channel(message.channel.id)
        await message.add_reaction("Pepenoweeb:892154131228278846")
        #await channel.message.send("Pepenoweeb:892154131228278846")

    if 'CAN SOMEBODY TELL ME THE WAY OF ANDRISE' in message.content:
        channel = bot.get_channel(message.channel.id)
        print(time, 'proboha už zase!')
        await message.add_reaction(":emoji_50:913417410013458442")
        await channel.send("https://tenor.com/view/not-funny-didnt-laugh-not-funny-didnt-laugh-dancing-money-dance-gif-14496446")

    if 'https://tenor.com/view/bye-felicia-hi-hello-bye-gif-14084675' in message.content:
        print(time, ' Dobrou noc')
        await message.add_reaction("agrLove:917046239202246656")

    if message.author.name == 'MEE6':
        print(time, ' mee6 šmejd')
        #await message.add_reaction('monkaStab:886319312187555911')
        if 'GG' in message.content:
            await message.reply("https://tenor.com/view/gun-db-shotgun-gif-21597283")
        elif 'Student/ka' in message.content:
            await message.reply("https://tenor.com/view/gun-db-shotgun-gif-21597283")

   
 
 
bot.run(token.get("token"))