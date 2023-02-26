import handlers.handlerDiscordLogger as handlerDiscordLogger
import services.serviceBot as serviceBot
import services.serviceFileManager as serviceFileManager
import services.serviceTime as serviceTime
from services.serviceLogger import consoleLogger
from settings.settingColors import *


class discordLogger:
	#0 debug
    #1 info
    #2 warn
    #3 error
    #4 fatal

    async def debug(error, server_id):
        logs_id = handlerDiscordLogger.getLogsID(server_id)
        
        if logs_id == None:
            return
        
        logLevel = handlerDiscordLogger.getLogsLevel(server_id)
        if logLevel == 0:
            #Set message
            message = "[DEBUG] " + serviceTime.classTime.getHMS() + " " + str(error)
              
            #Print to console
            consoleLogger.debug(message)
            
            #Print log to log file
            serviceFileManager.fileWrite("logs/" + serviceTime.classTime.getDMY() + ".log", message)
            
            #Send Embed
            embed=serviceBot.classBot.getDiscord().Embed(title="📓 [DEBUG]", description=error, color=white)
            embed.set_footer(text=serviceTime.classTime.getHMS())
            await serviceBot.classBot.getBot().get_channel(logs_id).send(embed=embed)
            
            
    async def info(error, server_id):
        logs_id = handlerDiscordLogger.getLogsID(server_id)
        
        if logs_id == None:
            return
        
        logLevel = handlerDiscordLogger.getLogsLevel(server_id)
        if logLevel <= 1:
            #Set message
            message = "[INFO] " + serviceTime.classTime.getHMS() + " " + str(error)
            
            #Print log to log file
            serviceFileManager.fileWrite("logs/" + serviceTime.classTime.getDMY() + ".log", message)
            
            #Send Embed
            embed=serviceBot.classBot.getDiscord().Embed(title="📘 [INFO]", description=error, color=cyan)
            logs_id = handlerDiscordLogger.getLogsID(server_id)
            await serviceBot.classBot.getBot().get_channel(logs_id).send(embed=embed)
        else:
            print("[LOGS] Annulation de l'envoi de logs (Niveau 1)")
    
    
    async def warn(error, server_id):
        logs_id = handlerDiscordLogger.getLogsID(server_id)
        
        if logs_id == None:
            return
        
        logLevel = handlerDiscordLogger.getLogsLevel(server_id)
        if logLevel <= 2:
            #Set message
            message = "[WARN] " + serviceTime.classTime.getHMS() + " " + str(error)
            
            #Print log to log file
            serviceFileManager.fileWrite("logs/" + serviceTime.classTime.getDMY() + ".log", message)
            
            #Send Embed
            embed=serviceBot.classBot.getDiscord().Embed(title="📙 [WARN]", description=error, color=yellow)
            logs_id = handlerDiscordLogger.getLogsID(server_id)
            await serviceBot.classBot.getBot().get_channel(logs_id).send(embed=embed)
        else:
            print("[LOGS] Annulation de l'envoi de logs (Niveau 2)")
            
            
    async def error(error, server_id):
        logs_id = handlerDiscordLogger.getLogsID(server_id)
        
        if logs_id == None:
            return
        
        logLevel = handlerDiscordLogger.getLogsLevel(server_id)
        if logLevel <= 3:
            #Set message
            message = "[ERROR] " + serviceTime.classTime.getHMS() + " " + str(error)
            
            #Print log to log file
            serviceFileManager.fileWrite("logs/" + serviceTime.classTime.getDMY() + ".log", message)
            
            #Send Embed
            embed=serviceBot.classBot.getDiscord().Embed(title="📕 [ERROR]", description=error, color=orange)
            logs_id = handlerDiscordLogger.getLogsID(server_id)
            await serviceBot.classBot.getBot().get_channel(logs_id).send(embed=embed)
        else:
            print("[LOGS] Annulation de l'envoi de logs (Niveau 3)")
    
    
    async def critical(error, server_id):
        logs_id = handlerDiscordLogger.getLogsID(server_id)
        
        if logs_id == None:
            return
        
        logLevel = handlerDiscordLogger.getLogsLevel(server_id)
        if logLevel <= 4:
            #Set message
            message = "[CRITICAL] " + serviceTime.classTime.getHMS() + " " + str(error)
            
            #Print log to log file
            serviceFileManager.fileWrite("logs/" + serviceTime.classTime.getDMY() + ".log", message)
            
            #Send Embed
            embed=serviceBot.classBot.getDiscord().Embed(title="⚠️ [CRITICAL]", description=error, color=red)
            logs_id = handlerDiscordLogger.getLogsID(server_id)
            await serviceBot.classBot.getBot().get_channel(logs_id).send(embed=embed)
        else:
            print("[LOGS] Annulation de l'envoi de logs (Niveau 4)")