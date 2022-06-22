import discord
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Default Female


class mii_Default_Female(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mii_Default_f(self, ctx):
        embed_default_f = discord.Embed()
        embed_default_f.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed_default_f.add_field(name='Name:', value='Default Female')
        embed_default_f.add_field(
            name='Face properties:',
            value='Skin tone: \n Default \n\n\nFace shape: \n Default \n\n\nMakeup: \n None \n\n\n Face lines: \n None ',
        )
        embed_default_f.add_field(
            name='Hair properties:',
            value='Hair style: \n Default \n\n\nHair color: \n Brown ',
        )
        embed_default_f.add_field(
            name='Eyebrow properties:',
            value='Eyebrow style: \n Default \n\n\n\nEyebrow color: \n Brown \n\n\n\n Eyebrow proportions: \n Default ',
        )
        embed_default_f.add_field(
            name='Eye properties:',
            value='Eye style: \n Default \n\n\n\nEye color: \n Black \n\n\n\n Eye proportions: \n Default',
        )
        embed_default_f.add_field(
            name='Nose propertes:',
            value='Nose style: \n Default \n\n\n\nNose proportions: \n default ',
        )
        embed_default_f.add_field(
            name='Mouth properties:',
            value='Mouth style: \n Default \n\n\nMouth proportions: \n Default ',
        )
        embed_default_f.add_field(name='Facial hair:', value='None')
        embed_default_f.add_field(name='Mole:', value='Mole: \n None')
        embed_default_f.add_field(name='Glasses:', value='None')
        embed_default_f.add_field(name='Gender', value='Male')
        embed_default_f.add_field(name='Favorite color:', value='Red')
        embed_default_f.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87'
        )
        embed_default_f.set_image(
            url='https://cdn-mii.accounts.nintendo.com/2.0.0/miis/f80f4722e7022c74/image/68747470733a2f2f-7066326d2e636f6d.png?type=face&expression=normal&width=270&bgColor=FFFFFF00&clothesColor=default&cameraXRotate=0&cameraYRotate=0&cameraZRotate=0&characterXRotate=0&characterYRotate=0&characterZRotate=0&lightDirectionMode=none&instanceCount=1&instanceRotationMode=model'
        )
        await ctx.send(embed=embed_default_f)


async def setup(client):
    await client.add_cog(mii_Default_Female(client))
