import discord
from discord.ext import commands
import os
from discord.ext.commands.bot import when_mentioned_or
from discord.ext.commands.errors import CommandOnCooldown
from dotenv import load_dotenv

# bot status
activity = discord.Activity(name="Zenoku fail at coding", type=discord.ActivityType.watching)

# regular bot stuff
client = commands.Bot(command_prefix=when_mentioned_or("z.", "Z."), case_insensitive=True, activity = activity) 
client.load_extension('jishaku')
# client.remove_command("help")

# .env stuff
load_dotenv()
Token = os.getenv("Token")

# loading events
@client.event
async def on_connect():
    print("Zenbot is connected to Discord")

@client.event
async def on_ready():
    print("Zenbot is ready")
    print(f"Discord.py Version: {discord.__version__}")


# error msges
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing something bud")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't exist")
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send("That command has been disabled")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("That command isn't for you")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You're missing {error.missing_perms} to use that command")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(f"I am missing {error.missing_perms} to use that command")        
    else:
        log_channel = client.get_channel(845671875626795008)
        await log_channel.send(f"Error encountered by: **{ctx.author}**\nMessage id: {ctx.message.jump_url}\n{error}")


"""
work on embeds and stuff. also uncomment remove(help) above when done

@client.command()
async def help(ctx):
    await ctx.send("Work In Progress, commands are hi, bye, and feedback for now")
"""

# loading cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(Token)