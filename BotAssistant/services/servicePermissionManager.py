import handlers.handlerPermission as handlerPermission

async def messageAuthorHasPermission(ctx, permission: str):

    # If the permission is discord permission
    if permission.startswith("discord.permission."):

        permission = permission.replace("discord.permission.", "")
        
        # If the author has the permission
        if ctx.author.guild_permissions.__getattribute__(permission):
            return True
        
        else:
            return False
        
    else:
        # If one of the roles of the author has the permission
        for role in ctx.author.roles:
            if handlerPermission.roleHasPermission(ctx.guild.id, permission, role.id):
                return True
            
        return False