import discord
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Saburo


class miiSaburo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mii_Saburo(self, ctx):
        embed_Saburo = discord.Embed()
        embed_Saburo.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed_Saburo.add_field(name='Name:', value='Saburo')
        embed_Saburo.add_field(
            name='Face properties:',
            value='Skin tone: \n  Column 3, row 1 \n\n\nFace shape: \n Column 4, row 1 \n\n\nMakeup: \n  None \n\n\n Face lines: \n  Column 3, row 1 ',
        )
        embed_Saburo.add_field(
            name='Hair properties:',
            value='Hair style: \n 1st pg, column 4, row 3 \n\n\nHair color: \n Black ',
        )
        embed_Saburo.add_field(
            name='Eyebrow properties:',
            value='Eyebrow style: \n Column 1, row 1 \n\n\nEyebrow color: \n Black \n\n\n Eyebrow proportions: \n Rotate 1 clockwise, smaller by 1, move down by 2 ',
        )
        embed_Saburo.add_field(
            name='Eye properties:',
            value='Eye style: \n Pg 1, column 4 row 5 \n\n\nEye color: \n Black \n\n\n Eye proportions: \n Rotate 1 clockwise, smaller by 2, farther apart by 1, moved up by 1',
        )
        embed_Saburo.add_field(
            name='Nose propertes:',
            value='Nose style: \n Column 5, row 1 \n\n\nNose proportions: \n Moved up by 1 ',
        )
        embed_Saburo.add_field(
            name='Mouth properties:',
            value='Mouth style: \n Column 6, row 4 \n\n\nMouth proportions: \n Smaller by 1 ',
        )
        embed_Saburo.add_field(
            name='Facial hair:',
            value='Beard: \n Column 2, row 1 \n\n\nFacial hair proportions: \n Default \n\n\n Facial hair color: \n Black ',
        )
        embed_Saburo.add_field(name='Mole:', value='Mole: \n None')
        embed_Saburo.add_field(
            name='Glasses:',
            value='Glasses style: \n None \n Glasses placement: None \n\n\n Glasses color: \n None',
        )
        embed_Saburo.add_field(name='Gender', value='Male')
        embed_Saburo.add_field(name='Favorite color:', value='Dark blue')
        embed_Saburo.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87'
        )
        embed_Saburo.set_image(
            url='https://cdn.discordapp.com/attachments/760119885996097560/966684424848695386/68747470733a2f2f-7066326d2e636f6d_8.png'
        )
        await ctx.send(embed=embed_Saburo)


async def setup(client):
    await client.add_cog(miiSaburo(client))
