import discord 
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Daisuke

class miiDaisuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mii_Daisuke(self, ctx):
        embed_Daisuke = discord.Embed()
        embed_Daisuke.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed_Daisuke.add_field(name='Name:', value='Daisuke')
        embed_Daisuke.add_field(name='Face properties:', value='Skin tone: \n  Column 1 row 3 \n\n\nFace shape: \n Column 4 row 1 \n\n\nMakeup: \n  None \n\n\n Face lines: \n  Column 2 row 4 ')
        embed_Daisuke.add_field(name='Hair properties:', value='Hair style: \n Column 2 row 1 \n\n\nHair color: \n Brown ')
        embed_Daisuke.add_field(name='Eyebrow properties:', value='Eyebrow style: \n Column 2 row 2 \n\n\nEyebrow color: \n Brown \n\n\n Eyebrow proportions: \n Rotate 1 clockwise, decrease size by 2, move farther apart by 1, move upwards by 5 ')
        embed_Daisuke.add_field(name='Eye properties:', value='Eye style: \n Pg 2, column 2 row 2 \n\n\nEye color: \n Black \n\n\n Eye proportions: \n Rotate 1 clockwise, Smaller by 2, Farther apart by 3, Move upwards by 3')
        embed_Daisuke.add_field(name='Nose propertes:', value='Nose style: \n Column 3 row 2 \n\n\nNose proportions: \nIncrease size by 1, move upwards by 2 ')
        embed_Daisuke.add_field(name='Mouth properties:', value='Mouth style: \n Column 4 row 1 \n\n\nMouth proportions: \n Increase size by 1 ')
        embed_Daisuke.add_field(name='Facial hair:', value='Facial hair style: \n Column 3 row 1 \n\n\nFacial hair proportions: \n Default \n\n\n Facial hair color: \n Brown ')
        embed_Daisuke.add_field(name='Mole:', value='None')
        embed_Daisuke.add_field(name='Glasses:', value='Glasses style: \n Column 4 row 1 \n\n\n Glasses placement: Move up 1 \n\n\n Glasses color: \n Column 2 row 2')
        embed_Daisuke.add_field(name='Gender', value='Male')
        embed_Daisuke.add_field(name='Favorite color:', value='Light blue')
        embed_Daisuke.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
        embed_Daisuke.set_image(url='https://cdn.discordapp.com/attachments/760119885996097560/966743759805112320/68747470733a2f2f-7066326d2e636f6d_10.png')
        await ctx.send(embed=embed_Daisuke)

async def setup(client):
    await client.add_cog(miiDaisuke(client))
