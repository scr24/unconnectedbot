import discord
from discord import Intents
from discord.ext import commands,tasks
from discord.ext.commands import Bot, CommandInvokeError, UserNotFound
from discord.utils import get
from datetime import timezone, tzinfo, timedelta
import time as timeModule
import math
import random
import asyncio
import os
from unconnectedbot_complete import client

class SupportAssistance(commands.Cog):
    def __init__(self, client):
        self.bot = client

    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        creator = client.get_user(341257685901246466)

        if payload.user_id == creator.id:

            if payload.emoji.name == '✅':

                if payload.channel_id == 795364029538631750 :

                    EmbedContent = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)

                    EmbedInfos = EmbedContent.embeds

                    EmbedSupportCheck = discord.Embed(title = "Support done !",
                                                    description = f"{EmbedInfos[0].description}",
                                                    colour = discord.Colour.green()
                                                    )
                    
                    await EmbedContent.edit(embed = EmbedSupportCheck)



def setup(client):
    client.add_cog(SupportAssistance(client))
    print("Support Assistance cog ready !")