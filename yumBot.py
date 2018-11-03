import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#clientid: 507270757668356096
#token: NTA3MjcwNzU3NjY4MzU2MDk2.DruRQg.76Wc2qGpsp-NT3-AdoOj0gBf4Cc

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Welcome !!!')
    print('Name: ' + bot.user.name)
    print('Client ID: ' + bot.user.id)
    print('------------------------------------------')


bot.run("NTA3MjcwNzU3NjY4MzU2MDk2.DruRQg.76Wc2qGpsp-NT3-AdoOj0gBf4Cc")

