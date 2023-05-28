import os
import importlib

import settings.settingBot as settingBot

import services.serviceGitHub as serviceGitHub
import services.serviceConsoleMessages as serviceConsoleMessages
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

                    # Print the logo
                    serviceConsoleMessages.logo()

                    Logger.update(f"Addon: {addonName} - Version: {importedFile.version} > {repositoryVersion}")

                    # Ask if you want really to update the addon
                    print(" ")
                    print("Write 'y' to update the addon, everything else to cancel")
                    update = input("Answer: ")

                    # If the answer is not "y" then cancel the update
                    if update != "y":
                        return

                    # Update the addon
                    Logger.update(f"Addon: {addonName} - Updating...")

                    # Download the latest release
                    serviceGitHub.updateLatestReleaseAddons(importedFile.author, importedFile.repository, addonName)

                    updatedAddon = True

    if updatedAddon == True:
        Logger.update(f"PLEASE RESTART THE BOT TO APPLY THE CHANGES")
        os._exit(0)





            
        
                
                

                