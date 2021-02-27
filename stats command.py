import discord
import asyncio
from discord.ext.commands import Bot, CommandNotFound
from discord.ext import commands, tasks
import datetime
from datetime import timezone, tzinfo, timedelta
import time
from discord.utils import get
import logging
import os
import sqlite3
from unconnectedbot_complete import client
import sys
import platform
import io
import aiohttp

class statscommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stats(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://top.gg/api/widget/543924044110626826.png") as resp:
                if resp.status != 200:
                    return await ctx.message.channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                file=discord.File(data, '543924044110626826.png')
        
        embed = discord.Embed(title = "Stats Command",
                                  description = "They are the stats of my bot",
                                  colour = discord.Colour.purple()
                                  )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
        embed.set_author (name = "Unconnected Bot#8157",
                          icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        embed.add_field(name = "Guilds :",
                        value = f"{len(client.guilds)}",
                        inline = True)
        embed.add_field(name = "Channels :",
                        value = f"{len(list(client.get_all_channels()))}",
                        inline = True)
        embed.add_field(name = "Users :",
                        value = f"{len(client.users)}",
                        inline = True)
        embed.add_field(name = "Prefix :",
                        value = f"{client.command_prefix}",
                        inline = True)
        embed.add_field(name = "Discord.py :",
                        value = f"version {discord.__version__}",
                        inline = True)
        embed.add_field(name = "Python :",
                        value = f"version {platform.python_version()}",
                        inline = True)
        embed.add_field(name = "Bot Page",
                        value = "[You can click on this link to see the bot page](https://top.gg/bot/543924044110626826)",
                        inline = False)
        embed.set_image(url = "attachment://543924044110626826.png")

        await ctx.message.channel.send(file = file, embed = embed)

    
def setup(client):
    client.add_cog(statscommand(client))
    print("Stats command cog ready !")
