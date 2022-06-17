import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Mii-Bot is ready.')
    await client.change_presence(activity=discord.Game('!helpmii'))

# !mii_name command
for file in os.listdir('cmds\!mii'):
    if file.endswith('.py'):
        client.load_extension(f'cmds.!mii.{file[:-3]}')

client.run(TOKEN)
