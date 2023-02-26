import os

# Addons imports

import addons.soundplay.handlers.handlerSoundsList as handlerSoundsList
# Settings
from addons.soundplay.settings.settingAddon import *

# Init BotAssistant
import services.serviceBot as serviceBot
bot = serviceBot.classBot.getBot()

def onReady():
    for guild in bot.guilds:
            if not os.path.exists(defaultSoundFolder):
                os.makedirs(defaultSoundFolder)

            if not os.path.exists(defaultSoundFolder + str(guild.id)):
                os.makedirs(defaultSoundFolder + str(guild.id))
            
            # Get the sounds list from the database
            soundListDatabase = handlerSoundsList.getAllSoundsInfo([guild.id])
            
            # Remove the sounds from the database if they don't exist
            for sound in soundListDatabase:

                # If the folder doesn't exist in the sound folder
                if sound[0] not in os.listdir(defaultSoundFolder + str(guild.id) + "/"):
                    handlerSoundsList.removeSound(guild.id, sound[0], sound[1])
                    continue
                
                # If the sound doesn't exist in the folder
                if sound[1] not in os.listdir(defaultSoundFolder + str(guild.id) + "/" + sound[0] + "/"):
                    handlerSoundsList.removeSound(guild.id, sound[0], sound[1])

            # Verify if all sounds are in the database
            for folder in os.listdir(defaultSoundFolder + str(guild.id) + "/"):
                for sound in os.listdir(defaultSoundFolder + str(guild.id) + "/" + folder + "/"):
                    if sound not in [sound[1] for sound in soundListDatabase if sound[0] == folder]:
                        handlerSoundsList.addSound(guild.id, folder, sound, 0)