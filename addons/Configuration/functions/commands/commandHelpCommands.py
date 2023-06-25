import addons.Configuration.settings.settingThumbnail as settingThumbnail
import addons.Configuration.settings.settingColors as settingColors

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
bot = serviceBot.classBot.getBot()

async def helpCommands(ctx, commandName):

    embed = discord.Embed(
                        
        title = f"Command **/{commandName}**",
        description = "Here is the help message of the command.\nYou must have permission to run some commands.\nㅤ",
        color = settingColors.blue
    )

    embed.set_thumbnail(url=settingThumbnail.settingsIcons)

    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)

    for command in bot.commands:

        if command.name == commandName:

            for subCommand in command.walk_commands():
                
                if subCommand.description.startswith("🔶"):
                    continue

                if len(embed.fields) == 25:
                    embed.description = "⚠️ This command has too many options to display them all."
                    break
                
                try:
                    optionList = ""
                    
                    for option in subCommand.options:
                        
                        optionList = optionList + f"`<{option.name}>` "

                    embed.add_field(
                        name = f"🔹 /{subCommand.parent} {subCommand.name} {optionList}",
                        value = f"{subCommand.description}\nㅤ",
                        inline = False
                    )

                except:
                    embed.add_field(
                        name = f"🔹 /{command.name} {subCommand.name}",
                        value = f"{subCommand.description}\nㅤ",
                        inline = False
                    )


    await ctx.respond(embed=embed, delete_after=900)

