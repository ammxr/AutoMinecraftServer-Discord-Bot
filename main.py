#Client Work: Minecraft Custom Server Maker 
from discord.ext import commands
import discord
import datetime
from urllib import parse, request
import re
import random
import asyncio
import subprocess
import time
import os
import zipfile
import shutil
import threading
import zlib

bot = commands.Bot(command_prefix='-', description="Making Servers")

bot.remove_command('help')
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Customs Server", url=""))
    print('Bot Ready')
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


#Server Versions
spx1710= ['spx1710']
spx189= ['spx189']
spx1122= ['spx1122']
spx1165= ['spx1165']
files = ['Server']

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('!server'):
        await message.channel.send('Please enter your desired RAM limit:')
        def is_correct(m):
            return m.author == message.author and m.content.isdigit()
        try:
            ramLimit = await bot.wait_for('message', check=is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry you took too long please try again')
        fin = open("startReference.bat", "rt")
        fout = open("Server/start.bat", "wt")
        for line in fin:
          fout.write(line.replace('Xmx4G', 'Xmx'+(ramLimit.content)+'G'))
        fin.close()
        fout.close()
        await message.channel.send('Successfully allocated '+(ramLimit.content)+'gb into batch file')

#Max Amt of People
        time.sleep(1)
        await message.channel.send('How many people would you like allowed on the server?:')
        def is_correct(m):
            return m.author == message.author and m.content.isdigit()
        try:
            pplLimit = await bot.wait_for('message', check=is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry you took too long please try again')
        fin = open("serverReference.properties", "rt")
        fout = open("Server/server.properties", "wt")
        for line in fin:
          fout.write(line.replace('max-players=20', 'max-players='+(pplLimit.content)))
        fin.close()
        fout.close()
        await message.channel.send('Max players set too '+(pplLimit.content))

#Server Desc
        time.sleep(1)
        await message.channel.send('What would you like the server description to be? (MOTD)')
        def is_correct(m):
            return m.author == message.author
        try:
            csMotd = await bot.wait_for('message', check=is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry you took too long please try again')
        fin = open("serverReference.properties", "rt")
        fout = open("Server/server.properties", "wt")
        for line in fin:
          fout.write(line.replace('motd=A Minecraft Server', 'motd= '+(csMotd.content)))
        fin.close()
        fout.close()
        await message.channel.send('MOTD set too '+(csMotd.content))

#Importing a Seed
        time.sleep(1)
        await message.channel.send('Would you like to add a Seed?')
        def is_correct(m):
            return m.author == message.author
        try:
            csSeed = await bot.wait_for('message', check=is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry you took too long please try again')
        fin = open("serverReference.properties", "rt")
        fout = open("Server/server.properties", "wt")
        for line in fin:
          fout.write(line.replace('level-seed=', 'level-seed='+(csSeed.content)))
        fin.close()
        fout.close()
        await message.channel.send('Seed set too '+(csSeed.content))

@bot.command(pass_context=True)
async def snd(ctx):
  channel = bot.get_channel(819309121861451777)
  shutil.make_archive("minecraft_server", "zip", "Server")
  my_files = [
    discord.File('minecraft_server.zip')
  ]
  await channel.send(files=my_files)
  await os.remove("minecraft_server.zip")

bot.run("TOKEN")