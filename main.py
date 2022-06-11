import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('!helpmii'))


f = []

for file in os.listdir('./cmds'):
    if file.endswith('.py'):
        f.append("cmds." + file[:-3])

if __name__ == '__main__':
    for e in f:
        client.load_extension(e)


client.run(TOKEN)
