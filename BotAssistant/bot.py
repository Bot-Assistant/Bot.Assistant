# INIT FILE SYSTEM
import services.serviceFileManager as serviceFileManager
serviceFileManager.createFolder("logs")

import services.serviceVerification as serviceVerification
serviceVerification.packageVerification()

from settings.settingBot import botVersion
print("=============================================")
print("█▄▄ █▀█ ▀█▀ ░ ▄▀█ █▀ █▀ █ █▀ ▀█▀ ▄▀█ █▄░█ ▀█▀")
print("█▄█ █▄█ ░█░ ▄ █▀█ ▄█ ▄█ █ ▄█ ░█░ █▀█ █░▀█ ░█░")
print("=============================================")
print("            Bot Assistant Version            ")
print(f"            {botVersion}         ")

# INIT LOG SYSTEM
from services.serviceLogger import consoleLogger as Logger
Logger.system("[BOT]The bot is loading")

# INIT CONFIG FILE SYSTEM
import services.serviceFirstInit as serviceFirstInit
serviceFirstInit.firstStartCheck()

# INIT DATABASE
import handlers.handlerDatabaseInit as handlerDatabaseInit
handlerDatabaseInit.databaseInit()

# INIT BOT 
import services.serviceBot as serviceBot
serviceBot.classBot.initialize()
bot = serviceBot.classBot.getBot()
command = serviceBot.classBot.getCommands()



# █▀█ █▄░█   █▀█ █▀▀ ▄▀█ █▀▄ █▄█
# █▄█ █░▀█   █▀▄ ██▄ █▀█ █▄▀ ░█░
from services.serviceStop import stopCommand
import functions.events.eventOnReady as eventOnReady
@bot.event
async def on_ready():
    Logger.system("The bot is now online")
    eventOnReady.onReady()
    stopCommand()



from handlers import handlersServer
@bot.event
async def on_guild_join(guild):
    handlersServer.addServerID(guild.id)

@bot.event
async def on_guild_remove(guild):
    handlersServer.delServerID(guild.id)


# ▄▀█ █▀▄ █▀▄ █▀█ █▄░█ █▀
# █▀█ █▄▀ █▄▀ █▄█ █░▀█ ▄█
from services.serviceCogLoad import importCogs
importCogs()


# START THE BOT
import settings.settingToken as settingToken
bot.run(settingToken.token)