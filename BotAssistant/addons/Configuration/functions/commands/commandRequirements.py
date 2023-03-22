import addons.Configuration.init as init

import addons.Configuration.settings.settingColors as settingColors
import addons.Configuration.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
commands = serviceBot.classBot.getCommands()


async def checkRequirements(ctx):
    # PERMISSIONS CHECK
    import addons.Configuration.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdRequirements") == False:
        return
    

    # COMMAND
    embed = discord.Embed(title="Permissions", color=settingColors.cyan)
    embed.set_thumbnail(url=settingThumbnail.settingsIcons)

    # Check if the bot has the permissions
    for permission in init.addonPermissions:
        if not ctx.guild.me.guild_permissions.__getattribute__(permission):
            embed.add_field(name=permission, value="❌", inline=False)
        else:
            embed.add_field(name=permission, value="✅", inline=False)

    await ctx.respond(embed=embed)