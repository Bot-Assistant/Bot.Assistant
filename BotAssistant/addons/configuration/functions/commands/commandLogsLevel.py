import addons.configuration.handlers.handlerConfiguration as handlerConfiguration

import services.serviceBot as serviceBot
import settings.settingColors as settingColors
import settings.settingThumbnail as settingThumbnail

async def logs_level(ctx, level):
    if ctx.author.guild_permissions.manage_guild:
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs level configuration", description="The logs level has been configured.", color=settingColors.green)
        embed.add_field(name="Level", value=level, inline=False)
        embed.set_thumbnail(url=settingThumbnail.pageWithCurl)

        match level:
            case "📓 Debug":
                handlerConfiguration.setLogsLevel(ctx.guild.id, 0)
            case "📘 Info":
                handlerConfiguration.setLogsLevel(ctx.guild.id, 1)
            case "📙 Warn":
                handlerConfiguration.setLogsLevel(ctx.guild.id, 2)
            case "📕 Error":
                handlerConfiguration.setLogsLevel(ctx.guild.id, 3)
            case "⚠️ Fatal":
                handlerConfiguration.setLogsLevel(ctx.guild.id, 4)
    else:
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs level configuration", description="You don't have the permission to do this.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.pageWithCurl)

    await ctx.respond(embed=embed, delete_after=10)