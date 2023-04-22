# EXTERNAL IMPORTS
import os

# ADDON IMPORTS
import addons.Configuration.init as init

import addons.Configuration.functions.commands.commandLogsChannel as commandLogsChannel
import addons.Configuration.functions.commands.commandLogsLevel as commandLogsLevel
import addons.Configuration.functions.commands.commandPermissionAdd as commandPermissionAdd
import addons.Configuration.functions.commands.commandPermissionRemove as commandPermissionRemove
import addons.Configuration.functions.commands.commandPermissionList as commandPermissionList
import addons.Configuration.functions.commands.commandRequirements as commandRequirements

import addons.Configuration.handlers.handlerDatabaseInit as handlerDatabaseInit
import addons.Configuration.handlers.handlerPermission as handlerPermission

import addons.Configuration.settings.settingLogsLevel as settingLogsLevel

# BOTASSISTANT IMPORTS
import services.serviceAddonManager as serviceAddonManager
from services.serviceLogger import consoleLogger as Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()



class Configuration(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # AUTOCOMPLETE
    async def getAddonsList(ctx: discord.AutocompleteContext):
        return os.listdir("addons")

    async def getPermissionsListAddon(ctx: discord.AutocompleteContext):
        addon = ctx.options["addon"]
        return serviceAddonManager.getPermissionsList(addon)


    async def getPermissionsListDB(ctx: discord.AutocompleteContext):
        role = ctx.options["role"]
        resultDatabase = handlerPermission.getPermissionsByRoleID(ctx.interaction.guild_id, role)

        permissions = []
        for permission in resultDatabase:
            permissions.append(permission[1])

        return permissions


    # INIT GROUP COMMAND
    groupConfiguration = discordCommands.SlashCommandGroup(init.cogName, "Various commands to configure the bot.")
    groupPermission = groupConfiguration.create_subgroup("permission", "Various commands to configure the bot's permissions.")
    groupLogs = groupConfiguration.create_subgroup("logs", "Various commands to configure the bot's logs.")

    # Verify if the bot has the prerequisites permissions
    @groupConfiguration.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)

    # Configuration Logs Channel
    @groupLogs.command(name="channel", description="Allows you to define the bot's log channel.")
    async def cmdLogsChannel(
        self,
        ctx, 
        channel: discord.Option(discord.TextChannel, required=True)
    ):
        await commandLogsChannel.logsChannel(ctx, channel)


    # Configuration Logs Level
    @groupLogs.command(name="level", description="Change the log level.")
    async def cmdLogsLevel(
        self,
        ctx, 
        logs_level: discord.Option(str, "logs_level", choices=settingLogsLevel.logsLevels, required=True)
    ):
        await commandLogsLevel.logsLevel(ctx, logs_level)


    # Configuration Permissions Add
    @groupPermission.command(name="add", description="Add a permission to a role.")
    async def cmdPermissionAdd(
        self,
        ctx,
        addon: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getAddonsList), description="Name of the addon"),
        permission: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getPermissionsListAddon), description="Name of the permission"),
        role: discord.Option(discord.Role, required=True)
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the permission add command.", str(ctx.command))
        await commandPermissionAdd.add(ctx, addon, permission, role)


    # Configuration Permissions Remove
    @groupPermission.command(name="remove", description="Remove a permission from a role.")
    async def cmdPermissionRemove(
        self,
        ctx,
        role: discord.Option(discord.Role, required=True),
        permission: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getPermissionsListDB), description="Name of the permission")
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the permission remove command.", str(ctx.command))
        await commandPermissionRemove.remove(ctx, role, permission)


    # Configuration Permissions List
    @groupPermission.command(name="list", description="List the permissions of a role.")
    async def cmdPermissionList(
        self,
        ctx,
        role: discord.Option(discord.Role, required=True)
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the permission list command.", str(ctx.command))
        await commandPermissionList.list(ctx, role)
      

def setup(bot):
    if debug: Logger.debug("Loading cog: " + init.cogName)
    handlerDatabaseInit.databaseInit()
    bot.add_cog(Configuration(bot))
    
    