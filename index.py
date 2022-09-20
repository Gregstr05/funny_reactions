from importlib.resources import contents

import discord

from discord.ext import commands

from discord.ext.commands import Bot

import asyncio

import json

import sys, datetime, time

import aiohttp







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

    Channel = message.channel.name

    ServerName = message.guild.name

    Sender = message.author.name

    print (time, " New message" ,"  ",Sender,"  " , ServerName,"/#",Channel)

    emoji = bot.get_emoji("ehm:929430156907540491")

    #await message.add_reaction("👀")



    if(Channel == "info-dump-discord"):

        if(Sender != 'MEE6'):

            await message.delete()



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



    if 'https://tenor.com/view/scp-gif-14114975' in message.content:

        print(time , ' Thicc')

        await message.add_reaction(":gachiHyper:917046625912881233")



    if 'https://tenor.com/view/come-sit-bathroom-furry-bunny-seduce-gif-3419315' in message.content:

        print(time , ' Cum sit with me')

        await message.add_reaction(":dgihjtitled:944637259544690739")

        

    if 'https://tenor.com/view/capymelon-melon-watermelon-capy-capybara-gif-22716025' in message.content:

        print(time, ' melon')

        await message.author.send('Ok kamaráde retarde')



    if message.author.name == 'MEE6':

        print(time, ' mee6 šmejd')

        #await message.add_reaction('monkaStab:886319312187555911')

        if 'GG' in message.content:

            await message.reply("https://tenor.com/view/gun-db-shotgun-gif-21597283")

        elif 'Student/ka' in message.content:

            await message.reply("https://tenor.com/view/gun-db-shotgun-gif-21597283")



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



    if '$poll' in message.content:

        print(time, ' time to vote')

        await message.add_reaction("1️⃣")

        await message.add_reaction("0️⃣")



   

 

 

bot.run(token.get("token"))
