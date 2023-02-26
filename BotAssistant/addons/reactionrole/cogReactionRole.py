# █▀█ █▀▀ ▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█   █▀█ █▀█ █░░ █▀▀
# █▀▄ ██▄ █▀█ █▄▄ ░█░ █ █▄█ █░▀█   █▀▄ █▄█ █▄▄ ██▄
from addons.reactionrole.functions.commands.commandCreate import create
from addons.reactionrole.functions.commands.commandDelete import delete
from addons.reactionrole.functions.commands.commandList import list
from addons.reactionrole.functions.events.eventOnRawReactionAdd import OnRawReactionAdd
from addons.reactionrole.functions.events.eventOnRawReactionRemove import OnRawReactionRemove

import addons.reactionrole.handlers.handlerDatabaseInit as handlerDatabaseInit
from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()


class ReactionRole(serviceBot.classBot.getCommands().Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    discord = serviceBot.classBot.getDiscord()
    
    # EVENTS LISTENERS
    @serviceBot.classBot.getCommands().Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await OnRawReactionAdd(payload)
        
    @serviceBot.classBot.getCommands().Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        await OnRawReactionRemove(payload)
    
    # INIT GROUP COMMAND
    groupReactionRole = discordCommands.SlashCommandGroup("reactionrole", "Various commands to manage reaction role")
    
    #t CREATE
    @groupReactionRole.command(name="create", description="Command to define the roles when users arrive.")
    async def commandLogs(
        self,
        ctx,
        
        channel_id: discord.Option(discord.TextChannel, required=True),
        message_id: discord.Option(str, required=True),
        role: discord.Option(discord.Role, required=True),
        emote: discord.Option(str, required=True),
        reactiontype: discord.Option(str, choices=["Ajoute le role","Supprime le role","Ajoute/Supprime le role"], required=True)
    ):
        await create(ctx, channel_id.id, message_id, role, emote, reactiontype)
        
        
    #t DELETE
    @groupReactionRole.command(name="delete", description="Delete a defined reaction role.")
    async def commandLogs(
        self,
        ctx,
        id: discord.Option(int, required=True)
    ):
        await delete(ctx, id)
        
        
    #t LIST
    @groupReactionRole.command(name="list", description="Get the list of reaction role list.")
    async def commandLogs(
        self,
        ctx,
        
        page: discord.Option(int, required=False)
    ):
        await list(ctx, page)
    


def setup(bot):
    if debug: Logger.debug("Loading Reaction Role")
    handlerDatabaseInit.databaseInit()
    bot.add_cog(ReactionRole(bot))
    
    