import filecmp
import os
import shutil

from services.serviceLogger import Logger

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


# Delete a folder if it exists
def deleteFolder(folderName):
    if os.path.exists(folderName):
        try:
            shutil.rmtree(folderName)
            Logger.info("[FILEMANAGER]" + folderName + " folder was deleted")
        except:
            Logger.error("[FILEMANAGER]" + "Unable to delete "+ folderName +" folder")
    else:
        Logger.info("[FILEMANAGER]" + folderName + " folder does not exist")


# Copy a folder if it exists
def copyFolder(folderName, destination):
    if os.path.exists(folderName):
        try:
            shutil.copytree(folderName, destination)
            Logger.info("[FILEMANAGER]" + folderName + " folder was copied")
        except:
            Logger.error("[FILEMANAGER]" + "Unable to copy "+ folderName +" folder")
    else:
        Logger.info("[FILEMANAGER]" + folderName + " folder does not exist")


def extractZip(zipFile, destination):
    if os.path.exists(zipFile):
        try:
            shutil.unpack_archive(zipFile, destination)
            Logger.info("[FILEMANAGER]" + zipFile + " was extracted")
        except:
            Logger.error("[FILEMANAGER]" + "Unable to extract "+ zipFile)
    else:
        Logger.info("[FILEMANAGER]" + zipFile + " does not exist")


def deleteFile(file):
    if os.path.exists(file):
        try:
            os.remove(file)
            Logger.info("[FILEMANAGER]" + file + " was deleted")
        except Exception as error:
            Logger.error("[FILEMANAGER]" + "Unable to delete "+ str(error))
    else:
        Logger.info("[FILEMANAGER]" + file + " does not exist")



def replaceFolder(source, destination):

    if os.path.exists(source):
        try:

            for root, dirs, files in os.walk(source):
                for file in files:

                    sourcePath = os.path.join(root, file)
                    destinationPath = os.path.join(destination, os.path.relpath(sourcePath, source))

                   
                    if os.path.exists(destinationPath):
                        
                        if not filecmp.cmp(sourcePath, destinationPath):
                            
                            shutil.copy2(sourcePath, destinationPath)
                            Logger.debug("[FILEMANAGER] " + destinationPath + " was replaced")
                        else:
                            Logger.debug("[FILEMANAGER] " + destinationPath + " is the same")
                    else:
                       
                        if not os.path.exists(os.path.dirname(destinationPath)):

                            os.makedirs(os.path.dirname(destinationPath))

                            Logger.debug("[FILEMANAGER] " + os.path.dirname(destinationPath) + " folder was created")

                        shutil.copy2(sourcePath, destinationPath)

                        Logger.debug("[FILEMANAGER] " + destinationPath + " does not exist, copied from source")
        except:
            Logger.debug("[FILEMANAGER] Unable to replace "+ source)
    else:
        Logger.error("[FILEMANAGER] " + source + " does not exist")
