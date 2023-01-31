import addons.joinrole.handlers.handlerJoinRole as handlerJoinRole
import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger             


async def list(ctx):
    if ctx.author.guild_permissions.manage_roles:
        # Get join role list
        joinRoleList = handlerJoinRole.listRole(ctx.guild.id)
        
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="List of configured join roles", color=0x00ff00)
        
        if joinRoleList != None:
            for role in joinRoleList:
                roleName = serviceBot.classBot.getDiscord().utils.get(ctx.guild.roles, id=role[0])
                embed.add_field(name=roleName, value="Role ID is " + str(role[0]), inline=False)
        else:
            embed.add_field(name="No roles configured", value="Type the command /joinrole add to add roles to users who join the Discord.", inline=False)
        message = await ctx.respond(embed=embed)
        
        #Logs
        await serviceDiscordLogger.discordLogger.info("The list of join roles has been requested by  " + ctx.author.name, ctx.guild.id)
    else:
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)
        
        
        #Logs
        await serviceDiscordLogger.discordLogger.info("The user " + ctx.author.name + " wanted to type the command: /joinrole list", ctx.guild.id)