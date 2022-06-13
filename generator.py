# *-*-Mii Embed Generator-*-*
# Version: --> 1.2.0

import os

options = ['None', 'No', 'none', 'no']

print(
"""
*-*-Mii Embed Generator-*-*
Version 1.1.0
---------------------------
This program is made for generating a .py file for creating embeds of Miis
I would really appreciate any contributions to this script, or the bot itself. 

*-*-Instructions-*-*
---------------------------
When inputting Mii proportions or styles that are default, enter "Default".
If there is a selectable option that is not applicable to the Mii, enter "None." (example: Facial hair, glasses, etc)
Otherwise, input the proper proportions or style of said Mii.
For proportions, I reccomend typing "Moved up by {number}", "Stretched thinner/upwards by {number}", "Moved farther/closer apart by {number} etc.
You can also refer to existing Miis for how to phrase proportions.
FOR SWITCH ONLY:
To phrase options such as eyebrows, hair, skin tone, etc, reference the Column and row they are on. If the option is on a different page, specify the page first.

*-*-Images-*-*
---------------------------
You will need an image for an embed so this is how you get one.
Make a Mii on Mii Studio, save it and input it into Mii Renderer.
Right click the Mii, and copy the image as link. 
Paste the link when necessary 
"""
)

name = input('What is the Mii name? ')
gender = input('Gender? ')
color = input('Favorite color? (Names: Red, orange, yellow, light green, dark green, dark blue, light blue, pink, purple, brown, white, black. ')
skin = input('What is the skin tone of the Mii.')
face_shape = input('Face shape? ')
makeup = input('Makeup? (Input none if answer is no)')
face_lines = input('Facelines? (Input none if answer is no)')
hair = input('Hair style? ')
hair_color = input('Input the Mii Hair color? ')
eyebrow = input('Input the Eyebrow style? ')
eyebrow_color = input('Input the Mii Eyebrow color ')
eyebrow_p = input('Input the Eyebrow proportions? ')
eye = input('Eye style? ')
eye_color = input('What is the Eye color of the Mii? ')
eye_p = input('Eye proportions? ')
nose = input('What is the Nose style? ')
nose_p = input('Nose properties? ')
mouth = input('Input the Mouth style?')
mouth_p = input('Input the Mouth propotions ')
facial_hair = input('Facial hair? (Input none if answer is no)')
facial_hair_p = input('Facial hair position? (Input none if previous answer was none.)')
facial_hair_color = input('Facial hair color? (Click enter if previous answer was none.)')
mole_p = input('Mole? Size and position? (Input none if answer is no)')
glasses = input('Glasses? (Input none if answer is no)')
glasses_p = input('Glasses position? (Click enter if previous answer was none.)')
glasses_color = input('Glasses color? (Click enter if previous answer was none.)')
image = input('Enter the Mii image url. ')

# F strings are a blessing
embed = f"""import discord 
from discord.ext import commands

# Code generated with "Mii embed generator."
# Mii: {name}

class mii{name}(commands.Cog):
    def __init__(self, bot):
    self.bot = bot

    @commands.command()
    async def mii_{name}(self, ctx):
    \tembed_{name} = discord.Embed()
    \tembed_{name}.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    \tembed_{name}.add_field(name='Name:', value='{name}')
    \tembed_{name}.add_field(name='Face properties:', value='Skin tone: \\n {skin} \\n\\nFace shape: \\n {face_shape} \\n\\nMakeup: \\n {makeup} \\n\\n Face lines: \\n {face_lines} ')
    \tembed_{name}.add_field(name='Hair properties:', value='Hair style: \\n {hair} \\n\\nHair color: \\n {hair_color} ')
    \tembed_{name}.add_field(name='Eyebrow properties:', value='Eyebrow style: \\n {eyebrow} \\n\\n\\nEyebrow color: \\n {eyebrow_color} \\n\\n Eyebrow proportions: \\n {eyebrow_p} ')
    \tembed_{name}.add_field(name='Eye properties:', value='Eye style: \\n\\n {eye} \\n\\nEye color: \\n {eye_color} \\n\\n Eye proportions: \\n {eye_p}')
    \tembed_{name}.add_field(name='Nose propertes:', value='Nose style: \\n {nose} \\n\\n\\nNose proportions: \\n\\n {nose_p} ')
    \tembed_{name}.add_field(name='Mouth properties:', value='Mouth style: \\n {mouth} \\n\\nMouth proportions: \\n {mouth_p} ')
    \tembed_{name}.add_field(name='Facial hair:', value='Facial hair style: \\n {facial_hair} \\n\\nFacial hair proportions: \\n {facial_hair_p} \\n\\n Facial hair color: \\n {facial_hair_color} ')
    \tembed_{name}.add_field(name='Mole:', value='Mole: \\n {mole_p}')
    \tembed_{name}.add_field(name='Glasses:', value='Glasses style: \\n {glasses} \n\\n Glasses placement: {glasses_p} \\n\\n Glasses color: \\n {glasses_color}')
    \tembed_{name}.add_field(name='Gender', value='{gender}')
    \tembed_{name}.add_field(name='Favorite color:', value='{color}')
    \tembed_{name}.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
    \tembed_{name}.set_image(url='{image}')
    \tawait ctx.send(embed=embed_{name})

def setup(client):
    client.add_cog(mii{name}(client))
"""

def remove(string, replace_char):
    if glasses in options:
        
        embed = string.replace(
            f'Glasses style: \\n {glasses} \n\\n Glasses placement: {glasses_p} \\n\\n Glasses color: \\n {glasses_color}',
            replace_char
        )
        
    elif makeup in options:
        embed = string.replace(f'\\n\\nMakeup: \\n {makeup}', replace_char)
        
    elif face_lines in options:
        embed = string.replace(f'\\n\\n Face lines: \\n {face_lines}', replace_char)
                               
    elif facial_hair in options:
        embed = string.replace(f'Facial hair style: \\n {facial_hair} \\n\\nFacial hair proportions: \\n {facial_hair_p} \\n\\n Facial hair color: \\n {facial_hair_color}', replace_char)
      
    elif mole_p in options:
        embed = string.replace(f'Mole: \\n {mole_p}', replace_char)
        
    else:
         embed = string
            
    return embed


n_embed = remove(embed, 'None')


if os.path.isfile(f'{name}.py'):
    os.remove(f'{name}.py')
file = open(f'{name}.py', 'x')
file.write(n_embed)
file.close()
print('File written! Check the directory where you ran this script. ')
print('If you want to do another Mii, rerun the script/exe.')
keep_alive = input('')
