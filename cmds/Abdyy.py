import discord
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Abdyy
# This is an example Mii


class Abdyy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mii_Abdyy(self, ctx):
        embed_Abdyy = discord.Embed()
        embed_Abdyy.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed_Abdyy.add_field(name='Name:', value='Abdyy')
        embed_Abdyy.add_field(
            name='Face properties:',
            value='Skin tone: \n Row 1, Column. \n\nFace shape: \n Default \n\nMakeup: \n None. \n\n Face lines: \n None. ',
        )
        embed_Abdyy.add_field(
            name='Hair properties:',
            value='Hair style: \n 2nd page, row 1, column 3. \n\nHair color: \n Default. ',
        )
        embed_Abdyy.add_field(
            name='Eyebrow properties:',
            value='Eyebrow style: \n Row 1, column 3. \n\n\nEyebrow color: \n  Default. \n\n Eyebrow proportions: \n Rotate left by 1, move down by 1, decrease size by 1, stretched thinner by 2, moved apart by 2. ',
        )
        embed_Abdyy.add_field(
            name='Eye properties:',
            value='Eye style: \n 2nd page, row 4, column 2. \n\nEye color: \n  Dark Brown. \n\n Eye proportions: \n Rotate 1 right, move downwards by 3, stretched upwards by 2.',
        )
        embed_Abdyy.add_field(
            name='Nose propertes:',
            value='Nose style: \n Default. \n\n\nNose proportions: \n Smaller by 2, move down by 3. ',
        )
        embed_Abdyy.add_field(
            name='Mouth properties:',
            value='Mouth style: \n Row 3, column 5. \n\nMouth proportions: \n Smaller by 1, stretched thinner by 2. ',
        )
        embed_Abdyy.add_field(
            name='Facial hair:',
            value='Facial hair style: \n  None. \n\nFacial hair proportions: \n  None. \n\n Facial hair color: \n  None. ',
        )
        embed_Abdyy.add_field(
            name='Mole:',
            value='Mole style and position: \n  Move 11 to the right, 3 down, decrease size by 3.',
        )
        embed_Abdyy.add_field(
            name='Glasses:',
            value='Glasses style: \n  None. \n\nGlasses proportions:  None. \n\n Glasses color: \n None. ',
        )
        embed_Abdyy.add_field(name='Gender', value='Male')
        embed_Abdyy.add_field(name='Favorite color:', value='Dark Blue')
        embed_Abdyy.set_thumbnail(
            url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87'
        )
        embed_Abdyy.set_image(
            url='https://cdn-mii.accounts.nintendo.com/2.0.0/miis/83d4e4faf441c59d/image/68747470733a2f2f-7066326d2e636f6d.png?type=face&expression=normal&width=270&bgColor=FFFFFF00&clothesColor=default&cameraXRotate=0&cameraYRotate=0&cameraZRotate=0&characterXRotate=0&characterYRotate=0&characterZRotate=0&lightDirectionMode=none&instanceCount=1&instanceRotationMode=model'
        )
        await ctx.send(embed=embed_Abdyy)


def setup(client):
    client.add_cog(Abdyy(client))
