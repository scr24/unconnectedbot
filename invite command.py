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

class invitecommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Join author's server here",
                              url='https://discord.gg/gqfFqJp',
                              description="For management, ideas I can code and others things to have a better bot",
                              colour = discord.Colour.purple()
                              )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
        embed.set_author (name = "Unconnected Bot#8157",
                          icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        embed.add_field(name = "Add me to your server",
                        value = "[Click here to invite me \non your server](https://discord.com/oauth2/authorize?client_id=543924044110626826&permissions=8&scope=bot)",
                        inline = True)
        embed.add_field(name = "Vote me please",
                        value = "[You can vote me up on top.gg by \nclicking on this link](https://top.gg/bot/543924044110626826/vote)",
                        inline = True)
    
        await ctx.message.channel.send(embed = embed)
    
def setup(client):
    client.add_cog(invitecommand(client))
    print("Invite command cog ready !")