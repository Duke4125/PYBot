import discord
import os
import nekos
import asyncio

client = discord.Client()




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_ready():
  activity= discord.Game(name="UwU")
  await client.change_presence(status=discord.Status.idle, activity=activity)



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send('Welcome to the help command!')


client.run('ODMwOTAyNzI3Njc1NjA5MTQ4.YHNcdw._MFYRkBSxL0PR1JopOgg4sutaK4')
