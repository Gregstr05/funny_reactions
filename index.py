import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import sys, datetime, time
import aiohttp
import typing



with open('config.json') as f:
    token = json.load(f)
type(token)
print(token.keys())

#with open('uwu.json') as i:
#    uwu = json.load(i)
#type(uwu)
#print(uwu.keys())


bot = commands.Bot(command_prefix='$')
 
@bot.event
async def on_ready():
    print ("I am alive")
# Setting `Watching ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cringe memes"))
    print ("cringe memísky jsou super")

@bot.command
async def foo(ctx, arg):
    await ctx.send(arg)

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
        print(time, ' proboha už zase!')
        channel = bot.get_channel(message.channel.id)
        await message.add_reaction(":emoji:939282373873389578")
        await channel.send("https://tenor.com/view/not-funny-didnt-laugh-not-funny-didnt-laugh-dancing-money-dance-gif-14496446")

    
    if '$cat' in message.content:
        print(time, ' Kočka ฅ^•ﻌ•^ฅ')
        channel = bot.get_channel(message.channel.id)
        #await channel.send('http://aws.random.cat/meow')
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as r:
                if r.status == 200:
                    js = await r.json()
                    await channel.send(js['file'])

    if '$dog' in message.content:
        print(time, ' Dogo ▼(´ᴥ`)▼')
        channel = bot.get_channel(message.channel.id)
        #await channel.send('http://aws.random.cat/meow')
        async with aiohttp.ClientSession() as session:
            async with session.get('https://random.dog/woof.json') as r:
                if r.status == 200:
                    js = await r.json()
                    await channel.send(js['url'])

    if '$ping' in message.content:
        print(time, ' ping')
        channel = bot.get_channel(message.channel.id)
        await channel.send('Pong! {0}'.format(round(bot.latency, 1)))

    if 'https://tenor.com/view/bye-felicia-hi-hello-bye-gif-14084675' in message.content:
        print(time, ' Dobrou noc')
        await message.add_reaction("agrLove:917046239202246656")

@bot.command
async def cat(ctx):
    channel = bot.get_channel(ctx.channel.id)
    print("kočka")
    async with aiohttp.ClientSession() as session:
      async with session.get('http://aws.random.cat/meow') as r:
        if r.status == 200:
            js = await r.json()
            await channel.send(js['file'])


"""
@bot.command()
async def cat(ctx):
    await ctx.send('http://aws.random.cat/meow')
    """

bot.run(token.get("token"))