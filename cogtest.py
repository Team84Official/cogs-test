import discord
import json
from discord.ext import commands

with open('settings.json', 'r') as json_file:
  settings = json.load(json_file)

class cogtest(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command()
    async def cogaddtest(self, ctx):
        await ctx.send('Hello World!')

def setup(client):
    client.add_cog(cogtest(client))
