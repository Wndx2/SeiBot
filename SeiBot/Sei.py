"""WELCOME TO SEIBOT, A VIRTUAL FISHING BOT INSIDE DISCORD."""

# STABLE CODE,
# CREATED ON 23:00, 21ST OF DECEMBER, 2024.

import discord
import platform
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"\nSuccessfully logged in as {bot.user}\nCurrently running: SeiBot.v1")
    print(f"Running on: {platform.system()} {platform.release()} ({platform.machine()})\n\n\n")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

bot.run('TOKEN')
