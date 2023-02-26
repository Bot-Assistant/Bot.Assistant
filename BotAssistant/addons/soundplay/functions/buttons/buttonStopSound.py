import os
import contextlib

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

FFMPEG_OPTIONS = {'executable': './addons/soundplay/requirements/ffmpeg.exe'}

class ButtonStopSound(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Stop", 
            style=discord.ButtonStyle.red,
            emoji="⏹️"
            )

    async def callback(self, interaction: discord.Interaction):

        
        # Verify if the user is in a voice channel
        if interaction.user.voice is None:
            await interaction.response.send_message("You are not in a voice channel", ephemeral=True, delete_after=5)
            return
        
        # Verify if the bot is in a voice channel
        if interaction.guild.voice_client is None:
            await interaction.response.send_message("The bot is not in a voice channel", ephemeral=True, delete_after=5)
            return

        # Verify if the bot is with the user in the same voice channel
        if interaction.guild.voice_client == interaction.user.voice.channel:
            await interaction.response.send_message("The bot is not with you in the same voice channel", ephemeral=True, delete_after=5)
            return


        # Verify if the bot is not already playing a sound, if it is, save volume and stop the sound
        if interaction.guild.voice_client.is_playing():
            interaction.guild.voice_client.stop()
        else:
            await interaction.guild.voice_client.disconnect()

        with contextlib.suppress(discord.HTTPException):
            await interaction.response.send_message()