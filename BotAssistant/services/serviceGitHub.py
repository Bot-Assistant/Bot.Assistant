import requests
import time
import re

import services.serviceFileManager as serviceFileManager
from services.serviceLogger import Logger


def getLatestRelease(repository, version, author):
    url = f"https://api.github.com/repos/{author}/{repository}/releases/latest"
    gitRepository = requests.get(url)

    try:
        gitRepository.json()['tag_name']
    except:
        Logger.update(f"{repository} ({version})")

        ipPattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

        error = gitRepository.json()['message']

        if ipPattern.search(error):
            error = "GITHUB : API rate limit exceeded for your IP address."
            Logger.warning(error)
            time.sleep(5)

        else:
            Logger.critical(error)
            time.sleep(5)

        return None

    repositoryVersion = gitRepository.json()['tag_name'].replace("v", "")

    if repositoryVersion != version:
        return repositoryVersion
    else:
        return False
    
import requests
import json

def updateLatestReleaseAddons(author, repository, addonName):
    apiURL = f"https://api.github.com/repos/{author}/{repository}/releases/latest"
    
    # Send a GET request to the Github API to get information about the latest release
    response = requests.get(apiURL)
    data = json.loads(response.text)

    # Get the tag_name of the latest release
    latestVersion = data['tag_name']
    
    # Construct the download URL using the latestVersion
    downloadURL = f"https://github.com/{author}/{repository}/archive/refs/tags/{latestVersion}.zip"


    serviceFileManager.createFolder("updates")


    # DOWNLOAD
    Logger.update(f"Addon: {repository} - Downloading...")

    response = requests.get(downloadURL)
    with open(f"updates/{repository}-{latestVersion}.zip", "wb") as f:
        f.write(response.content)
    
    Logger.update(f"Addon: {repository} - Download complete")
    

    # EXTRACT
    Logger.update(f"Addon: {repository} - Extracting...")

    serviceFileManager.extractZip(f"updates/{repository}-{latestVersion}.zip", f"updates/")
    
    Logger.update(f"Addon: {repository} - Extract complete")

    

    # DELETE ZIP
    Logger.update(f"Addon: {repository} - Deleting zip file...")

    # Delete the zip file
    serviceFileManager.deleteFile(f"updates/{repository}-{latestVersion}.zip")

    Logger.update(f"Addon: {repository} - Zip file deleted")

    

    # Replace only the files different from the repository
    Logger.update(f"Addon: {repository} - Replacing files...")

    serviceFileManager.replaceFolder(f"updates/{repository}-{latestVersion}/{addonName}/", f"addons/{addonName}/")

    Logger.update(f"Addon: {repository} - Files replaced")


    # DELETE FOLDER
    Logger.update(f"Addon: {repository} - Deleting folder...")

    # Delete the folder
    serviceFileManager.deleteFolder(f"updates/{repository}-{latestVersion}")

    Logger.update(f"Addon: {repository} - Folder deleted")

    

    Logger.update(f"Addon: {repository} - Update complete")

