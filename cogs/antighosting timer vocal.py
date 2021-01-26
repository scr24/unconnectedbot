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

class agtimer(commands.Cog):
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

            try:
                vocalname = after.channel.name
            except AttributeError:
                return
                
            ### declaring differents embeds ###

            # embed unactive or ghosting for users #

            embedunactive = discord.Embed(title = "You've been kicked out the vocal",
                                        description = "You were unactive or you tried to ghost a discord vocal conversation, but you're not allowed to do it on this server. \nI give you the infos of your connection.",
                                        colour = discord.Colour.dark_magenta()
                                        )
            embedunactive.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                text = "JeSuisUnBonWhisky#1688")
            embedunactive.set_author (name = "Unconnected Bot#8157",
                                    icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
            embedunactive.add_field(name = "Server name :",
                                    value = f"{guildname}",
                                    inline = True)
            embedunactive.add_field(name = "Channel name :",
                                    value = f"{vocalname}",
                                    inline = True)
            embedunactive.add_field(name = "reactivate your microphone",
                                    value = f"and try again to connect :wink:",
                                    inline = False)

            # embed unactive or ghosting logs logs or me #

            embedunactiveperso = discord.Embed(title = "UNACTIVE OR GHOSTING",
                                            description = f"**{user}** / **{userid}** were unactive or tried to ghost a discord vocal conversation\nInfos of the connection.",
                                            colour = discord.Colour.dark_magenta()
                                            )
            embedunactiveperso.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                        text = "JeSuisUnBonWhisky#1688")
            embedunactiveperso.set_author (name = "Unconnected Bot#8157",
                                        icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
            embedunactiveperso.add_field(name = "Server name :",
                                        value = f"{guildname}",
                                        inline = True)
            embedunactiveperso.add_field(name = "Channel name :",
                                        value = f"{vocalname}",
                                        inline = True)
            embedunactiveperso.add_field(name = "Date infos :",
                                        value = f"{infojour}",
                                        inline = False)

            # embed ghosting for users #

            embedghosting = discord.Embed(title = "You can't join the vocal",
                                        description = "You tried to join a vocal self muted, but you can't on this server.\nWe call that ghosting, and it's not allowed on this server.\nI give you the infos of your connection.",
                                        colour = discord.Colour.dark_orange()
                                        )
            embedghosting.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                    text = "JeSuisUnBonWhisky#1688")
            embedghosting.set_author(name = "Unconnected Bot#8157",
                                    icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
            embedghosting.add_field(name = "Server name :",
                                    value = f"{guildname}",
                                    inline = True)
            embedghosting.add_field(name = "Channel name :",
                                    value = f"{vocalname}",
                                    inline = True)
            embedghosting.add_field(name = "reactivate your microphone",
                                    value = f"and try again to connect :wink:",
                                    inline = False)

            # embed ghosting for logs or me #

            embedghostingperso = discord.Embed(title = "GHOSTING",
                                                description = f"**{user}** / **{userid}** tried to ghost a discord vocal conversation\nInfos of the connection.",
                                                colour = discord.Colour.dark_orange()
                                                )
            embedghostingperso.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                                        text = "JeSuisUnBonWhisky#1688")
            embedghostingperso.set_author(name = "Unconnected Bot#8157",
                                        icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
            embedghostingperso.add_field(name = "Server name :",
                                        value = f"{guildname}",
                                        inline = True)
            embedghostingperso.add_field(name = "Channel name :",
                                        value = f"{vocalname}",
                                        inline = True)
            embedghostingperso.add_field(name = "Date infos :",
                                        value = f"{infojour}",
                                        inline = False)

            ### starting code ###

            db = sqlite3.connect("main.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT timer FROM main WHERE guild_id = {member.guild.id}")
            agtimer = cursor.fetchone()

            if agtimer is None:
                return
            else:
                if int(str(agtimer[0])) > 0:
                    cursor.execute(f"SELECT bypassrole FROM main WHERE guild_id = {member.guild.id}")
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
                        if before.channel == after.channel:
                            if after.self_mute == True:
                                await asyncio.sleep(int(str(agtimer[0])))
                                if before.channel == after.channel:
                                    if after.self_mute == True:

                                        cursor.execute(f"SELECT logchannel FROM main WHERE guild_id = {member.guild.id}")
                                        logresult = cursor.fetchone()

                                        try:
                                            await member.move_to(None)
                                        except discord.Forbidden:
                                            return

                                        try:
                                            if logresult is not None :
                                                await client.get_channel(int(logresult[0])).send(embed = embedunactiveperso)
                                        except TypeError:
                                            pass

                                        try:
                                            await member.send(embed = embedunactive)
                                        except discord.Forbidden:
                                            pass
                                        await creator.send(embed = embedunactiveperso)
                                        print (f"\nUNACTIVE OR GHOSTING\nGuildname = {guildname}\nVocal name = {vocalname}\nUser = {user} / {userid}\nDate infos = {infojour}")

                        else:
                            if after.self_mute == True:

                                cursor.execute(f"SELECT logchannel FROM main WHERE guild_id = {member.guild.id}")
                                logresult = cursor.fetchone()

                                try:
                                    await member.move_to(None)
                                except discord.Forbidden:
                                    return

                                try:
                                    if logresult is not None :
                                        await client.get_channel(int(logresult[0])).send(embed = embedghostingperso)
                                except TypeError:
                                    pass
                                
                                try:
                                    await member.send(embed = embedghosting)
                                except discord.Forbidden:
                                    pass

                                await creator.send(embed = embedghostingperso)
                                print (f"\nGHOSTING\nGuildname = {guildname}\nVocal name = {vocalname}\nUser = {user} / {userid}\nDate infos = {infojour}")
        except discord.HTTPException:
            return
        except ValueError:
            return


def setup(client):
    client.add_cog(agtimer(client))
    print("AG Timer Vocal launch !")