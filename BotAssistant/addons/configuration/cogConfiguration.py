import addons.configuration.functions.commands.commandLogs as commandLogs
import addons.configuration.functions.commands.commandLogsLevel as commandLogsLevel

import addons.configuration.init as init

import services.servicePermissionCheck as servicePermissionCheck


# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()



class Configuration(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # INIT GROUP COMMAND
    groupConfiguration = discordCommands.SlashCommandGroup(init.cogName, "Various commands to configure the bot.")

    # Verify if the bot has the permissions
    @groupConfiguration.command(name="permissions", description="Check the permissions of the bot")
    async def cmdSFXPermissions(self, ctx: commands.Context):
        await servicePermissionCheck.permissionCheck(ctx, init.addonPermissions)

    #t LOGS
    @groupConfiguration.command(name="log", description="Allows you to define the bot's log channel.")
    async def cmdLogs(
        self,
        ctx, 
        channel: discord.Option(discord.TextChannel, required=True)
    ):
        await commandLogs.logs(ctx, channel)


    #t LOGS_LEVEL
    @groupConfiguration.command(name="logs_level", description="Change the log level.")
    async def cmdLanguage(
        self,
        ctx, 
        logs_level: discord.Option(str, "logs_level", choices=["📓 Debug","📘 Info","📙 Warn","📕 Error","⚠️ Fatal"], required=True)
    ):
        await commandLogsLevel.logs_level(ctx, logs_level)
      

def setup(bot):
    bot.add_cog(Configuration(bot))
    
    