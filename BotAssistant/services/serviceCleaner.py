import os
import shutil
from settings.settingBot import debug
from services.serviceLogger import Logger

def clean(path):
    Logger.info("[CLEANER] Cleaning started")
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            if dirname == "__pycache__":
                Logger.debug("[CLEANER] Deleting " + os.path.join(dirpath, dirname))
                shutil.rmtree(os.path.join(dirpath, dirname))
        for filename in filenames:
            if filename == ".DS_Store":
                Logger.debug("[CLEANER] Deleting " + os.path.join(dirpath, filename))
                os.remove(os.path.join(dirpath, filename))
    Logger.info("[CLEANER] Cleaning done")
