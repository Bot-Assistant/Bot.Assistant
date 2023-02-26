import os

from settings.settingColors import *

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

from addons.soundplay.settings.settingAddon import *
import addons.soundplay.handlers.handlerSoundsList as handlerSoundsList

async def folderDelete(ctx, directory):

    # Folder where the sounds are located
    folder = defaultSoundFolder

    selectedFolder = folder + str(ctx.guild.id) + "/"+ directory + "/"
    print(selectedFolder)

    # If the folder already exists, send a message
    if os.path.exists(selectedFolder) == False:
        embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="This folder doesn't exist", color=red)
        await ctx.respond(embed=embed)
        return

    # Embed deleting folder
    embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="Deleting folder...", color=green)
    interaction = await ctx.respond(embed=embed)

    # Delete all sounds in the folder from the database
    for sound in os.listdir(selectedFolder):
        # Delete the sound from the database
        handlerSoundsList.removeSound(ctx.guild.id, directory, sound)

        # Delete the sound
        os.remove(selectedFolder + sound)
    
    # Delete the folder
    os.rmdir(selectedFolder)

    # Update the embed
    embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="Folder deleted", color=green)
    await interaction.edit_original_response(embed=embed)
