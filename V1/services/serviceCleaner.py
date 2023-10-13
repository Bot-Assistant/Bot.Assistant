import os
import shutil
from services.serviceLogger import Logger

def clean(path):
    Logger.info("[CLEANER] Cleaning started")

    for dirPath, dirNames, fileNames in os.walk(path):

        for dirName in dirNames:

            if dirName == "__pycache__":
                Logger.debug("[CLEANER] Deleting " + os.path.join(dirPath, dirName))
                shutil.rmtree(os.path.join(dirPath, dirName))

            if dirName == "updates":
                Logger.debug("[CLEANER] Deleting " + os.path.join(dirPath, dirName))
                shutil.rmtree(os.path.join(dirPath, dirName))

        for filename in fileNames:
            if filename == ".DS_Store":
                Logger.debug("[CLEANER] Deleting " + os.path.join(dirPath, filename))
                os.remove(os.path.join(dirPath, filename))

    Logger.info("[CLEANER] Cleaning done")
