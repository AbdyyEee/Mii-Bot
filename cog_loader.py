import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


cog_commands = []

class mii_bot(commands.Bot):
    """Class for loading cogs in the cmds dir:"""
    def __init__(self):
        super().__init__(
            command_prefix='!', 
            intents=discord.Intents.all()
        )

        for file in os.listdir('mii_bot/!wii_mii'):
            if file.endswith('.py'):
                cog_commands.append(f'mii_bot.!wii_mii.{file[:-3]}')

    async def setup_hook(self):
        for file in cog_commands:
            await self.load_extension(file)

    async def on_ready(self):
        await self.wait_until_ready()
        await client.change_presence(activity=discord.Game('!helpmii'))
        print('Bot is logged in ')

# Bot loading
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
client = mii_bot()
client.run(TOKEN)
