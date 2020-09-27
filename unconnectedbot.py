import discord
import time
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import datetime
from datetime import timezone, tzinfo, timedelta
import time as timeModule
from discord.utils import get
import dbl
import logging
import os

TOKEN = 'NzAyNTUyNjQ5MDQzNTQyMDE3.XqBtLA.MYFYgmArGIv9u2SELI0MWcJSGgk'

client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name=")help",
                                                            url="https://www.twitch.tv/ps_racing_team/"))

    #for member in client.get_all_members():
    #    print(member, member.status)
    print("bot ready !!")

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Hi administrator of this server.\n\nI made my own server to help you if you need it, and to notify you of upcoming updates.\nYou can join my server with this link : https://discord.gg/gqfFqJp \n\nCordially : Creator of this bot.")
        break


@client.event
async def on_message(message):
    
    guildname = message.guild.name
    
    channelname = message.channel.name
    
    user = message.author
    userid = message.author.id
    creator = client.get_user(341257685901246466)

    infojour = datetime.datetime.now()
    
    messagecontent = message.content
    
    statut = message.author.status

    embed = discord.Embed()
    
    if message.content.startswith(')help'):
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
        
        await message.channel.send(embed = embed)

        

    if message.content.startswith(')stats'):
        embed = discord.Embed(title = "Stats Command",
                                  description = "They are the stats of my bot",
                                  colour = discord.Colour.purple()
                                  )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
        embed.set_author (name = "Unconnected Bot#8157",
                          icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        embed.add_field(name = ")help",
                        value = "[You can click on this link to see the bot page](https://top.gg/bot/543924044110626826)",
                        inline = False)
        embed.set_image(url = "https://top.gg/api/widget/543924044110626826.png?usernamecolor=ffffff")

        await message.channel.send(embed = embed)

        
    
    if message.content.startswith(')invite'):
        embed = discord.Embed(title="Join author's server here",
                              url='https://discord.gg/gqfFqJp',
                              description="For management, ideas I can code and others things to have a better bot",
                              colour = discord.Colour.purple()
                              )
        embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
        embed.set_author (name = "Unconnected Bot#8157",
                          icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')
        embed.add_field(name = "Add me to your server",
                        value = "[Click here to invite me \non your server](https://discord.com/oauth2/authorize?client_id=543924044110626826&permissions=8&scope=bot)",
                        inline = True)
        embed.add_field(name = "Vote me please",
                        value = "[You can vote me up on top.gg by \nclicking on this link](https://top.gg/bot/543924044110626826/vote)",
                        inline = True)
    
        await message.channel.send(embed = embed)

        

    if message.content.startswith(')createrole'):
        if user.guild_permissions.administrator:
            if get(message.guild.roles, name = 'AllowUnconnected'):
                embed = discord.Embed(title="Create role :no_entry_sign:",
                              description='**You already have a role named "__AllowUnconnected__". You can already give this role to whoever you want**',
                              colour = discord.Colour.red()
                              )
                embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
                embed.set_author (name = "Unconnected Bot#8157",
                                  icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')

                await message.channel.send(embed = embed)
        
            else :
                await message.guild.create_role(name='AllowUnconnected')
                embed = discord.Embed(title="Create role :white_check_mark:",
                              description='**The role "__AllowUnconnected__" has been created. You can now give this role to whoever you want so they can speak offline**',
                              colour = discord.Colour.green()
                              )
                embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/341257685901246466/6a2c7949778597a955eba4e9585b7a63.png?size=4096",
                         text = "JeSuisUnBonWhisky#1688")
                embed.set_author (name = "Unconnected Bot#8157",
                                  icon_url = 'https://cdn.discordapp.com/avatars/543924044110626826/1341bf81b2289bf25bd0e5de2aafbad2.png?size=4096')

                await message.channel.send(embed = embed)
        else :
            return


        
    
    if statut is discord.Status.offline:
        if userid == int(341257685901246466):
            return
        elif user.guild_permissions.administrator:
            return
        elif get(user.roles, name = 'AllowUnconnected'):
            return
        else:
            if message.channel.permissions_for(message.guild.me).manage_messages:
                await message.delete()
                await message.author.send(f"You tried to type a message in invisible status, but you can't on this server. \nI give you the infos of your message. \nServer name : {guildname} \nChannel name : #{channelname} \nYour message was : {messagecontent} \n \nChange your status and send your message again :wink:")
                await creator.send(f"{user} / {userid} tried to type a message in invisible status. \n Infos of the message. \n Server name : {guildname} \n Channel name : #{channelname} \n Date infos : {infojour} \n \n The message was : {messagecontent}")
                print (f"{guildname}, {channelname}, {user}, {messagecontent}")
                print (f"{infojour}")
            else:
                return

@client.event
async def on_voice_state_update(member, before, after):

    guildname = member.guild.name
    
    user = member
    userid = member.id
    creator = client.get_user(341257685901246466)

    vocalname = after.channel.name

    infojour = datetime.datetime.now()

    statut = member.status

    if statut is discord.Status.offline:
        if after.channel is not None :
            if userid == int(341257685901246466):
                return
            elif user.guild_permissions.administrator:
                return
            elif get(user.roles, name = 'AllowUnconnected'):
                return
            else:
                await member.move_to(None)
                await member.send(f"You tried to connect to a vocal in invisible status, but you can't on this server. \nI give you the infos of your message. \nServer name : {guildname} \nVocal name : {vocalname} \n \nChange your status and try to connect again in the voice you want :wink:")
                await creator.send(f"{user} / {userid} tried to connect to a vocal in invisible status. \nInfos of the message. \nServer name : {guildname} \nVocal name : {vocalname} \nDate infos : {infojour}")
                print (f"{guildname}, {vocalname}, {user}, {userid} \n{infojour}")

client.run(TOKEN)
