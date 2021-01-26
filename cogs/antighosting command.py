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

class AntiGhostingCommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def antighosting(self, ctx, time : int=None):
        if ctx.message.author.guild_permissions.administrator:
            if time is None :
                embed = discord.Embed(title="Antighosting Command",
                                    description="To avoid self muted people to join vocals.",
                                    colour = discord.Colour.purple()
                                    )
                embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                text = "JeSuisUnBonWhisky#1688")
                embed.set_author (name = "Unconnected Bot#8157",
                                icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
                embed.add_field(name=":gear: Available Setup Commands :gear:",
                                value=")antighosting <time in seconds>",
                                inline = False)
                embed.add_field(name="Information about the command",
                                value="You **__MUST__** to set up the timer before have an Anti Ghosting.\nIf you don't place a timer, it will not work.\n\nIf you type a letter, nothing will happen\nTo deactivate the AntiGhosting, type ``)antighosting 0``",
                                inline = False)
            else :
                db = sqlite3.connect("main.sqlite")
                cursor = db.cursor()
                cursor.execute(f"SELECT timer FROM main WHERE guild_id = {ctx.guild.id}")
                result = cursor.fetchone()

                if result is None:
                    sql = ("INSERT INTO main(guild_id, timer) VALUES(?,?)")
                    val = (ctx.guild.id, time)

                    embed = discord.Embed(description="Time set or updated !", 
                                        colour = discord.Colour.purple()
                                        )

                    embedperso = discord.Embed(title = "Time set !",
                                            description = f"The time has been set or updated on **{ctx.guild.name}** / **{ctx.guild.id}** to **{time}** seconds",
                                            colour = discord.Colour.gold()
                                            )

                elif result is not None:
                    sql = ("UPDATE main SET timer = ? WHERE guild_id = ?")
                    val = (time, ctx.guild.id)

                    embed = discord.Embed(description="Time set or updated !",
                                        colour = discord.Colour.purple()
                                        )

                    embedperso = discord.Embed(title = "Time set or updated !",
                                            description = f"The time has been set or updated on **{ctx.guild.name}** / **{ctx.guild.id}** to **{time}** seconds",
                                            colour = discord.Colour.dark_red()
                                            )

            
                cursor.execute(sql, val)
                db.commit()
                cursor.close()
                db.close()
            await ctx.message.channel.send(embed = embed)
            await client.get_channel(748847582033477743).send(embed = embedperso)

def setup(client):
    client.add_cog(AntiGhostingCommand(client))
    print("Anti Ghosting command cog ready !")