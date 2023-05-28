import os
import time
import requests

from services.serviceLogger import Logger
import services.serviceFileManager as serviceFileManager

def updateBot(actuelVersion, latestVersion):


    # █ █▄░█ █ ▀█▀
    # █ █░▀█ █ ░█░

    # DON'T CHANGE THIS IF YOU DON'T KNOW WHAT YOU'RE DOING
    # You can make a fork of the bot and change the repository and author variables
    repository = "Bot.Assistant"
    author = "Ted-18"

    # Print text logo
    import services.serviceConsoleMessages as serviceConsoleMessages
    serviceConsoleMessages.logo()
    
    # Ask if you want to update the bot
    print("Write 'update' to update the bot, everything else to cancel")
    update = input("Answer: ")

    # If the answer is not "update" then cancel the update
    if update != "update":
        return False
    
    # Get the latest version
    if latestVersion == None:
        return False
    


    # █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄
    # █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀

    # Get the download URL
    downloadURL = f"https://github.com/{author}/{repository}/archive/refs/tags/v{latestVersion}.zip"

    # Create the folder "updates" if it doesn't exist
    serviceFileManager.createFolder("updates")

    # DOWNLOAD
    Logger.update(f"Repository: {repository} - Downloading...")

    response = requests.get(downloadURL)
    with open(f"updates/{repository}-{latestVersion}.zip", "wb") as f:
        f.write(response.content)
    
    Logger.update(f"Repository: {repository} - Download complete")


    # EXTRACT
    Logger.update(f"Repository: {repository} - Extracting...")

    serviceFileManager.extractZip(f"updates/{repository}-{latestVersion}.zip", f"updates/")

    Logger.update(f"Repository: {repository} - Extract complete")


    # DELETE ZIP
    Logger.update(f"Repository: {repository} - Deleting zip file...")

    # Delete the zip file
    serviceFileManager.deleteFile(f"updates/{repository}-{latestVersion}.zip")

    Logger.update(f"Repository: {repository} - Zip file deleted")



    # █░█ █▀█ █▀▄ ▄▀█ ▀█▀ █▀▀
    # █▄█ █▀▀ █▄▀ █▀█ ░█░ ██▄

    serviceConsoleMessages.logo()

    # Ask if you want really to update the bot
    print("Write 'overwrite' to overwrite the bot, everything else to cancel")
    print("WARNING: This will overwrite the bot files but not the addons and the settings")

    overwrite = input("Answer: ")

    # If the answer is not "overwrite" then cancel the update
    if overwrite != "overwrite":
        return False
    
    # Replace only the files different from the repository
    Logger.update(f"Repository: {repository} - Replacing files...")

    serviceFileManager.replaceFolder(f"updates/{repository}-{latestVersion}/BotAssistant/", f".")

    Logger.update(f"Repository: {repository} - Files replaced")


    
    # █▀▀ █░░ █▀▀ ▄▀█ █▄░█ █▀▀ █▀█
    # █▄▄ █▄▄ ██▄ █▀█ █░▀█ ██▄ █▀▄

    # DELETE FOLDER
    Logger.update(f"Repository: {repository} - Deleting folder...")

    # Delete the folder
    serviceFileManager.deleteFolder(f"updates/{repository}-{latestVersion}/")

    Logger.update(f"Repository: {repository} - Folder deleted")


    serviceConsoleMessages.logo()

    Logger.system(f"Bot updated from v{actuelVersion} to v{latestVersion}")
    Logger.system(f"Restart the bot to apply the changes")

    time.sleep(10)

    os._exit(0)


    