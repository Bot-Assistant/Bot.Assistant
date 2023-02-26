# Settings
from addons.soundplay.settings.settingAddon import *

# Init BotAssistant
import services.serviceBot as serviceBot
bot = serviceBot.classBot.getBot()

async def onVoiceStateUpdate(member, before, after):
    if member != bot.user:
        return
    
    if before.channel is None:
        return
    
    if bot.user in before.channel.members:
        if len(before.channel.members) == 1:
            if before.channel.guild.voice_client is not None:
                before.channel.guild.voice_client.stop()
            await before.channel.guild.voice_client.disconnect()