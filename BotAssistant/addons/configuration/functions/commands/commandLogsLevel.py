import services.serviceBot as serviceBot

from addons.configuration.handlers.handlerConfiguration import setLogsLevel

# This is a command that is used to set the logs level
async def logs_level(ctx, arg1):

    # Permission check
    if ctx.author.guild_permissions.manage_guild:

        # Set the logs level in the database
        match arg1:
            case "📓 Debug":
                setLogsLevel(ctx.guild.id, 0)
            case "📘 Info":
                setLogsLevel(ctx.guild.id, 1)
            case "📙 Warn":
                setLogsLevel(ctx.guild.id, 2)
            case "📕 Error":
                setLogsLevel(ctx.guild.id, 3)
            case "⚠️ Fatal":
                setLogsLevel(ctx.guild.id, 4)

        # Send a message to the user
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs level configuration", description="The logs level is now: " + arg1, color=0x00ff00)
        await ctx.respond(embed=embed)

    else:

        # Send a message to the user
        embed = serviceBot.classBot.getDiscord().Embed(title="Logs level configuration", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)