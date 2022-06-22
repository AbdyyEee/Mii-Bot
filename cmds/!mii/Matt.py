import discord
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Matt


class miiMatt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mii_Matt(self, ctx):
        embed_Matt = discord.Embed(color=0xFF6E19)
        embed_Matt.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed_Matt.add_field(name='Name:', value='Matt')
        embed_Matt.add_field(
            name='Face properties:',
            value='Skin tone: \n  Column 4, row 1 \n\n\nFace shape: \n Column 4, row 4 \n\n\nMakeup: \n  None \n\n\n Face lines: \n  None ',
        )
        embed_Matt.add_field(
            name='Hair properties:',
            value='Hair style: \n Page 2, Column 6, row 5 \n\n\nHair color: \n None ',
        )
        embed_Matt.add_field(
            name='Eyebrow properties:',
            value='Eyebrow style: \n Column 5, row 1 \n\n\n\nEyebrow color: \n Black \n\n\n Eyebrow proportions: \n Move down by 4, rotate counter clock-wise by 2 ',
        )
        embed_Matt.add_field(
            name='Eye properties:',
            value='Eye style: \n Page 2, column 2, row 5 \n\n\nEye color: \n Black \n\n\n Eye proportions: \n Move down by 2, move farther by 2, smaller by 1',
        )
        embed_Matt.add_field(
            name='Nose propertes:',
            value='Nose style: \n Column 4, row 1 \nNose proportions: \n\n\n Move down by 2, increase size by 1 ',
        )
        embed_Matt.add_field(
            name='Mouth properties:',
            value='Mouth style: \n  Column 2, row 2 \n\n\nMouth proportions: \n Moved down by 2 ',
        )
        embed_Matt.add_field(
            name='Facial hair:',
            value='Facial hair style: \n Mustache: Column 1, row 2 Beard: Column 3, row 1 \n\n\nFacial hair proportions: \n  Increase size by 2, move down by  \n\n\n Facial hair color: \n  Black ',
        )
        embed_Matt.add_field(name='Mole:', value='Mole: \n  None')
        embed_Matt.add_field(
            name='Glasses:',
            value='Glasses style: \n  None \n Glasses placement:  None \n\n\n Glasses color: \n  None',
        )
        embed_Matt.add_field(name='Gender', value='Male')
        embed_Matt.add_field(name='Favorite color:', value='Orange')
        embed_Matt.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87'
        )
        embed_Matt.set_image(
            url='https://media.discordapp.net/attachments/800680039272284200/966048898089091143/68747470733a2f2f-7066326d2e636f6d_53.png?width=243&height=243'
        )
        await ctx.send(embed=embed_Matt)


async def setup(client):
    await client.add_cog(miiMatt(client))
