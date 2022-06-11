# *-*-Mii Embed Generator-*-*
# Version: --> 1.0.0

import os

print(
    """
*-*-Mii Embed Generator-*-*
 Version 1.0.0
---------------------------
This program is made for generating a .py file for creating embeds of Miis
This auto-generated .py file is meant for contributing to Miibot. 
I would really appreciate any contributions to this script, or the bot itself. 

*-*-Instructions-*-*
---------------------------
When inputting Mii proportions or styles that are default, enter "Default".
If there is a selectable option that is not applicable to the Mii, enter "None." (example: Facial hair, glasses, etc)
Otherwise, input the proper proportions or style of said Mii.
You will need an image for an embed so this is how you get one.
Make a Mii on Mii Studio, save it and input it into Mii Renderer.
Right click the Mii, and copy the image as link. 

"""
)
name = input('What is the Mii name? ')
gender = input('Gender? ')
color = input('Favorite color? ')
skin = input('Skin tone? ')
face_shape = input('Face shape? ')
makeup = input('Makeup? ')
face_lines = input('Facelines?  ')
hair = input('Hair style? ')
hair_color = input('Hair color? ')
eyebrow = input('Eyebrow style? ')
eyebrow_color = input('Eyebrow color')
eyebrow_p = input('Eyebrow proportions? ')
eye = input('Eye style?  ')
eye_color = input('Eye color?')
eye_p = input('Eye proportions ')
nose = input('Nose style? ')
nose_p = input('Nose properties? ')
mouth = input('Mouth style ')
mouth_p = input('Mouth propotions ')
facial_hair = input('Facial hair?')
facial_hair_p = input('Facial hair position?')
facial_hair_color = input('Facial hair color?')
mole_p = input('Mole? Size and position?')
glasses = input('Glasses?')
glasses_p = input('Glasses position?')
glasses_color = input('Glasses color?')
image = input('Enter the Mii image url. ')

# F strings are a blessing
embed = f"""import discord 
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: {name}

class_{name}(commands.Cog):
    def __init__(self, bot):
    self.bot = bot

    @commands.command()
    async def mii_{name}(self, ctx):
    \tembed_{name} = discord.Embed()
    \tembed_{name}.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    \tembed_{name}.add_field(name='Name:', value='{name}')
    \tembed_{name}.add_field(name='Face properties:', value='Skin tone: \\n {skin} \\n\\nFace shape: \\n {face_shape} \\n\\nMakeup: \\n {makeup} \\n\\n, Face lines: \\n {face_lines} ')
    \tembed_{name}.add_field(name='Hair properties:', value='Hair style: \\n {hair} \\n\\nHair color: \\n {hair_color} ')
    \tembed_{name}.add_field(name='Eyebrow properties:', value='Eyebrow style: \\n {eyebrow} \\n\\n\\nEyebrow color: \\n {eyebrow_color} \\n\\n Eyebrow proportions: \\n {eyebrow_p} ')
    \tembed_{name}.add_field(name='Eye properties:', value='Eye style: \\n\\n {eye} \\n\\nEye color: \\n {eye_color} \\n\\n Eye proportions: \\n {eye_p}')
    \tembed_{name}.add_field(name='Nose propertes:', value='Nose style: \\n {nose} \\n\\n\\nNose proportions: \\n\\n {nose_p} ')
    \tembed_{name}.add_field(name='Mouth properties:', value='Mouth style: \\n {mouth} \\n\\nMouth proportions: \\n {mouth_p} ')
    \tembed_{name}.add_field(name='Facial hair:', value='Facial hair style: \\n {facial_hair} \\n\\nFacial hair proportions: \\n {facial_hair_p} \\n\\n Facial hair color: \\n {facial_hair_color} ')
    \tembed_{name}.add_field(name='Mole:', value='Mole style and position: \\n {mole_p}')
    \tembed_{name}.add_field(name='Glasses:', value='Glasses style: \\n {glasses} \n\\n Glasses placement: {glasses_p} \\n\\n Glasses color: \\n {glasses_color}')
    \tembed_{name}.add_field(name='Gender', value='{gender}')
    \tembed_{name}.add_field(name='Favorite color:', value='{color}')
    \tembed_{name}.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
    \tembed_{name}.set_image(url='{image}')

def setup(client):
    client.add_cog(history(client))
"""

options = ['None', 'No', 'none', 'no']


def remove(string):
    if glasses in options:
        embed = string.replace(
            f'Glasses style: \\n {glasses} \n\\n Glasses placement: {glasses_p} \\n\\n Glasses color: \\n {glasses_color}',
            'None',
        )
        # TODO: Add checks for other properties
    return embed


embed = remove(embed)


if os.path.isfile(f'{name}.py'):
    os.remove(f'{name}.py')
file = open(f'{name}.py', 'x')
file.write(embed)
file.close()
print('File written! Check the directory where you ran this script. ')
print('If you want to do another Mii, rerun the script/exe.')
keep_alive = input('')
