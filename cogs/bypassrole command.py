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

class bypassrolecommand(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.group(invoke_without_command=True)
    async def bypassrole(self, ctx):

        creator = self.client.get_user(341257685901246466)

        if ctx.message.author.guild_permissions.administrator:

            EmbedNone = discord.Embed(title="Available commands :",
                                    description = "Bypassrole command is used if an admin need to add a role as a bot rules bypasser\nIf you add a role to the list, all members who will have this role will be able to speak/send messages in offline status",
                                    colour = discord.Colour.purple())
            
            EmbedNone.add_field(name = ")bypassrole list",
                                value = "Give the bypassrole list you defined",
                                inline = False)
            EmbedNone.add_field(name = ")bypassrole add <Role Mention>",
                                value = "Add a role to your bypassrole list",
                                inline = False)
            EmbedNone.add_field(name = ")bypassrole remove <Role Mention>",
                                value = "Remove a role to your bypassrole list",
                                inline = False)
            EmbedNone.set_footer(icon_url = f"{creator.avatar_url}",
                                text = f"{creator}")
            
            await ctx.send(embed = EmbedNone)
    
    @bypassrole.command()
    async def list(self, ctx):

        creator = self.client.get_user(341257685901246466)

        if ctx.message.author.guild_permissions.administrator:

            cursor.execute(f"SELECT bypassrole FROM main WHERE guild_id = {ctx.guild.id}")
            customrole = cursor.fetchone()

            if customrole[0] is None :
                EmbedCustom = discord.Embed(title = "I haven't bypassrole in my database",
                                            description = "You must to add a bypassrole to the list using ``)bypassrole add <Role Mention>`` to print the bypassrole list",
                                            colour = discord.Colour.red())

                EmbedCustom.set_footer(icon_url = f"{creator.avatar_url}",
                                        text = f"{creator}")
            
            else :
                RoleList = ""
                customrole = (str(customrole[0]).split(","))

                for x in range(len(list(customrole))):
                    RoleList += f"<@&{customrole[x]}>\n"

                EmbedCustom = discord.Embed(title = "BypassRole list :",
                                            description = f"{RoleList}",
                                            colour = discord.Colour.purple())
                
                EmbedCustom.set_footer(icon_url = f"{creator.avatar_url}",
                                        text = f"{creator}")
                
            await ctx.send(embed = EmbedCustom)

    @bypassrole.command()
    async def add(self, ctx, RoleMention : discord.Role = None):

        EmbedDone = discord.Embed(description = "The role has been added to the bypassrole list",
                                colour = discord.Colour.green())

        if ctx.message.author.guild_permissions.administrator:

            if RoleMention is None :

                EmbedRoleMentionNone = discord.Embed(title = "Role Mention is blank",
                                                    description = "You must to mention a role to add your role to the bypassrole list\n Syntax : ``)bypassrole add <Role Mention>``",
                                                    colour = discord.Colour.red())

                await ctx.send(embed = EmbedRoleMentionNone)

            else:

                cursor.execute(f"SELECT bypassrole FROM main WHERE guild_id = {ctx.guild.id}")
                customrole = cursor.fetchone()

                if str(customrole) == "None":

                    sql = ("INSERT INTO main(guild_id, bypassrole) VALUES(?,?)")
                    val = (ctx.guild.id, RoleMention.id)
                    cursor.execute(sql, val)
                    db.commit()
                
                elif str(customrole) == "(None,)":

                    sql = ("UPDATE main SET bypassrole = ? WHERE guild_id = ?")
                    val = (RoleMention.id, ctx.guild.id)
                    cursor.execute(sql, val)
                    db.commit()

                else :
                    rolelist = (str(customrole[0]).split(","))

                    if str(RoleMention.id) in list(rolelist):

                        EmbedDone = discord.Embed(description = "This role is already in the bypassrole list\nYou can't add 2 times the same role to the list.",
                                                colour = discord.Colour.red())

                    else :
                        
                        NewRole = ""

                        for x in range(len(list(customrole))):

                            NewRole += customrole[x]
                            
                            if x < len(list(customrole)):
                                NewRole +=","

                        NewRole += f"{RoleMention.id}"

                        sql = ("UPDATE main SET bypassrole = ? WHERE guild_id = ?")
                        val = (NewRole, ctx.guild.id)
                        cursor.execute(sql, val)
                        db.commit()

                await ctx.send(embed = EmbedDone)
    
    @bypassrole.command()
    async def remove(self, ctx, RoleMention : discord.Role = None):

        if ctx.message.author.guild_permissions.administrator:

            ### Déclaration des Embeds ###

            EmbedDone = discord.Embed(description = "The role has been removed to the bypassrole list",
                                        colour = discord.Colour.green())

            EmbedImpossible = discord.Embed(description = "This role isn't in your bypassrole list\nType ``)bypassrole list`` to have your role list",
                                        colour = discord.Colour.red())

            EmbedEmptyList = discord.Embed(description = "Your role list is empty\nType ``)bypassrole add <Role Mention>`` to add a role to your bypassrole list",
                                        colour = discord.Colour.red())

            ### Code ###

            if RoleMention is None :

                EmbedRoleMentionNone = discord.Embed(title = "Role Mention is blank",
                                                    description = "You must to mention a role to remove the role to the bypassrole list\n Syntax : ``)bypassrole remove <Role Mention>``",
                                                    colour = discord.Colour.red())

                await ctx.send(embed = EmbedRoleMentionNone)
            
            else:
                cursor.execute(f"SELECT bypassrole FROM main WHERE guild_id = {ctx.guild.id}")
                customrole = cursor.fetchone()

                if str(customrole) == "(None,)" or str(customrole) == "None":

                    await ctx.send(embed = EmbedEmptyList)
                
                else:

                    customrole = (str(customrole[0]).split(","))

                    if str(RoleMention.id) in list(customrole):

                        customrole.remove(f"{RoleMention.id}")

                        NewRoleList = ""
                        for x in range(len(list(customrole))):
                            NewRoleList += customrole[x]
                            if x < len(list(customrole))-1:
                                NewRoleList +=","

                        if len(customrole) == 0:
                            sql = (f"UPDATE main SET bypassrole = NULL WHERE guild_id = {ctx.guild.id}")
                            cursor.execute(sql)
                            db.commit()
                        
                        else:
                            sql = ("UPDATE main SET bypassrole = ? WHERE guild_id = ?")
                            val = (NewRoleList, ctx.guild.id)
                            cursor.execute(sql, val)
                            db.commit()

                        await ctx.send(embed = EmbedDone)
                    
                    else:

                        await ctx.send(embed = EmbedImpossible)
            
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, RoleNotFound):
            embed = discord.Embed(description = "You must mention a role. Not type it like you done\nYou must to type it like this :\n``)bypassrole add <@the-role-you-want>``\nor\n``)bypassrole remove <@the-role-you-want>``\n\nexample :\n**)bypassrole add @AllowUnconnected**\n**)bypassrole remove @AllowUnconnected**",
                                colour = discord.Colour.red()
                                )
            await ctx.message.channel.send(embed = embed)

    

def setup(client):
    client.add_cog(bypassrolecommand(client))
    print("BypassRole command cog ready !")
