import os
from services.serviceLogger import consoleLogger as Logger

# Write a message in a file (create the file if it does not exist)
def fileWrite(file, message):
    fileWrited = open(file, "a", encoding="utf-8")
    fileWrited.write("\n" + message)
    fileWrited.close()

# Create a folder if it does not exist
def createFolder(folderName):
    if not os.path.exists(folderName):
        try:
            os.mkdir(folderName)
            Logger.info("[FILEMANAGER]" + folderName + " folder was created")
        except:
            Logger.error("[FILEMANAGER]" + "Unable to create "+ folderName +" folder")
    else:
        Logger.info("[FILEMANAGER]" + folderName + " folder already exists")