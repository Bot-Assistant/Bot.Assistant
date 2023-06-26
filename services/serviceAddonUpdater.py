import os
import importlib
from services.serviceLogger import Logger
import services.serviceConsoleMessages as serviceConsoleMessages
import services.serviceGitHub as serviceGitHub
import settings.settingBot as settingBot

def updateAddon():
    if not settingBot.addonUpdate:
        Logger.system("Addon update is disabled")
        return
    
    updatedAddon = False

    for root, dirs, files in os.walk("addons"):
        for file in files:
            if file == "init.py":
                initFile = os.path.join(root, file).replace(os.sep, ".")[:-3]
                importedFile = importlib.import_module(initFile)

                if not importedFile.cogEnabled:
                    continue
                
                addonName = root.replace("addons" + os.sep, "")

                if not importedFile.enableGithub:
                    continue
                
                repositoryVersion = serviceGitHub.getLatestRelease(importedFile.repository, importedFile.version, importedFile.author)

                if repositoryVersion is None:
                    return

                elif repositoryVersion is False:
                    Logger.update(f"Addon: {addonName} - Up to date")

                # Verify if the repository version is different from the local version
                elif repositoryVersion < importedFile.version:
                    Logger.update(f"Addon: {addonName} - BETA version")
                    
                elif repositoryVersion > importedFile.version:
                    Logger.update(f"Addon: {addonName} - Update available")
                    serviceConsoleMessages.logo()
                    Logger.update(f"Addon: {addonName} - Version: {importedFile.version} > {repositoryVersion}")

                    # Ask if you really want to update the addon
                    print(" ")
                    print("Write 'y' to update the addon, anything else to cancel")
                    update = input("Answer: ")

                    # If the answer is not "y", cancel the update
                    if update != "y":
                        return

                    # Update the addon
                    Logger.update(f"Addon: {addonName} - Updating...")
                    serviceGitHub.updateLatestReleaseAddons(importedFile.author, importedFile.repository, addonName)

                    updatedAddon = True

    if updatedAddon:
        Logger.update("PLEASE RESTART THE BOT TO APPLY THE CHANGES")
        os._exit(0)
