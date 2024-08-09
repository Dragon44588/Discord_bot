import discord
from discord.ext import commands


class models_cog(commands.Cog):
    def __init__(self, bot):
        #self.message = "it's Work in progress wednesday BOZOS. post models or feet pics <@&1201397388649173044>"
        self.message = "hello"

    @commands.command(name="WIP", help="gets the bozoids to post")
    async def post_message(self, ctx):
        await ctx.send(self.message)