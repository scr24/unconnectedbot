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

class helpcommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):

        creator = self.client.get_user(341257685901246466)

        botuser = self.client.get_user(543924044110626826)

        embed = discord.Embed(title = "Help Command",
                                  description = "The list of all commands available for users and/or admins.\nMy main utility is to avoid offline members to chat and to connect in vocal in offline mode.",
                                  colour = discord.Colour.purple()
                                  )
        embed.set_footer(icon_url = f"{creator.avatar_url}",
                        text = f"{creator}")
        embed.set_author (name = f"{botuser}",
                          icon_url = f"{botuser.avatar_url}")
        embed.add_field(name = ")help",
                        value = "This command. Show you the availables commands.\n**Can be used by all users**",
                        inline = False)
        embed.add_field(name = ")invite",
                        value = "Show all links that may be useful (for you and for me).\n**Can be used by all users**",
                        inline = False)
        embed.add_field(name = ")stats",
                        value = "Show all stats of my bot and his TopGG page.\n**Can be used by all users**",
                        inline = False)

        if ctx.message.author.guild_permissions.administrator:
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
                            value = "Do the same thing as the ``)createrole`` command but with one of your roles.\n~~**Only ONE ROLE** can be set with this command~~\nYou can now add multiple roles to your bypassrole list !\nTry the command to have more infos about it.\n**__Only admins__ can use this command**",
                            inline = False)
            embed.add_field(name = ")support",
                            value = "Use this command if you need help or ask something about the bot itself (update idea, the bot doesn't work...)\nTo use the command :\n``)support <Your full request>``\n**__Only admins__ can use this command**",
                            inline = False)
            embed.add_field(name = ")streampass",
                            value = "Use this command if you want all users can display their screen self muted and in offline status\nTo use the command :\n``)streampass on/off``\nOn typing ``)streampass`` you will have more infos about the command, and you'll be able to see if it is activated or not on the server.\n**__Only admins__ can use this command**",
                            inline = False)
        
        else:
            embed.add_field(name = "You're not admin",
                            value = "When an admin type this command, it shows more commands only available for them",
                            inline = False)

        
        await ctx.message.channel.send(embed = embed)
    
def setup(client):
    client.add_cog(helpcommand(client))
    print("Help command cog ready !")
