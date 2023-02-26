import addons.joinrole.handlers.handlerJoinRole as handlerJoinRole
import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger


async def onMemberJoin(member):
    # Get join role list
        joinRoleList = handlerJoinRole.listRole(member.guild.id)
        
        if joinRoleList != None:
            for role in joinRoleList:
                joinRole = serviceBot.classBot.getDiscord().utils.get(member.guild.roles, id=role[0])
                await member.add_roles(joinRole)
                
                #Logs
                await serviceDiscordLogger.discordLogger.info("A new player has join the server, roles added to " + member.name, member.guild.id)
