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

db = sqlite3.connect("main.sqlite")
cursor = db.cursor()

class unvocal(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        ### variable declaration ###

        try:
            guildname = member.guild.name
        
            user = member
            userid = member.id
            creator = client.get_user(341257685901246466)

            infojour = time.strftime("%H:%M:%S %d/%m/%Y")

            statut = member.status

            vocalname = after.channel.name

            ### declaring differents embeds ###

            # embed vocal for users #

            embedvocal = discord.Embed(title = "You can't join the vocal",
                                        description = "You tried to join a vocal in invisible status, but you can't on this server\nI give you the infos of your connection.",
                                        colour = discord.Colour.gold()
                                        )
            embedvocal.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                    text = "JeSuisUnBonWhisky#1688")
            embedvocal.set_author(name = "Unconnected Bot#8157",
                                    icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
            embedvocal.add_field(name = "Server name :",
                                    value = f"{guildname}",
                                    inline = True)
            embedvocal.add_field(name = "Channel name :",
                                    value = f"{vocalname}",
                                    inline = True)
            embedvocal.add_field(name = "Change your status",
                                    value = f"and try again :wink:",
                                    inline = False)

            # embed vocal for logs and me #

            embedvocalperso = discord.Embed(title = "VOCAL",
                                            description = f"**{user}** / **{userid}** tried to join a vocal in invisible status\nInfos of the connection.",
                                            colour = discord.Colour.gold()
                                            )
            embedvocalperso.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                        text = "JeSuisUnBonWhisky#1688")
            embedvocalperso.set_author(name = "Unconnected Bot#8157",
                                        icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
            embedvocalperso.add_field(name = "Server name :",
                                        value = f"{guildname}",
                                        inline = True)
            embedvocalperso.add_field(name = "Channel name :",
                                        value = f"{vocalname}",
                                        inline = True)
            embedvocalperso.add_field(name = "Date infos :",
                                        value = f"{infojour}",
                                        inline = False)

            ### Starting code ###

            if after.channel is None:
                return
            elif after.channel is not None:
                if statut is discord.Status.offline or statut is discord.Status.Idle or statut is discord.Status.DoNotDisturb:
                    cursor.execute(f"SELECT bypassrole FROM main WHERE guild_id = {member.guild.id}")
                    bpresult = cursor.fetchone()
                    if str(bpresult) == "(None,)" or str(bpresult) == "None":
                        pass
                    else:
                        bpresult = (str(bpresult[0]).split(","))
                        for x in range(len(bpresult)):
                            if get(user.roles, id = int(bpresult[x])):
                                return
                    
                    cursor.execute(f"SELECT streampass FROM main WHERE guild_id = {member.guild.id}")
                    StreamPassValue = cursor.fetchone()
                    if after.self_stream is True:
                        if str(StreamPassValue) == "(None,)" or str(StreamPassValue) == "None":
                            pass
                        else:
                            return
                    
                    if userid == int(341257685901246466):
                        return
                    elif user.guild_permissions.administrator:
                        return
                    elif get(user.roles, name = "AllowUnconnected"):
                        return
                    elif user.bot:
                        return
                    elif after.channel == member.guild.afk_channel:
                        return
                    else:

                        cursor.execute(f"SELECT logchannel FROM main WHERE guild_id = {member.guild.id}")
                        logresult = cursor.fetchone()

                        try:
                            await member.move_to(None)
                        except discord.Forbidden:
                            return
                        
                        try:
                            if logresult is not None :
                                await client.get_channel(int(logresult[0])).send(embed = embedvocalperso)
                        except TypeError:
                            pass

                        try:
                            await member.send(embed = embedvocal)
                        except discord.Forbidden:
                            pass
                            
                        await creator.send(embed = embedvocalperso)
                        print (f"\nVOCAL\nGuildname = {guildname}\nVocal name = {vocalname}\nUser = {user} / {userid}\nDate infos = {infojour}")
        except AttributeError:
            return


def setup(client):
    client.add_cog(unvocal(client))
    print("Unconnected Vocals cog ready !")
