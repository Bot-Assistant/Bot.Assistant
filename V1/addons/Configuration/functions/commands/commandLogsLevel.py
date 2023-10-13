
import addons.Configuration.handlers.handlerConfiguration as handlerConfiguration
import addons.Configuration.settings.settingThumbnail as settingThumbnail
import addons.Configuration.settings.settingColors as settingColors
import addons.Configuration.settings.settingLogsLevel as settingLogsLevel

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def logsLevel(ctx, level):

    # PERMISSIONS CHECK
    import addons.Configuration.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdLogsLevel") == False:
        return
    
    # COMMAND
    embed = discord.Embed(
        title="Logs level configuration", 
        description="The logs level has been configured.", 
        color=settingColors.green
    )
    embed.add_field(name="Level", value=level, inline=False)
    embed.set_thumbnail(url=settingThumbnail.settingsIcons)

    match level:
        case settingLogsLevel.level1:
            handlerConfiguration.setLogsLevel(ctx.guild.id, 0)
        case settingLogsLevel.level2:
            handlerConfiguration.setLogsLevel(ctx.guild.id, 1)
        case settingLogsLevel.level3:
            handlerConfiguration.setLogsLevel(ctx.guild.id, 2)
        case settingLogsLevel.level4:
            handlerConfiguration.setLogsLevel(ctx.guild.id, 3)
        case settingLogsLevel.level5:
            handlerConfiguration.setLogsLevel(ctx.guild.id, 4)
                

    await ctx.respond(embed=embed)