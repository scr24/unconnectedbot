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

db = sqlite3.connect("main.sqlite") # Ouverture de la base de données
cursor = db.cursor()

class streampasscommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def streampass(self, ctx, OnOff : str = None):

        creator = self.client.get_user(341257685901246466)

        if ctx.message.author.guild_permissions.administrator:

            if OnOff is None or OnOff not in ["on", "off"] :

                cursor.execute(f"SELECT streampass FROM main WHERE guild_id = {ctx.guild.id}")
                StreamPassValue = cursor.fetchone()

                EmbedPresentation = discord.Embed(title = "Streampass command",
                                                description = "Streampass command is used if you want a user can display his screen self muted and in offline status",
                                                colour = discord.Colour.purple())
                EmbedPresentation.add_field(name = ")streampass on",
                                            value = "This command will activate the streampass command on your server.\nAll users will be able to share their screen self muted and offline",
                                            inline = False)
                EmbedPresentation.add_field(name = ")streampass off",
                                            value = "This command will deactivate the streampass command on your server.\nAll users (except admins) will must to have their mic activated and online/idle/dnd status",
                                            inline = False)
                EmbedPresentation.set_footer(icon_url = f"{creator.avatar_url}",
                                            text = f"{creator}")

                if (str(StreamPassValue) == "None") or (str(StreamPassValue) == "(None,)") :

                    EmbedPresentation.add_field(name = "Streampass Status :",
                                                value = "__Deactivated__",
                                                inline = False)
                
                else :

                    EmbedPresentation.add_field(name = "Streampass Status :",
                                                value = "__Activated__",
                                                inline = False)
                
                await ctx.send(embed = EmbedPresentation)
            
            elif OnOff == "on" :

                cursor.execute(f"SELECT streampass FROM main WHERE guild_id = {ctx.guild.id}")
                StreamPassValue = cursor.fetchone()

                StreamPassActivate = 1

                EmbedActivated = discord.Embed(description = "Streampass has been activated on your server !",
                                                colour = discord.Colour.green())

                EmbedAlreadyActivated = discord.Embed(description = "Streampass was already activated on your server !",
                                                    colour = discord.Colour.red())

                if str(StreamPassValue) == "None":

                    sql = ("INSERT INTO main(guild_id, streampass) VALUES(?,?)")
                    val = (ctx.guild.id, StreamPassActivate)
                    cursor.execute(sql, val)
                    db.commit()

                    await ctx.send(embed = EmbedActivated)
                
                elif str(StreamPassValue) == "(None,)":

                    sql = ("UPDATE main SET streampass = ? WHERE guild_id = ?")
                    val = (StreamPassActivate, ctx.guild.id)
                    cursor.execute(sql, val)
                    db.commit()

                    await ctx.send(embed = EmbedActivated)

                elif str(StreamPassValue[0]) == "1":
                    
                    await ctx.send(embed = EmbedAlreadyActivated)
                 
            elif OnOff == "off" :
                
                cursor.execute(f"SELECT streampass FROM main WHERE guild_id = {ctx.guild.id}")
                StreamPassValue = cursor.fetchone()

                EmbedAlreadyDeactivated = discord.Embed(description = "Streampass was already deactivated on your server !",
                                                        colour = discord.Colour.red())

                EmbedDeactivated = discord.Embed(description = "Streampass has been deactivated on your server !",
                                                colour = discord.Colour.green())

                if (str(StreamPassValue) == "None") or (str(StreamPassValue) == "(None,)") :

                    await ctx.send(embed = EmbedAlreadyDeactivated)
                
                else :

                    sql = (f"UPDATE main SET streampass = NULL WHERE guild_id = {ctx.guild.id}")
                    cursor.execute(sql)
                    db.commit()

                    await ctx.send(embed = EmbedDeactivated)


        


def setup(client):
    client.add_cog(streampasscommand(client))
    print("StreamPass command cog ready !")