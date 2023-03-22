import addons.Configuration.handlers.handlerPermission as handlerPermission
import addons.Configuration.settings.settingColors as settingColors
import addons.Configuration.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def remove(ctx, role, permission):

    # PERMISSIONS CHECK
    import addons.Configuration.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdPermissionRemove") == False:
        return


    # COMMAND
    # If the permission is already in the database
    if not handlerPermission.permissionExists(ctx.guild.id, permission, role.id):
        
        embed = discord.Embed(
            title="Permission already removed",
            description="The role doesn't have this permission.",
            color=settingColors.red
        )
        embed.set_thumbnail(url=settingThumbnail.groupsIcons)
        await ctx.respond(embed=embed)
        return


    embed = discord.Embed(
        title="Permission added",
        description="The permission has been removed from the role.",
        color=settingColors.green
    )
    embed.set_thumbnail(url=settingThumbnail.groupsIcons)
    await ctx.respond(embed=embed)

    # Add the permission to the role
    handlerPermission.removePermission(ctx.guild.id, permission, role.id)


