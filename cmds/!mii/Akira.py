import discord
from discord.ui import Button
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Akira


class miiAkira(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def mii_Akira(self, ctx):
        button = Button(label='Next', style=discord.ButtonStyle)
        embed_Akira = discord.Embed()
        embed_Akira.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        embed_Akira.add_field(name='Name:', value='Akira')
        embed_Akira.add_field(
            name='Face properties:',
            value='Skin tone: \n  Column 1 row 1 \n\n\nFace shape: \n Column 3 row 1 \n\n\nMakeup: \n  None \n\n\n Face lines: \n  Column 4 row 1 ',
        )
        embed_Akira.add_field(
            name='Hair properties:',
            value='Hair style: \n Column 2 row 1 \n\n\nHair color: \n Black ',
        )
        embed_Akira.add_field(
            name='Eyebrow properties:',
            value='Eyebrow style: \n Column 6 row 3 \n\n\n\nEyebrow color: \n Black \n\n\n Eyebrow proportions: \n Rotate 1 clockwise, smaller by 1, move up by 2 ',
        )
        embed_Akira.add_field(
            name='Eye properties:',
            value='Eye style: \n Pg 1, Column 6 row 1 \n\n\n\nEye color: \n Default \n\n\n Eye proportions: \n Smaller by 2, moved apart by 1, moved down 1  ',
        )
        embed_Akira.add_field(
            name='Nose propertes:',
            value='Nose style: \n Column 5 row 1 \n\n\n\nNose proportions: \n Moved down by 1 ',
        )
        embed_Akira.add_field(
            name='Mouth properties:',
            value='Mouth style: \n  Column 3 row 2 \n\n\nMouth proportions: \n Smaller by 2, moved down by 3 ',
        )
        embed_Akira.add_field(
            name='Facial hair:',
            value='Beard style: \n  Column 3 row 1 \n\n\n Mustache Style: Column 3 row 1 \n\n\nMustache proportions: \nMove 1 down, smaller by 1 \n\n\n Facial hair color: \n  Default ',
        )
        embed_Akira.add_field(name='Mole:', value='Mole: \n  None')
        embed_Akira.add_field(
            name='Glasses:',
            value='Glasses style: \n  Column 5 row 3 \n\n\n Glasses placement:  Smaller by 1, moved down by 2 \n\n\n Glasses color: \n  Column 3 row 1',
        )
        embed_Akira.add_field(name='Gender', value='Male')
        embed_Akira.add_field(name='Favorite color:', value='Brown')
        embed_Akira.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87'
        )
        embed_Akira.set_image(
            url='https://cdn.discordapp.com/attachments/972159228573798440/989188293092585482/68747470733a2f2f-7066326d2e636f6d_2.png'
        )
        await ctx.send(embed=embed_Akira)


async def setup(client):
    await client.add_cog(miiAkira(client))
