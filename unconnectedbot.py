import discord
import time
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
from datetime import timezone, tzinfo, timedelta
import time
import time as timeModule

client = discord.Client()
Client = commands.Bot(command_prefix = '.')

on = discord.Status.online
dnd = discord.Status.dnd
inv = discord.Status.offline


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Delete invisible message'),
                                 status=dnd)
    for member in client.get_all_members():
        print(member, member.status)


@client.event
async def on_message(message):
    
    guildname = message.guild.name
    
    channelname = message.channel.name
    
    user = message.author
    userid = message.author.id
    creator = client.get_user(341257685901246466)

    permissions = discord.Permissions()

    infojour = datetime.datetime.now()
    
    messagecontent = message.content
    
    statut = message.author.status
    
    if statut is discord.Status.offline:
        if userid == int(341257685901246466):
            return
        elif user.guild_permissions.administrator:
            return
        else:
            await message.delete()
            await message.author.send(f"You tried to type a message in invisible status, but you can't on this server. \nI give you the infos of your message. \nServer name : {guildname} \nChannel name : #{channelname} \nYour message was : {messagecontent} \n \nChange your status and send your message again :wink:")
            await creator.send(f"{user} / {userid} tried to type a message in invisible status. \n Infos of the message. \n Server name : {guildname} \n Channel name : #{channelname} \n Date infos : {infojour} \n \n The message was : {messagecontent}")
            print (f"{guildname}, {channelname}, {user}, {messagecontent}")
            print (f"{infojour}")



client.run('BCN8dfzVLzdC207eD99c5W0NMIgSafyo')
