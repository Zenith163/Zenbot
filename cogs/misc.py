import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandOnCooldown
from discord.ext.commands.cooldowns import BucketType

class misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        latency = self.client.latency * 1000
        latency_round = round(latency,2)
        await ctx.send(f"{latency_round}ms")

    @commands.command(aliases = ["hello", "hai"])
    async def hi(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}")

    @commands.command(aliases = ["bai"])
    async def bye(self, ctx):
        await ctx.send(f"Bye {ctx.author.name}")

    @commands.command(aliases = ["e"])
    async def echo(self, ctx, *, arg = None):
        if arg == None:
            await ctx.send("Can't send nothing bud")
        else:
            await ctx.send(arg)

    @commands.command()
    async def dm(self, ctx, member:discord.User, *, arg,):
        await member.send(f"**{ctx.author}** says: {arg}")
        await ctx.send("DM sent")

def setup(client):
    client.add_cog(misc(client))