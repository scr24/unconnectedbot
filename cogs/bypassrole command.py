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
from unconnectedbot_complete import client

class bypassrolecommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def bypassrole (self, ctx, bprole: discord.Role=None):
        if ctx.message.author.guild_permissions.administrator:

            if bprole is None :
                embed = discord.Embed(title="BypassRole Command",
                                    description="To have a custom role bypasser (like \"AllowUnconnected\" role)",
                                    colour = discord.Colour.purple()
                                    )
                embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                text = "JeSuisUnBonWhisky#1688")
                embed.set_author (name = "Unconnected Bot#8157",
                                icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
                embed.add_field(name=":gear: Available Setup Commands :gear:",
                                value=")bypassrole <@the-role-you-want>",
                                inline = False)
                embed.add_field(name="Information about the command",
                                    value="This command is nice to give the \"Admins\" autorizations to the staff. With this command, they will be able to bypass the bot rules.\nTo have the custom role bypasser, please mention the role. If you don't mention it, Nothing will happen",
                                    inline = False)
            
            else:
                db = sqlite3.connect("main.sqlite")
                cursor = db.cursor()
                cursor.execute(f"SELECT bypassrole FROM main WHERE guild_id = {ctx.guild.id}")
                customrole = cursor.fetchone()
                
                if customrole is None :
                    sql = ("INSERT INTO main(guild_id, bypassrole) VALUES(?,?)")
                    val = (ctx.guild.id, bprole.id)
                    embed = discord.Embed(description="Custom role bypasser set or updated !", 
                                        colour = discord.Colour.purple()
                                        )
                    embedperso = discord.Embed(title = "Custom role bypasser set or updated !",
                                            description = f"The custom role bypasser has been set or updated on **{ctx.guild.name}** / **{ctx.guild.id}** to **{bprole}** / **{bprole.id}**",
                                            colour = discord.Colour.dark_green()
                                            )

                else:
                    sql = ("UPDATE main SET bypassrole = ? WHERE guild_id = ?")
                    val = (bprole.id, ctx.guild.id)
                    embed = discord.Embed(description="Custom role bypasser set or updated !",
                                        colour = discord.Colour.purple()
                                        )
                    embedperso = discord.Embed(title = "Custom role bypasser set or updated !",
                                            description = f"The custom role bypasser has been set or updated on **{ctx.guild.name}** / **{ctx.guild.id}** to **{bprole}** / **{bprole.id}**",
                                            colour = discord.Colour.dark_green()
                                            )

                cursor.execute(sql, val)
                db.commit()
                cursor.close()
                db.close()

            await ctx.message.channel.send(embed = embed)
            await client.get_channel(748847582033477743).send(embed = embedperso)



    @bypassrole.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            embed = discord.Embed(description = "You must mention a role. Not type it like you done\nYou must to type it like this :\n``)bypassrole <@the-role-you-want>``\nexample : **)bypassrole @AllowUnconnected**",
                                colour = discord.Colour.red()
                                )
            await ctx.message.channel.send(embed = embed)

            
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, RoleNotFound):
            return

    

def setup(client):
    client.add_cog(bypassrolecommand(client))
    print("BypassRole command cog ready !")