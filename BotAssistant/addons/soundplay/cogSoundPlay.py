import os

# Addons imports
# Database
from addons.soundplay.handlers.handlerDatabaseInit import databaseInit
# Settings
import addons.soundplay.settings.settingAddon as settingAddon
# Functions
from addons.soundplay.functions.commands.commandPlay import play
from addons.soundplay.functions.commands.commandFolderCreate import folderCreate
from addons.soundplay.functions.commands.commandFolderDelete import folderDelete
from addons.soundplay.functions.commands.commandSoundUpload import upload
from addons.soundplay.functions.commands.commandSoundDelete import soundDelete
# Events
from addons.soundplay.functions.events.eventOnReady import onReady
from addons.soundplay.functions.events.eventOnGuildJoin import onGuildJoin
from addons.soundplay.functions.events.eventOnGuildRemove import onGuildRemove
from addons.soundplay.functions.events.eventOnVoiceStateUpdate import onVoiceStateUpdate

# BotAssistant imports
from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug

# Init BotAssistant
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()


class PlaySound(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # INIT SOUNDS FOLDERS
    @commands.Cog.listener()
    async def on_ready(self):
        onReady()

    # Create the sound folder with guild ID if it doesn't exist
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        onGuildJoin(guild)

    # Remove the sound folder with guild ID if it exists
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        onGuildRemove(guild)
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        await onVoiceStateUpdate(member, before, after)



    # AUTOCOMPLETE
    async def getSoundsFolders(ctx: discord.AutocompleteContext):
        return os.listdir(settingAddon.defaultSoundFolder + str(ctx.interaction.guild_id) + "/")

    async def getSounds(ctx: discord.AutocompleteContext):
        directory = ctx.options["directory"]
        return os.listdir(settingAddon.defaultSoundFolder + str(ctx.interaction.guild_id) + "/" + directory + "/")


    # INIT GROUP COMMAND
    groupSoundPlay = discordCommands.SlashCommandGroup("soundplay", "Various commands to play sounds")
    groupDeleteElement = groupSoundPlay.create_subgroup ("delete", "Various commands to delete sounds or folders")
    groupCreateElement = groupSoundPlay.create_subgroup ("create", "Various commands to create folders")


    # PLAY A SOUND
    # Play a sound from the sound folder
    @groupSoundPlay.command(name="play", description="Play a sound from the sound folder")
    async def commandSFX(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located")
        ):
        await play(ctx, directory)


    # UPLOAD A SOUND
    # Upload a sound in a specific folder
    @groupSoundPlay.command(name="upload", description="Upload a sound in a specific folder")
    async def commandSFXUpload(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located", required=True),
        sound: discord.Option(discord.Attachment, description="Sound to upload", required=True)
        ):
        await upload(ctx, directory, sound)


    # DELETE A ELEMENT
    # Create a new sound folder in the sound folder
    @groupCreateElement.command(name="folder", description="Create a new sound folder in the sound folder")
    async def commandSFXFolderCreate(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, description="Folder where the sound is located")
        ):
        await folderCreate(ctx, directory)

    # Delete a sound folder in the sound folder
    @groupDeleteElement.command(name="folder", description="Delete a sound folder in the sound folder")
    async def commandSFXFolderDelete(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located")
        ):
        await folderDelete(ctx, directory)

    # Delete a sound in a specific folder
    @groupDeleteElement.command(name="sound", description="Delete a sound in a specific folder")
    async def commandSFXDelete(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located", required=True),
        sound: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSounds), description="Sound to delete", required=True)
        ):
        await soundDelete(ctx, directory, sound)


# INIT COG
def setup(bot):
    if debug: Logger.debug("[COG][SOUNDPLAY]Sound play cog init")
    databaseInit()
    bot.add_cog(PlaySound(bot))
