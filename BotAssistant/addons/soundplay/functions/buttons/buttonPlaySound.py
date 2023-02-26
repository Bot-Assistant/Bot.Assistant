import os
import contextlib
import addons.soundplay.handlers.handlerSettings as handlerSettings
import addons.soundplay.handlers.handlerSoundsList as handlerSoundsList

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

from addons.soundplay.settings.settingAddon import *

FFMPEG_OPTIONS = {'executable': './addons/soundplay/requirements/ffmpeg.exe'}

class ButtonPlaySound(discord.ui.Button):

    def __init__(self, folder, file):
        super().__init__(label=file, style=discord.ButtonStyle.secondary)
        self.folder = folder
        self.file = file
        self.volume = defaultVolume
        
    async def callback(self, interaction: discord.Interaction):

        # Get the default volume from the database
        databaseVolume = handlerSettings.getVolume(interaction.guild.id, interaction.user.id)
        if databaseVolume == []:
            self.volume = defaultVolume
        else:
            self.volume = databaseVolume[0][0]
        
        # Verify if the user is in a voice channel
        if interaction.user.voice is None:
            await interaction.response.send_message("You are not in a voice channel", ephemeral=True, delete_after=5)
            return
        
        # Verify if the bot is in a voice channel 
        # and if it is in the same voice channel as the user
        if interaction.guild.voice_client is None:
            await interaction.user.voice.channel.connect()
        elif interaction.guild.voice_client.channel != interaction.user.voice.channel:
            await interaction.guild.voice_client.move_to(interaction.user.voice.channel)    
        
        # Verify if the bot is not already playing a sound, if it is, save the volume and stop the sound
        if interaction.guild.voice_client.is_playing():
            self.volume = interaction.guild.voice_client.source.volume
            interaction.guild.voice_client.stop()

        # Verify if ffmpeg is installed
        if not os.path.isfile(FFMPEG_OPTIONS["executable"]):
            await interaction.response.send_message("FFmpeg is not installed", ephemeral=True, delete_after=5)
            return

        # Add 1 to the number of times the sound has been played
        folder = self.folder.replace(".", "")
        folder = folder.split("/")

        playCountDatabase = handlerSoundsList.getAllSoundsInfo([interaction.guild.id])
        for sound in playCountDatabase:
            if sound[0] == folder[5] and sound[1] == self.file:
                sound = sound
                break
            
        handlerSoundsList.updateSoundPlayCount(interaction.guild.id, folder[5], self.file, sound[2] + 1)


        # Play the sound with the actual volume
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(self.folder + self.file, **FFMPEG_OPTIONS), volume=self.volume)
        interaction.guild.voice_client.play(source)

        with contextlib.suppress(discord.HTTPException):
            await interaction.response.send_message()