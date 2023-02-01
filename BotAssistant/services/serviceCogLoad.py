import importlib
import os

from services.serviceLogger import consoleLogger as Logger
from services.serviceBot import classBot

bot = classBot.getBot()

def importCogs():
    try:
        if os.name == 'nt':
            Logger.system("OS: Windows")
        elif os.name == 'posix':
            Logger.system("OS: Linux")
        else:
            Logger.system("OS: Unknown")
            os._exit(0)
            
        for root, dirs, files in os.walk("addons"):
            for file in files:
                if file == "init.py":
                    
                    if os.name == 'nt':
                        initFile = os.path.join(root, file).replace("\\", ".")[:-3]
                    elif os.name == 'posix':
                        initFile = os.path.join(root, file).replace("/", ".")[:-3]

                    importedFile = importlib.import_module(initFile)

                    if importedFile.cogEnabled == False:
                        continue
                    
                    if os.name == 'nt':
                        cogPath = root.replace("\\", ".") + "." + importedFile.cogFile
                    elif os.name == 'posix':
                        cogPath = root.replace("/", ".") + "." + importedFile.cogFile
                    
                    bot.load_extension(cogPath)
                    
                    Logger.info("[COG]" + cogPath + " loaded")
        
    except Exception as error:
        Logger.error("Loading cogs error --> " + str(error))