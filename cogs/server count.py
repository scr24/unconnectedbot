import dbl
import discord
from discord.ext import commands, tasks
import asyncio
import requests
import logging

url = 'https://top.gg/api/bots/543924044110626826/stats'
headers = {'Authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU0MzkyNDA0NDExMDYyNjgyNiIsImJvdCI6dHJ1ZSwiaWF0IjoxNTk4NTE2MjA5fQ.6tB_r1stD2DJaLOFj8ZK9PIWo-CjWIO1Ra-M5JslLg8'}

res = requests.get(url, headers=headers)

print (res)


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""


    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog pret !")


    def __init__(self, client):
        self.bot = client
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU0MzkyNDA0NDExMDYyNjgyNiIsImJvdCI6dHJ1ZSwiaWF0IjoxNTk4NTE2MjA5fQ.6tB_r1stD2DJaLOFj8ZK9PIWo-CjWIO1Ra-M5JslLg8'
        self.dblpy = dbl.DBLClient(self.bot, self.token)
        self.update_stats.start()

    @tasks.loop(minutes=3.0)
    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        logger.info('Attempting to post server count')
        try:
            await self.dblpy.post_guild_count()
            logger.info('Posted server count ({})'.format(self.dblpy.guild_count()))
            print("server count envoyé !!")
        except Exception as e:
            logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            print("erreur de l'envoi du server count")

def setup(client):
    global logger
    logger = logging.getLogger('bot')
    client.add_cog(TopGG(client))
