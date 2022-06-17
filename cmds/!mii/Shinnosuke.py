import discord
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Shinnosuke


class miiShinnosuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mii_Shinnosuke(self, ctx):
        embed_Shinnosuke = discord.Embed()
        embed_Shinnosuke.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed_Shinnosuke.add_field(name='Name:', value='Shinnosuke')
        embed_Shinnosuke.add_field(
            name='Face properties:',
            value='Skin tone: \n  Column 3, row 1 \n\n\nFace shape: \n Column 3, row 2 \n\nMakeup: \n  None \n\n Face lines: \n  Column 2, row 3 ',
        )
        embed_Shinnosuke.add_field(
            name='Hair properties:',
            value='Hair style: \n Page 4, column 3, row 1 \n\nHair color: \n Black ',
        )
        embed_Shinnosuke.add_field(
            name='Eyebrow properties:',
            value='Eyebrow style: \n Column 6, row 1 \n\n\nEyebrow color: \n Black \n\n Eyebrow proportions: \n Smaller by 1, move up by 2 ',
        )
        embed_Shinnosuke.add_field(
            name='Eye properties:',
            value='Eye style: \n Column 4, row 1 \n\n\nEye color: \n Black \n\n Eye proportions: \n Rotate 3 counterclockwise ',
        )
        embed_Shinnosuke.add_field(
            name='Nose propertes:',
            value='Nose style: \n Column 5, row 1 \n\n\nNose proportions: \nMove up by 2 ',
        )
        embed_Shinnosuke.add_field(
            name='Mouth properties:',
            value='Mouth style: \n  Column 4, row 3 \n\n\nMouth proportions: \n Increase size by 2, move up by 1 ',
        )
        embed_Shinnosuke.add_field(
            name='Facial hair:',
            value='Facial hair style: \n  Beard: Column 2, row 1 \n\nFacial hair proportions: \n Default \n\n Facial hair color: \n  Black ',
        )
        embed_Shinnosuke.add_field(name='Mole:', value='Mole: \n  None')
        embed_Shinnosuke.add_field(
            name='Glasses:',
            value='Glasses style: \n  Column 4, row 2 \n\n Glasses placement: Increase size by 2, move up by 1 \n\n Glasses color: \n  Column 2, row 2',
        )
        embed_Shinnosuke.add_field(name='Gender', value='Male')
        embed_Shinnosuke.add_field(name='Favorite color:', value='Red')
        embed_Shinnosuke.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87'
        )
        embed_Shinnosuke.set_image(
            url='https://cdn.discordapp.com/attachments/760119885996097560/966744333208416316/68747470733a2f2f-7066326d2e636f6d_2.png'
        )
        await ctx.send(embed=embed_Shinnosuke)


def setup(client):
    client.add_cog(miiShinnosuke(client))
