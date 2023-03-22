import settings.settingThumbnail as settingThumbnail
import settings.settingColors as settingColors

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def noPermission(ctx, permission: str):
    embed = discord.Embed(
        title="Permission denied",
        description="You don't have the permission execute this command.",
        color=settingColors.red
    )

    embed.add_field(
        name="Permission needed",
        value=permission
    )

    embed.set_thumbnail(url=settingThumbnail.interdictIcons)

    await ctx.respond(embed=embed)


