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

class logcommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def logs(self, ctx, logchannel : discord.TextChannel=None):
        if ctx.message.author.guild_permissions.administrator:

            if logchannel is None :
                embed = discord.Embed(title="Logs Command",
                                    description="To have the logs of the bot on your server",
                                    colour = discord.Colour.purple()
                                    )
                embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                text = "JeSuisUnBonWhisky#1688")
                embed.set_author (name = "Unconnected Bot#8157",
                                icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
                embed.add_field(name=":gear: Available Setup Commands :gear:",
                                value=")logs <#the-channel-you-want>",
                                inline = False)
                embed.add_field(name="Information about the command",
                                    value="To place the bot logs to the channel you want, please mention the channel. If you don't mention it, Nothing will happen",
                                    inline = False)

            else:
                db = sqlite3.connect("main.sqlite")
                cursor = db.cursor()
                cursor.execute(f"SELECT logchannel FROM main WHERE guild_id = {ctx.guild.id}")
                logresult = cursor.fetchone()

                if logresult is None :
                        sql = ("INSERT INTO main(guild_id, logchannel) VALUES(?,?)")
                        val = (ctx.guild.id, logchannel.id)
                        embed = discord.Embed(description="Logs channel has been set or updated !", 
                                            colour = discord.Colour.purple()
                                            )

                else:
                    sql = ("UPDATE main SET logchannel = ? WHERE guild_id = ?")
                    val = (logchannel.id, ctx.guild.id)
                    embed = discord.Embed(description="Logs channel has been set or updated !",
                                        colour = discord.Colour.purple()
                                        )

                cursor.execute(sql, val)
                db.commit()
                cursor.close()
                db.close()

            await ctx.message.channel.send(embed = embed)

def setup(client):
    client.add_cog(logcommand(client))
    print("Logs command cog ready !")
