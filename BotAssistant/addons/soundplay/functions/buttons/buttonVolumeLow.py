import contextlib

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

from addons.soundplay.settings.settingAddon import *

FFMPEG_OPTIONS = {'executable': './addons/soundplay/requirements/ffmpeg.exe'}

class ButtonVolumeLow(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Volume Low",
            style=discord.ButtonStyle.blurple,
            emoji="🔈"
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

        # Verify if the bot is not already playing a sound
        if not interaction.guild.voice_client.is_playing():
            await interaction.response.send_message("The bot is not playing a sound", ephemeral=True, delete_after=5)
            return

        # Verify if the bot is not already playing a sound, if it is, make the sound volume -10%
        if interaction.guild.voice_client.is_playing():

            # Verify if the sound volume is already 5%, if it is, send a message to the user
            if interaction.guild.voice_client.source.volume <= 0.20:
                await interaction.response.send_message("The sound volume is already at the minimum", ephemeral=True, delete_after=5)
                return

            # Change the sound volume
            interaction.guild.voice_client.source.volume -= 0.10

            # Set embed volume field to the new volume
            embed = interaction.message.embeds[0]
            embed.set_field_at(0, name="Volume", value=f"`{interaction.guild.voice_client.source.volume * 100:.0f}%`")

            # Edit the message with the new embed
            await interaction.message.edit(embed=embed)

        with contextlib.suppress(discord.HTTPException):
            await interaction.response.send_message()