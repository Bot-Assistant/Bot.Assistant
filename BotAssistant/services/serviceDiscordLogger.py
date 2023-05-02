from services.serviceLogger import consoleLogger

import handlers.handlerDiscordLogger as handlerDiscordLogger
import services.serviceTime as serviceTime
import settings.settingColors as settingColors

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
bot = serviceBot.classBot.getBot()

class discordLogger:

    async def debug(ctx, title:str, error:str, commandName:str = None):

        logsID = handlerDiscordLogger.getLogsID(ctx.guild.id)
        
        if logsID == None:
            return
        
        if handlerDiscordLogger.getLogsLevel(ctx.guild.id) == 0:

            consoleLogger.debug("[DISCORD] " + error)

            embed=discord.Embed(title="📓 [DEBUG] " + title, description=error, color=settingColors.white)
            embed.set_footer(text=serviceTime.classTime.getHMS())

            if commandName != None:
                embed.add_field(name="Command", value=f"`/{commandName}`", inline=False)

            try:
                await bot.get_channel(logsID).send(embed=embed)
            except:
                pass
            
            
    async def info(ctx, title:str, error:str, commandName:str = None):
        logsID = handlerDiscordLogger.getLogsID(ctx.guild.id)
        
        if logsID == None:
            return
        
        if handlerDiscordLogger.getLogsLevel(ctx.guild.id) <= 1:
            consoleLogger.info("[DISCORD] " + error)
            
            embed=discord.Embed(title="📘 [INFO] " + title, description=error, color=settingColors.cyan)
            embed.set_footer(text=serviceTime.classTime.getHMS())

            if commandName != None:
                embed.add_field(name="Command", value=f"`/{commandName}`", inline=False)

            try:
                await bot.get_channel(logsID).send(embed=embed)
            except:
                pass
    
    
    async def warn(ctx, title:str, error:str, commandName:str = None):
        logsID = handlerDiscordLogger.getLogsID(ctx.guild.id)
        
        if logsID == None:
            return
        
        if handlerDiscordLogger.getLogsLevel(ctx.guild.id) <= 2:
            consoleLogger.warn("[DISCORD] " + error)
            
            embed=discord.Embed(title="📒 [WARN] " + title, description=error, color=settingColors.yellow)
            embed.set_footer(text=serviceTime.classTime.getHMS())

            if commandName != None:
                embed.add_field(name="Command", value=f"`/{commandName}`", inline=False)

            try:
                await bot.get_channel(logsID).send(embed=embed)
            except:
                pass
            
            
    async def error(ctx, title:str, error:str, commandName:str = None):
        logsID = handlerDiscordLogger.getLogsID(ctx.guild.id)
        
        if logsID == None:
            return
        
        if handlerDiscordLogger.getLogsLevel(ctx.guild.id) <= 3:
            consoleLogger.error("[DISCORD] " + error)
            
            embed=discord.Embed(title="📙 [ERROR] " + title, description=error, color=settingColors.orange)
            embed.set_footer(text=serviceTime.classTime.getHMS())

            if commandName != None:
                embed.add_field(name="Command", value=f"`/{commandName}`", inline=False)

            try:
                await bot.get_channel(logsID).send(embed=embed)
            except:
                pass
        
        
    
    
    async def critical(ctx, title:str, error:str, commandName:str = None):
        logsID = handlerDiscordLogger.getLogsID(ctx.guild.id)
        
        if logsID == None:
            return
        
        if handlerDiscordLogger.getLogsLevel(ctx.guild.id) <= 4:
            consoleLogger.critical("[DISCORD] " + error)
            
            embed=discord.Embed(title="📕 [CRITICAL] " + title, description=error, color=settingColors.red)
            embed.set_footer(text=serviceTime.classTime.getHMS())

            if commandName != None:
                embed.add_field(name="Command", value=f"`/{commandName}`", inline=False)

            try:
                await bot.get_channel(logsID).send(embed=embed)
            except:
                pass