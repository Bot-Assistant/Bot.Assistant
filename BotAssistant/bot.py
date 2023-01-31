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

# INIT FILE SYSTEM
import services.serviceFileManager as serviceFileManager

serviceFileManager.createFolder("logs")

# INIT CONFIG FILE SYSTEM
from services.serviceFirstInit import firstStartCheck

firstStartCheck()

# INIT DATABASE
import services.serviceDatabase as serviceDatabase

serviceDatabase.bddInit()

# INIT BOT 
import services.serviceBot as serviceBot

serviceBot.classBot.initialize()

bot = serviceBot.classBot.getBot()



# █▀█ █▄░█   █▀█ █▀▀ ▄▀█ █▀▄ █▄█
# █▄█ █░▀█   █▀▄ ██▄ █▀█ █▄▀ ░█░
from services.serviceStop import stopCommand
@bot.event
async def on_ready():
    Logger.system("The bot is now online")
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