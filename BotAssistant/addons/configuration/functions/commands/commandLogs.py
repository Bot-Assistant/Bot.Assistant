import services.serviceBot as serviceBot

from addons.configuration.handlers.handlerConfiguration import setLogsID

# This is a command that is used to set the logs channel
async def logs(ctx, arg1):

    # Permission check
    if ctx.author.guild_permissions.manage_guild:
        
        # Set the logs channel in the database
        setLogsID(ctx.guild.id, arg1.id)
        
        # Send a message to the user
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs channel configuration", description="The logs channel is now: " + arg1.name, color=0x00ff00)
        await ctx.respond(embed=embed)
    
    else:
        
        # Send a message to the user
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs channel configuration", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)