# █▀█ █▄░█   █▀▄▀█ █▀▀ █▀▄▀█ █▄▄ █▀▀ █▀█   ░░█ █▀█ █ █▄░█
# █▄█ █░▀█   █░▀░█ ██▄ █░▀░█ █▄█ ██▄ █▀▄   █▄█ █▄█ █ █░▀█
import addons.joinrole.functions.commands.commandAdd as funcAdd
import addons.joinrole.functions.commands.commandDelete as funcDelete
import addons.joinrole.functions.commands.commandList as funcList
import addons.joinrole.functions.events.eventOnMemberJoin as funcEventOnMemberJoin

import addons.joinrole.handlers.handlerDatabaseInit as handlerDatabaseInit
from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
commands = serviceBot.classBot.getCommands()
discord = serviceBot.classBot.getDiscord()
bot = serviceBot.classBot.getBot()

# INIT GROUP COMMAND
groupJoinRole = bot.create_group("joinrole")

class JoinRole(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await funcEventOnMemberJoin.onMemberJoin(member)
    
    
    #t ADD
    @groupJoinRole.command(name="add", description="Command to define the roles when users arrive.")
    async def commandLogs(
        ctx: discord.ApplicationContext, 
        role: discord.Option(
            discord.SlashCommandOptionType.role,  
            required=True
        )
    ):
        await funcAdd.add(ctx, role)


    #t DELETE
    @groupJoinRole.command(name="delete", description="Command to remove a role from the newcomers list.")
    async def commandLogs(
        ctx: discord.ApplicationContext,
        role: discord.Option(
            discord.SlashCommandOptionType.role,  
            required=True
        )
    ):
        await funcDelete.delete(ctx, role)


    #t LIST
    @groupJoinRole.command(name="list", description="Command to remove a role from the newcomers list.")
    async def commandLogs(
        ctx: discord.ApplicationContext
    ):
        await funcList.list(ctx)
        


def setup(bot):
    if debug: Logger.debug("Loading Join Role")
    handlerDatabaseInit.databaseInit()
    bot.add_cog(JoinRole(bot))
    
    