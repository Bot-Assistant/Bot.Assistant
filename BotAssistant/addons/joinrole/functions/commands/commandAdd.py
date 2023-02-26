import addons.joinrole.handlers.handlerJoinRole as handlerJoinRole
import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger             


async def add(ctx, role):
    if ctx.author.guild_permissions.manage_roles:
        #Ajout BDD
        handlerJoinRole.addRole(ctx.guild.id, role.id)
        
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="New join role added: " + role.name, color=0x00ff00)
        await ctx.respond(embed=embed)
        
        #Logs
        await serviceDiscordLogger.discordLogger.warn("A new join role has been added by " + ctx.author.name + " -> " + role.name, ctx.guild.id)
    else:
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)
        
        #Logs
        await serviceDiscordLogger.discordLogger.info("The user " + ctx.author.name + " wanted to type the command: /joinrole add", ctx.guild.id)
 