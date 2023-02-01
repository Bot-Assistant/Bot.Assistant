# █▀█ █▀▀ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█   █▀█ █▀█ █░░ █▀▀
# █▀▄ ██▄ █▀█ █▄▄ ░█░ █ █▄█ █░▀█   █▀▄ █▄█ █▄▄ ██▄
import addons.reactionrole.functions.commands.commandCreate as commandCreate
import addons.reactionrole.functions.commands.commandDelete as commandDelete
import addons.reactionrole.functions.commands.commandList as commandList
import addons.reactionrole.functions.events.eventOnRawReactionAdd as eventOnRawReactionAdd
import addons.reactionrole.functions.events.eventOnRawReactionRemove as eventOnRawReactionRemove

import addons.reactionrole.handlers.handlerDatabaseInit as handlerDatabaseInit

from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
commands = serviceBot.classBot.getCommands()
discord = serviceBot.classBot.getDiscord()
bot = serviceBot.classBot.getBot()

# INIT GROUP COMMAND
groupReactionRole = bot.create_group("reactionrole")


class ReactionRole(serviceBot.classBot.getCommands().Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    discord = serviceBot.classBot.getDiscord()
    
    
    @serviceBot.classBot.getCommands().Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await eventOnRawReactionAdd.OnRawReactionAdd(payload)
        
    @serviceBot.classBot.getCommands().Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        await eventOnRawReactionRemove.OnRawReactionRemove(payload)
    
    
    #t CREATE
    @groupReactionRole.command(name="create", description="Command to define the roles when users arrive.")
    async def commandLogs(
        ctx,
        
        channel_id: discord.Option(discord.TextChannel, required=True),
        message_id: discord.Option(str, required=True),
        role: discord.Option(discord.Role, required=True),
        emote: discord.Option(str, required=True),
        reactiontype: discord.Option(str, choices=["Ajoute le role","Supprime le role","Ajoute/Supprime le role"], required=True)
    ):
        await commandCreate.create(ctx, channel_id.id, message_id, role, emote, reactiontype)
        
        
    #t DELETE
    @groupReactionRole.command(name="delete", description="Delete a defined reaction role.")
    async def commandLogs(
        ctx,
        id: discord.Option(int, required=True)
    ):
        await commandDelete.delete(ctx, id)
        
        
    #t LIST
    @groupReactionRole.command(name="list", description="Get the list of reaction role list.")
    async def commandLogs(
        ctx,
        page: discord.Option(int, required=False)
    ):
        await commandList.list(ctx, page)
    


def setup(bot):
    if debug: Logger.debug("Loading Reaction Role")
    handlerDatabaseInit.databaseInit()
    bot.add_cog(ReactionRole(bot))
    
    