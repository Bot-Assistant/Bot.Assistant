import addons.Configuration.handlers.handlerPermission as handlerPermission
import addons.Configuration.settings.settingColors as settingColors
import addons.Configuration.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def add(ctx, addon, permission, role):

    # PERMISSIONS CHECK
    import addons.Configuration.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdPermissionAdd") == False:
        return


    # COMMAND
    # Verify if the permission is already in the database
    permissionBool = handlerPermission.permissionExists(ctx.guild.id, permission, role.id)

    # If the permission is already in the database
    if permissionBool:
        
        embed = discord.Embed(
            title="Permission already added",
            description="The permission is already added to the role.",
            color=settingColors.red
        )
        embed.set_thumbnail(url=settingThumbnail.groupsIcons)
        await ctx.respond(embed=embed)

    # If the permission is not in the database
    else:
        embed = discord.Embed(
            title="Permission added",
            description="The permission has been added to the role.",
            color=settingColors.green
        )
        embed.set_thumbnail(url=settingThumbnail.groupsIcons)
        await ctx.respond(embed=embed)
        
        # Add the permission to the role
        handlerPermission.addPermission(ctx.guild.id, addon, permission, role.id)

