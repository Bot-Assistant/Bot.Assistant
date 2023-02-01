import addons.joinrole.handlers.handlerJoinRole as handlerJoinRole

import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger             


async def delete(ctx, role):

    # Permission check
    if ctx.author.guild_permissions.manage_roles:
        
        # Add the role in the database
        handlerJoinRole.deleteRole(ctx.guild.id, role.id)
        
        # Send a message to the user
        embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="Join role removed from configuration: " + role.name, color=0x00ff00)
        await ctx.respond(embed=embed)
        
        # Send a message to the logs
        await serviceDiscordLogger.discordLogger.warn("A join role has been removed by " + ctx.author.name + " -> " + role.name, ctx.guild.id)
    
    else:

        # Send a message to the user
        embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)
        
        # Send a message to the logs
        await serviceDiscordLogger.discordLogger.info("The user " + ctx.author.name + " wanted to type the command: /joinrole delete", ctx.guild.id)
