import discord
import asyncio
from discord.ext.commands import Bot, CommandNotFound
from discord.ext import commands, tasks
import datetime
from datetime import timezone, tzinfo, timedelta, date
import time
from discord.utils import get
import logging
import os
import sqlite3
from unconnectedbot_complete import client

class unmessage(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_message(self, message):

        ### variable declaration ###

        guildname = message.guild
    
        channelname = message.channel

        user = message.author
        userid = message.author.id
        creator = client.get_user(341257685901246466)

        infojour = time.strftime("%H:%M:%S %d/%m/%Y")
        
        messagecontent = message.content

        if not messagecontent:
            return

        ### declaring differents embeds ###

        # embed typing for users #

        embedtyping = discord.Embed(title = "Your message has been deleted",
                                    description = "You tried to type a message in invisible status, but you can't on this server\nI give you the infos of your message.",
                                    colour = discord.Colour.purple()
                                    )
        embedtyping.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                text = "JeSuisUnBonWhisky#1688")
        embedtyping.set_author(name = "Unconnected Bot#8157",
                                icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        embedtyping.add_field(name = "Server name :",
                                value = f"{guildname}",
                                inline = True)
        embedtyping.add_field(name = "Channel name :",
                                value = f"#{channelname}",
                                inline = True)
        embedtyping.add_field(name = f"Your message was :",
                                value = f"{messagecontent}",
                                inline = False)
        embedtyping.add_field(name = "Change your status",
                                value = f"and try again :wink:",
                                inline = False)

        # embed typing for logs or me #

        embedtypingperso = discord.Embed(title = "TYPING",
                                        description = f"**{user}** / **{userid}** tried to type a message in invisible status\nInfos of the message.",
                                        colour = discord.Colour.purple()
                                        )
        embedtypingperso.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                    text = "JeSuisUnBonWhisky#1688")
        embedtypingperso.set_author(name = "Unconnected Bot#8157",
                                    icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        embedtypingperso.add_field(name = "Server name :",
                                    value = f"{guildname}",
                                    inline = True)
        embedtypingperso.add_field(name = "Channel name :",
                                    value = f"#{channelname}",
                                    inline = True)
        embedtypingperso.add_field(name = f"The message was :",
                                    value = f"{messagecontent}",
                                    inline = False)
        embedtypingperso.add_field(name = "Date infos :",
                                    value = f"{infojour}",
                                    inline = False)

        ### Starting code ###

        try:
            statut = user.status
            if statut is discord.Status.offline:
                db = sqlite3.connect("main.sqlite")
                cursor = db.cursor()
                cursor.execute(f"SELECT bypassrole FROM main WHERE guild_id = {message.guild.id}")
                bpresult = cursor.fetchone()
                if bpresult is None:
                    pass
                else:
                    try:
                        if get(user.roles, id = int(str(bpresult[0]))):
                            return
                    except ValueError:
                        pass
                
                if userid == int(341257685901246466):
                    return
                elif user.guild_permissions.administrator:
                    return
                elif get(user.roles, name = "AllowUnconnected"):
                    return
                elif user.bot:
                    return
                else:

                    cursor.execute(f"SELECT logchannel FROM main WHERE guild_id = {message.guild.id}")
                    logresult = cursor.fetchone()

                    try:
                        await message.delete()
                    except discord.Forbidden:
                        return

                    try:
                        if logresult is not None :
                            await client.get_channel(int(logresult[0])).send(embed = embedtypingperso)
                    except TypeError:
                        pass
                        
                    try:
                        await message.author.send(embed = embedtyping)
                    except discord.Forbidden:
                        pass

                    await creator.send(embed = embedtypingperso)
                    print (f"\nTYPING\nGuild name = {guildname}\nChannel name = #{channelname}\nUser = {user} / {userid}\nMessage content = {messagecontent}\nDate infos = {infojour}")
        except AttributeError:
            return



def setup(client):
    client.add_cog(unmessage(client))
    print("Unconnected Messages cog ready !")