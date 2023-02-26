import services.serviceBot as serviceBot
from addons.configuration.handlers.handlerConfiguration import setLogsID


async def logs(ctx, arg1):
    if ctx.author.guild_permissions.manage_guild:
        
        setLogsID(ctx.guild.id, arg1.id)
        
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs channel configuration", description="The logs channel is now: " + arg1.name, color=0x00ff00)
        await ctx.respond(embed=embed)
        
    else:
        
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs channel configuration", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)