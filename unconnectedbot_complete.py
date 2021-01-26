import discord
import time
import asyncio
from discord.ext.commands import Bot, CommandInvokeError, CommandNotFound, RoleNotFound
from discord.ext import commands, tasks
import datetime
from datetime import timezone, tzinfo, timedelta
import time as timeModule
from discord.utils import get
import dbl
import logging
import os
import sqlite3
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

intents = discord.Intents(members=True, guilds=True, voice_states=True, presences=True, messages=True, reactions=True)


TOKEN = 'NTQzOTI0MDQ0MTEwNjI2ODI2.XF9WvQ.5KjU6mELDWLZ_l3539vvGrB-SaY'

client = commands.Bot(command_prefix = ')', intents=intents)
client.remove_command('help')


##### ON READY EVENT #####

@client.event
async def on_ready():
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS main(
        guild_id TEXT,
        timer TEXT,
        logchannel TEXT,
        bypassrole TEXT
        )
    """)
    await client.change_presence(activity=discord.Streaming(name=")help (v2.6.3)",
                                                            url="https://www.twitch.tv/ps_racing_team/"))

    time.sleep(1)
    print("========== Unconnected Bot is online !! ==========")



##### GUILD JOIN AND REMOVE #####

@client.event
async def on_guild_join(guild):
    guildname = guild.name
    serveurlist = len(client.guilds)
    embed = discord.Embed(title = "Join a guild",
                        description = f"I join **{guildname}**. I am now on **{serveurlist}** servers",
                        colour = discord.Colour.green()
                        )
    await client.get_channel(748847582033477743).send(embed = embed)

@client.event
async def on_guild_remove(guild):
    guildname = guild.name
    serveurlist = len(client.guilds)
    embed = discord.Embed(title = "Left a guild",
                        description = f"I left **{guildname}**. I am now on **{serveurlist}** servers",
                        colour = discord.Colour.red()
                        )
    await client.get_channel(748847582033477743).send(embed = embed)



##### APPEL DES COGS #####

for filename in os.listdir(f"./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(TOKEN)
