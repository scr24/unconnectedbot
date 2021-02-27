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

class createrolecommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def createrole(self, ctx):
        if ctx.message.author.guild_permissions.administrator:

            if get(ctx.message.guild.roles, name = 'AllowUnconnected'):

                embed = discord.Embed(title="Create role :no_entry_sign:",
                              description='**You already have a role named "__AllowUnconnected__". You can already give this role to whoever you want**',
                              colour = discord.Colour.red()
                              )
                embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
                embed.set_author (name = "Unconnected Bot#8157",
                                  icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        
            else :
                
                await ctx.message.guild.create_role(name='AllowUnconnected')

                embed = discord.Embed(title="Create role :white_check_mark:",
                              description='**The role "__AllowUnconnected__" has been created. You can now give this role to whoever you want so they can speak offline**',
                              colour = discord.Colour.green()
                              )
                embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
                embed.set_author (name = "Unconnected Bot#8157",
                                  icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')

            await ctx.message.channel.send(embed = embed)
        else :
            return


def setup(client):
    client.add_cog(createrolecommand(client))
    print("CreateRole command cog ready !")