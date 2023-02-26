# █▀█ █▄░█   █▀▄▀█ █▀▀ █▀▄▀█ █▄▄ █▀▀ █▀█   ░░█ █▀█ █ █▄░█
# █▄█ █░▀█   █░▀░█ ██▄ █░▀░█ █▄█ ██▄ █▀▄   █▄█ █▄█ █ █░▀█
import addons.configuration.functions.commands.commandLogs as funcLogs
import addons.configuration.functions.commands.commandLogsLevel as funcLogsLevel


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
    groupConfiguration = discordCommands.SlashCommandGroup("configuration")

    #t LOGS
    @groupConfiguration.command(name="log", description="Allows you to define the bot's log channel.")
    async def commandLogs(
        self,
        ctx, 
        channel: discord.Option(discord.TextChannel, required=True)
    ):
        await funcLogs.logs(ctx, channel)


    #t LOGS_LEVEL
    @groupConfiguration.command(name="logs_level", description="Change the log level.")
    async def commandLanguage(
        self,
        ctx, 
        logs_level: discord.Option(str, "logs_level", choices=["📓 Debug","📘 Info","📙 Warn","📕 Error","⚠️ Fatal"], required=True)
    ):
        await funcLogsLevel.logs_level(ctx, logs_level)

        

def setup(bot):
    bot.add_cog(Configuration(bot))
    
    