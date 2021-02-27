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

class SupportCommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def support(self, ctx, *, SupportMessage : str=None):

        infojour = time.strftime("%H:%M:%S %d/%m/%Y")

        if ctx.message.author.guild_permissions.administrator and ctx.message.guild != None:
            
            if SupportMessage == None :
                EmbedErrorNone = discord.Embed(title = "Error !!",
                                                description = "You need to put a request in your support message !\n``)support <your full request in one message>``",
                                                colour = discord.Colour.red()
                                                )
                ErrorMessage = await ctx.send(embed = EmbedErrorNone)
                await asyncio.sleep(5)
                await ctx.message.author.delete()
                await ErrorMessage.delete()
            
            else :
                EmbedMessageSent = discord.Embed(title = "Sent !",
                                                description = "Your request has been sent. Check your discord friend invitations.\nThe bot owner will add you as friend if he need it !\nGo check on the [bot owner server](https://discord.gg/gqfFqJp) to know when your support help is done !",
                                                colour = discord.Colour.green()
                                                )
                
                client.EmbedSupportRequest = discord.Embed(title = "Support Required !",
                                                        description = f"**Ticket opened by :**\n{ctx.message.author} / {ctx.message.author.id}\n\n**Guild :**\n{ctx.guild.name} / {ctx.guild.id}\n\n**Date / Time of the message :**\n{infojour}\n\n**Support Message :**\n{SupportMessage}",
                                                        colour = discord.Colour.red()
                                                        )
                
                await client.get_channel(795364029538631750).send(embed = client.EmbedSupportRequest)
                await ctx.send(embed = EmbedMessageSent)




def setup(client):
    client.add_cog(SupportCommand(client))
    print("Support command cog ready !")