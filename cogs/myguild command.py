import discord
import asyncio
from discord.ext.commands import Bot, CommandNotFound, RoleNotFound
from discord.ext import commands, tasks
import datetime
from datetime import timezone, tzinfo, timedelta
import time
from discord.utils import get
import logging
import os
import sqlite3

db = sqlite3.connect("main.sqlite") # Ouverture de la base de données
cursor = db.cursor()

class myguildcommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def myguild(self, ctx):

        creator = self.client.get_user(341257685901246466)

        if ctx.message.author.guild_permissions.administrator:

            cursor.execute(f"SELECT timer, logchannel, bypassrole, streampass FROM main WHERE guild_id = {ctx.guild.id}")
            guildinfos = cursor.fetchall()

            if str(guildinfos) == "[]" :

                EmbedNone = discord.Embed(title = "Your server stats :",
                                        colour = discord.Color.purple())
                
                EmbedNone.add_field(name = "AntiGhosting Timer :",
                                    value = f"Not active",
                                    inline = True)
                EmbedNone.add_field(name = "LogChannel :",
                                    value = f"Not set",
                                    inline = True)
                EmbedNone.add_field(name = "Bypassrole list :",
                                    value = f"No Roles",
                                    inline = True)
                EmbedNone.add_field(name = "Streampass :",
                                    value = f"Deactivated",
                                    inline = True)
                EmbedNone.set_author (name = f"{ctx.guild.name}",
                                icon_url = f"{ctx.guild.banner_url}")
                EmbedNone.set_footer(icon_url = f"{creator.avatar_url}",
                                    text = f"{creator}")
                
                await ctx.send(embed = EmbedNone)
            
            else :

                EmbedMyGuild = discord.Embed(title = "Your server stats :",
                                            colour = discord.Color.purple())
                
                if guildinfos[0][0] == "0" or guildinfos[0][0] == "None" :
                    EmbedMyGuild.add_field(name = "AntiGhosting Timer :",
                                        value = f"Not active",
                                        inline = True)
                else :
                    EmbedMyGuild.add_field(name = "AntiGhosting Timer :",
                                        value = f"{guildinfos[0][0]} seconds",
                                        inline = True)
                
                if guildinfos[0][1] == None :
                    EmbedMyGuild.add_field(name = "LogChannel :",
                                        value = f"Not set",
                                        inline = True)
                else : 
                    EmbedMyGuild.add_field(name = "LogChannel :",
                                        value = f"<#{guildinfos[0][1]}>",
                                        inline = True)
                
                if guildinfos[0][2] == None :
                    EmbedMyGuild.add_field(name = "Bypassrole list :",
                                        value = f"No Roles",
                                        inline = True)
                else :
                    RoleList = ""
                    CustomBypassRoleList = (str(guildinfos[0][2]).split(","))

                    for x in range(len(list(CustomBypassRoleList))):
                        RoleList += f"<@&{CustomBypassRoleList[x]}>\n"

                    EmbedMyGuild.add_field(name = "Bypassrole list :",
                                        value = f"{RoleList}",
                                        inline = True)
                
                if guildinfos[0][3] == None :
                    EmbedMyGuild.add_field(name = "Streampass :",
                                        value = f"Deactivated",
                                        inline = True)
                else :
                    EmbedMyGuild.add_field(name = "Streampass :",
                                        value = f"Activated",
                                        inline = True)
                
                EmbedMyGuild.set_author (name = f"{ctx.guild.name}",
                                icon_url = f"{ctx.guild.banner_url}")
                EmbedMyGuild.set_footer(icon_url = f"{creator.avatar_url}",
                                    text = f"{creator}")

                await ctx.send(embed = EmbedMyGuild)
                


def setup(client):
    client.add_cog(myguildcommand(client))
    print("MyGuild command cog ready !")