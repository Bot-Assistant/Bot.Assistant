import os

from settings.settingColors import *

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

from addons.soundplay.settings.settingAddon import *

async def folderCreate(ctx, directory):

    # Folder where the sounds are located
    folder = defaultSoundFolder

    selectedFolder = folder + str(ctx.guild.id) + "/"  + directory + "/"
    

    # If the folder already exists, send a message
    if os.path.exists(selectedFolder) == True:
        embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="This folder already exists", color=red)
        await ctx.respond(embed=embed)
        return

    # Create the folder
    os.mkdir(selectedFolder)

    # Create the embed
    embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="Folder created", color=green)
    await ctx.respond(embed=embed)