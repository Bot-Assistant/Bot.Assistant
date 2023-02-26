import os

from settings.settingColors import *

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

from addons.soundplay.settings.settingAddon import *
import addons.soundplay.handlers.handlerSoundsList as handlerSoundsList

async def soundDelete(ctx, directory, sound):
    # Folder where the sounds are located
    folder = defaultSoundFolder

    selectedFolder = folder + str(ctx.interaction.guild_id) + "/" + directory + "/"

    # If the folder already exists, send a message
    if os.path.exists(selectedFolder) == False:
        embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="This folder doesn't exist", color=red)
        await ctx.respond(embed=embed)
        return

    # If the sound doesn't exist, send a message
    if os.path.exists(selectedFolder + sound) == False:
        embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="This sound doesn't exist", color=red)
        await ctx.respond(embed=embed)
        return

    # Delete the sound
    os.remove(selectedFolder + sound)

    # Delete the sound from the database
    handlerSoundsList.removeSound(ctx.guild.id, directory, sound)

    # Create the embed
    embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="Sound deleted", color=green)
    await ctx.respond(embed=embed)