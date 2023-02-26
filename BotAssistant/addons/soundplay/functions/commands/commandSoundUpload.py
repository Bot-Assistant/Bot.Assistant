import os

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

from addons.soundplay.settings.settingAddon import *
import addons.soundplay.handlers.handlerSoundsList as handlerSoundsList

from settings.settingColors import *

async def upload(ctx, directory, sound):

    # Folder where the sounds are located
    folder = defaultSoundFolder

    selectedFolder = folder + directory + "/"

    # If the folder already exists, send a message
    if os.path.exists(selectedFolder) == False:
        embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="This folder doesn't exist", color=red)
        await ctx.respond(embed=embed)
        return

    # Save the sound in the folder
    await sound.save(selectedFolder + sound.filename)

    # Add the sound to the database
    handlerSoundsList.addSound(ctx.guild.id, directory, sound.filename, 0)

    # Create the embed
    embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="Sound uploaded", color=green)
    await ctx.respond(embed=embed)