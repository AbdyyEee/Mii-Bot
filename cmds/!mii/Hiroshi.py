import discord
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Hiroshi


class miiHiroshi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mii_Hiroshi(self, ctx):
        embed_Hiroshi = discord.Embed(color=0x7328AD)
        embed_Hiroshi.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed_Hiroshi.add_field(name='Name:', value='Hiroshi')
        embed_Hiroshi.add_field(
            name='Face properties:',
            value='Skin tone: \n  Column 4, row 1 \n\n\nFace shape: \n Column 2, row 3 \n\n\nMakeup: \n  None \n\n\n Face lines: \n  Column 3, row 1 ',
        )
        embed_Hiroshi.add_field(
            name='Hair properties:',
            value='Hair style: \n 2nd page, column 3, row 5  \n\n\nHair color: \n Black ',
        )
        embed_Hiroshi.add_field(
            name='Eyebrow properties:',
            value='Eyebrow style: \n Column 1, row 2 \n\n\n\nEyebrow color: \n Black \n\n\n Eyebrow proportions: \n Rotate 1 clockwise ',
        )
        embed_Hiroshi.add_field(
            name='Eye properties:',
            value='Eye style: \n Page 2, column 2, row 2 \n\n\nEye color: \n Black \n\n\n Eye proportions: \n Rotate 1 clockwise, 2 smaller, move apart by 3',
        )
        embed_Hiroshi.add_field(
            name='Nose propertes:',
            value='Nose style: \n Column 5, row 2 \n\n\n\nNose proportions: Increase size by 1, move down by 1 ',
        )
        embed_Hiroshi.add_field(
            name='Mouth properties:',
            value='Mouth style: \n  Column 1, row 2 \n\n\nMouth proportions: \n Increase size by 4, move down 3 ',
        )
        embed_Hiroshi.add_field(
            name='Facial hair:',
            value='Facial hair style: \n  None \n\n\nFacial hair proportions: \n  None \n\n\n Facial hair color: \n  None ',
        )
        embed_Hiroshi.add_field(name='Mole:', value='Mole: \n  None')
        embed_Hiroshi.add_field(
            name='Glasses:',
            value='Glasses style: \n  Column 4, row 3 \n\n\n Glasses placement: Smaller by 1 \n\n\n Glasses color: \n  Column 10, row 9',
        )
        embed_Hiroshi.add_field(name='Gender', value='Male')
        embed_Hiroshi.add_field(name='Favorite color:', value='Purple')
        embed_Hiroshi.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87'
        )
        embed_Hiroshi.set_image(
            url='https://cdn.discordapp.com/attachments/760119885996097560/966692296387100752/68747470733a2f2f-7066326d2e636f6d_9.png'
        )
        await ctx.send(embed=embed_Hiroshi)


def setup(client):
    client.add_cog(miiHiroshi(client))
