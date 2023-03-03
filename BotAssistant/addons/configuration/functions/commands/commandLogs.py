import services.serviceBot as serviceBot
import settings.settingColors as settingColors
import settings.settingThumbnail as settingThumbnail
from addons.configuration.handlers.handlerConfiguration import setLogsID


async def logs(ctx, channel):
    if ctx.author.guild_permissions.manage_guild:                  
        setLogsID(ctx.guild.id, channel.id)
        
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs channel configuration", description="The logs channel has been configured.", color=settingColors.green)
        embed.add_field(name="Channel", value=channel.mention, inline=False)
        embed.set_thumbnail(url=settingThumbnail.pageWithCurl)
        
        await ctx.respond(embed=embed, delete_after=10)
    
    else:
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs channel configuration", description="You don't have the permission to do this.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.pageWithCurl)
        
        await ctx.respond(embed=embed, delete_after=10)