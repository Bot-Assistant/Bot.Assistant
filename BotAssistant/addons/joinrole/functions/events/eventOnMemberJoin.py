import addons.joinrole.handlers.handlerJoinRole as handlerJoinRole

import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger


async def onMemberJoin(member):
    
    # Get the list of roles to add
    joinRoleList = handlerJoinRole.listRole(member.guild.id)
        
    # Add the roles to the user
    if joinRoleList != None:
        for role in joinRoleList:
            joinRole = serviceBot.classBot.getDiscord().utils.get(member.guild.roles, id=role[0])
            await member.add_roles(joinRole)
            
            #Logs
            await serviceDiscordLogger.discordLogger.info("A new player has join the server, roles added to " + member.name, member.guild.id)
