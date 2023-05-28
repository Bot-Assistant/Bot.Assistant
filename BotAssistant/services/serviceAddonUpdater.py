import os
import importlib

import settings.settingBot as settingBot

import services.serviceGitHub as serviceGitHub
from services.serviceLogger import Logger


def updateAddon():

    if settingBot.addonUpdate == False:
        Logger.system("Addon update is disabled")
        return
    
    updatedAddon = False

    for root, dirs, files in os.walk("addons"):
        for file in files:
            if file == "init.py":
                
                if os.name == 'nt':
                    initFile = os.path.join(root, file).replace("\\", ".")[:-3]
                elif os.name == 'posix':
                    initFile = os.path.join(root, file).replace("/", ".")[:-3]
                else:
                    Logger.system("OS: Unknown")

                importedFile = importlib.import_module(initFile)

                if importedFile.cogEnabled == False:
                    continue
                
                if os.name == 'nt':
                    addonName = root.replace("addons\\", "")
                elif os.name == 'posix':
                    addonName = root.replace("addons/", "")
                    
                if importedFile.enableGithub != True:
                    continue
                
                repositoryVersion = serviceGitHub.getLatestRelease(importedFile.repository, importedFile.version, importedFile.author)

                if repositoryVersion == None:
                    return

                elif repositoryVersion == False:
                    Logger.update(f"Addon: {addonName} - Up to date")

                # Verify if the repository version is different from the local version
                elif repositoryVersion < importedFile.version:
                    Logger.update(f"Addon: {addonName} - BETA version")
                    
                elif repositoryVersion > importedFile.version:
                    Logger.update(f"Addon: {addonName} - Update available")

                    # Update the addon
                    Logger.update(f"Addon: {addonName} - Updating...")

                    # Download the latest release
                    serviceGitHub.downloadLatestReleaseAddons(importedFile.author, importedFile.repository, addonName)

                    updatedAddon = True

    if updatedAddon == True:
        Logger.update(f"PLEASE RESTART THE BOT TO APPLY THE CHANGES")
        os._exit(0)





            
        
                
                

                