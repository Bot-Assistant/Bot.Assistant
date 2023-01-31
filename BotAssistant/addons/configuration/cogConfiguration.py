# █▀█ █▄░█   █▀▄▀█ █▀▀ █▀▄▀█ █▄▄ █▀▀ █▀█   ░░█ █▀█ █ █▄░█
# █▄█ █░▀█   █░▀░█ ██▄ █░▀░█ █▄█ ██▄ █▀▄   █▄█ █▄█ █ █░▀█
import addons.configuration.functions.commands.commandLogs as funcLogs
import addons.configuration.functions.commands.commandLogsLevel as funcLogsLevel


# INIT BOT VARIABLES
import services.serviceBot as serviceBot
commands = serviceBot.classBot.getCommands()
discord = serviceBot.classBot.getDiscord()
bot = serviceBot.classBot.getBot()

# INIT GROUP COMMAND
groupConfiguration = bot.create_group("configuration")

class Configuration(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    #t LOGS
    @groupConfiguration.command(name="log", description="Allows you to define the bot's log channel.")
    async def commandLogs(
        ctx, 
        channel: discord.Option(discord.TextChannel, required=True)
    ):
        await funcLogs.logs(ctx, channel)


    #t LOGS_LEVEL
    @groupConfiguration.command(name="logs_level", description="Change the log level.")
    async def commandLanguage(
        ctx, 
        logs_level: discord.Option(str, "logs_level", choices=["📓 Debug","📘 Info","📙 Warn","📕 Error","⚠️ Fatal"], required=True)
    ):
        await funcLogsLevel.logs_level(ctx, logs_level)

        

def setup(bot):
    bot.add_cog(Configuration(bot))
    
    