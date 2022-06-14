import discord 
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: Default Male

class miiDefault Male(commands.Cog):
    def __init__(self, bot):
    self.bot = bot

    @commands.command()
    async def mii_Default_m(self, ctx):
    	embed_Default_Male = discord.Embed()
    	embed_Default_Male.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    	embed_Default_Male.add_field(name='Name:', value='Default Male')
    	embed_Default_Male.add_field(name='Face properties:', value='Skin tone: \n Default \n\nFace shape: \n Default \n\nMakeup: \n None \n\n Face lines: \n None ')
    	embed_Default_Male.add_field(name='Hair properties:', value='Hair style: \n Default \n\nHair color: \n Brown ')
    	embed_Default_Male.add_field(name='Eyebrow properties:', value='Eyebrow style: \n Default \n\n\nEyebrow color: \n Brown \n\n Eyebrow proportions: \n Default ')
    	embed_Default_Male.add_field(name='Eye properties:', value='Eye style: \n\n Default \n\nEye color: \n Black \n\n Eye proportions: \n Default')
    	embed_Default_Male.add_field(name='Nose propertes:', value='Nose style: \n Default \n\n\nNose proportions: \n\n default ')
    	embed_Default_Male.add_field(name='Mouth properties:', value='Mouth style: \n Default \n\nMouth proportions: \n Default ')
    	embed_Default_Male.add_field(name='Facial hair:', value='Facial hair style: \n None \n\nFacial hair proportions: \n None \n\n Facial hair color: \n None')
    	embed_Default_Male.add_field(name='Mole:', value='Mole: \n None')
    	embed_Default_Male.add_field(name='Glasses:', value='None')
    	embed_Default_Male.add_field(name='Gender', value='Male')
    	embed_Default_Male.add_field(name='Favorite color:', value='Red')
    	embed_Default_Male.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
    	embed_Default_Male.set_image(url='https://cdn-mii.accounts.nintendo.com/2.0.0/miis/a82494580d52e0fc/image/68747470733a2f2f-7066326d2e636f6d.png?type=face&expression=normal&width=270&bgColor=FFFFFF00&clothesColor=default&cameraXRotate=0&cameraYRotate=0&cameraZRotate=0&characterXRotate=0&characterYRotate=0&characterZRotate=0&lightDirectionMode=none&instanceCount=1&instanceRotationMode=model')
    	await ctx.send(embed=embed_Default_Male)

def setup(client):
    client.add_cog(mii_Defualt_Male(client))
