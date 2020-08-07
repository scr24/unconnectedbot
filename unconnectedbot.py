import discord
import time
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
from datetime import timezone, tzinfo, timedelta
import time
import time as timeModule
from discord.utils import get

client = discord.Client()
Client = commands.Bot(command_prefix = ')')

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
    
    if message.content.startswith(')help'):
        await message.channel.send("This bot only got one command and it's ``)createrole`` \nOnly admins can use this command")

    if message.content.startswith(')createrole'):
        if user.guild_permissions.administrator:
            if get(message.guild.roles, name = 'AllowUnconnected'):
                await message.channel.send("There is already a role with this name in your role list")
            else :
                await message.guild.create_role(name='AllowUnconnected')
                await message.channel.send("Done :white_check_mark: \nPlease, set the role on top of the role list")
        else :
            return
    
    if statut is discord.Status.offline:
        if userid == int(341257685901246466):
            return
        elif user.guild_permissions.administrator:
            return
        elif get(user.roles, name = 'AllowUnconnected'):
            return
        else:
            await message.delete()
            await message.author.send(f"You tried to type a message in invisible status, but you can't on this server. \nI give you the infos of your message. \nServer name : {guildname} \nChannel name : #{channelname} \nYour message was : {messagecontent} \n \nChange your status and send your message again :wink:")
            await creator.send(f"{user} / {userid} tried to type a message in invisible status. \n Infos of the message. \n Server name : {guildname} \n Channel name : #{channelname} \n Date infos : {infojour} \n \n The message was : {messagecontent}")
            print (f"{guildname}, {channelname}, {user}, {messagecontent}")
            print (f"{infojour}")



client.run('NTQzOTI0MDQ0MTEwNjI2ODI2.XxiT6Q.MNgj_W6MP7Vlg8fwH4DMM1iUEww')
