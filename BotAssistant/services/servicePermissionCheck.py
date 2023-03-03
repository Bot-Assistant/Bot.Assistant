import settings.settingColors as settingColors
import settings.settingThumbnail as settingThumbnail
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
commands = serviceBot.classBot.getCommands()

async def permissionCheck(ctx: commands.Context, permissions: list):
    embed = discord.Embed(title="Permissions", color=settingColors.cyan)
    embed.set_thumbnail(url=settingThumbnail.balanceScale)

    # Check if the bot has the permissions
    for permission in permissions:
        if not ctx.guild.me.guild_permissions.__getattribute__(permission):
            embed.add_field(name=permission, value="❌", inline=False)
        else:
            embed.add_field(name=permission, value="✅", inline=False)

    await ctx.respond(embed=embed)