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

class helpcommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "Help Command",
                                  description = "The list of all commands available for users and/or admins.\nMy main utility is to avoid offline members to chat and to connect in vocal in offline mode.",
                                  colour = discord.Colour.purple()
                                  )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
        embed.set_author (name = "Unconnected Bot#8157",
                          icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        embed.add_field(name = ")help",
                        value = "This command. Show you the availables commands.\n**Can be used by all users**",
                        inline = False)
        embed.add_field(name = ")invite",
                        value = "Show all links that may be useful (for you and for me).\n**Can be used by all users**",
                        inline = False)
        embed.add_field(name = ")stats",
                        value = "Show all stats of my bot and his TopGG page.\n**Can be used by all users**",
                        inline = False)
        embed.add_field(name = ")createrole",
                        value = 'Create a role named "AllowUnconnected" to give users the possibility of being able to speak on the server.\n**__Only admins__ can use this command and give the role to users**',
                        inline = False)
        embed.add_field(name = ")antighosting",
                        value = "Activate the AntiGhosting on your server.\nType the command to have more infos on it.\n**__Only admins__ can use this command**",
                        inline = False)
        embed.add_field(name = ")logs",
                        value = "Activate the logs on your server. With it, you can see all the logs of your servers (who typed in offline mode, tried to ghost...).\nType the command to have more infos on it.\n**__Only admins__ can use this command**",
                        inline = False)
        embed.add_field(name = ")bypassrole",
                        value = "Do the same thing as the ``)createrole`` command but with one of your custom roles.\n**Only ONE ROLE** can be set with this command\n**__Only admins__ can use this command**",
                        inline = False)
        embed.add_field(name = ")support",
                        value = "Use this command if you need help or ask something about the bot itself (update idea, the bot doesn't work...)\nTo use the command :\n``)support <Your full request>``\n**__Only admins__ can use this command**",
                        inline = False)
        
        await ctx.message.channel.send(embed = embed)
    
def setup(client):
    client.add_cog(helpcommand(client))
    print("Help command cog ready !")