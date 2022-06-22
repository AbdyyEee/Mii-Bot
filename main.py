import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


cmds = []

class Mii_Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!', 
            intents=discord.Intents.all()
        )

        for file in os.listdir('cmds\!mii'):
            if file.endswith('.py'):
                cmds.append(f'cmds.!mii.{file[:-3]}')

    async def setup_hook(self):
        for file in cmds:
            await self.load_extension(file)

    async def on_ready(self):
        await self.wait_until_ready()
        await client.change_presence(activity=discord.Game('!helpmii'))
        print('Bot is logged in... ')


load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
client = Mii_Bot()
client.run(TOKEN)
