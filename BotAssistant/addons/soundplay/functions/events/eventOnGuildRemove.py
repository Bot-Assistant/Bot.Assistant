import os

import addons.soundplay.settings.settingAddon as settingAddon

def onGuildRemove(guild):
    if os.path.exists(settingAddon.defaultSoundFolder + str(guild.id)):
            os.rmdir(settingAddon.defaultSoundFolder + str(guild.id))