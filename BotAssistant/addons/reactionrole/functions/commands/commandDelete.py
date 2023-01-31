import addons.reactionrole.handlers.handlerReactionRole as handlerReactionRole
import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger

async def delete(ctx, ID):
    if ctx.author.guild_permissions.manage_roles:
        try:
            #Suppression BDD
            handlerReactionRole.deleteReactionRole(ctx.guild.id, ID)
        except Exception as error:
            #Message Commande
            embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="Reaction role deletion error", color=0xCD2B2B)
            await ctx.respond(embed=embed)
            return
        
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="Join role removed from configuration: " + str(ID), color=0x00ff00)
        await ctx.respond(embed=embed)
        
        #Logs
        await serviceDiscordLogger.discordLogger.warn("A reaction role has been removed by " + ctx.author.name + " -> " + ID, ctx.guild.id)
    else:
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)
        
        #Logs
        await serviceDiscordLogger.discordLogger.info("The user " + ctx.author.name + " wanted to type the command: /reactionrole delete", ctx.guild.id)