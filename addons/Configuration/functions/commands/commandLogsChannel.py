import addons.Configuration.handlers.handlerConfiguration as handlerConfiguration
import addons.Configuration.settings.settingThumbnail as settingThumbnail
import addons.Configuration.settings.settingColors as settingColors

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def logsChannel(ctx, channel):

    # PERMISSIONS CHECK
    import addons.Configuration.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdLogsChannel") == False:
        return

    # COMMAND
    handlerConfiguration.setLogsID(ctx.guild.id, channel.id)
    
    embed = discord.Embed(
        title="Logs channel configuration", 
        description="The logs channel has been configured.", 
        color=settingColors.green
    )
    embed.add_field(name="Channel", value=channel.mention, inline=False)
    embed.set_thumbnail(url=settingThumbnail.settingsIcons)
    
    await ctx.respond(embed=embed)
    