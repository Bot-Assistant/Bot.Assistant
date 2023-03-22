import os
from prettytable import PrettyTable

import addons.Configuration.handlers.handlerPermission as handlerPermission
import addons.Configuration.settings.settingColors as settingColors
import addons.Configuration.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def list(ctx, role):

    # PERMISSIONS CHECK
    import addons.Configuration.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdPermissionList") == False:
        return


    # COMMAND
    embed = discord.Embed(
        title="Permissions of the role " + role.name,
        color=settingColors.blue
    )
    embed.set_thumbnail(url=settingThumbnail.groupsIcons)

    # Get the permissions from the database
    permissions = handlerPermission.getPermissionsByRoleID(ctx.guild.id, role.id)

    # If the role has permissions
    if permissions:
        
        myTable = PrettyTable(["Addon", "Permissions"])

        # Add rows
        for permission in permissions:
            myTable.add_row([permission[0], permission[1]])
        

        # If content has more than 1900 characters send it as a file
        if len(myTable.get_string()) > 1900:
            with open("permissions.txt", "w") as f:
                f.write(myTable.get_string())
            await ctx.respond(embed=embed)
            await ctx.send(file=discord.File("permissions.txt"))
            os.remove("permissions.txt")

        # If content has less than 1900 characters send it as a message
        else:
            await ctx.respond(embed=embed)
            await ctx.send(content="`" + myTable.get_string() + "`")

    # If the role doesn't have permissions
    else:
        embed = discord.Embed(
            title="No permissions",
            description="The role doesn't have any permissions.",
            color=settingColors.red
        )
        embed.set_thumbnail(url=settingThumbnail.groupsIcons)
        await ctx.respond(embed=embed)
