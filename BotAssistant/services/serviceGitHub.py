import requests
import time

from services.serviceLogger import Logger


def getLatestRelease(repository, version, author):
    url = f"https://api.github.com/repos/{author}/{repository}/releases/latest"
    repositoryReleaseUrl = f"https://github.com/{author}/{repository}/releases/latest"
    gitRepository = requests.get(url)

    try:
        gitRepository.json()['tag_name']
    except:
        Logger.update(f"Addon: {repository} ({version})")
        Logger.update("Unable to get the latest release")
        time.sleep(5)
        return

    repositoryVersion = gitRepository.json()['tag_name'].replace("v", "")

    # If the version is bigger than the latest release, it means that the version is a beta version
    if version > repositoryVersion:
        Logger.update(f"Addon: {repository} ({version})")
        Logger.update("🔰 Beta version")
        time.sleep(5)
        return

    # If the version is different from the latest release, it means that a new version is available
    elif version != repositoryVersion:
        Logger.update(f"Addon: {repository} ({version})")
        Logger.update(f"⚠️  New version available: {repositoryVersion}")
        Logger.update(f"Download link: {repositoryReleaseUrl}")
        time.sleep(5)
        return
    
    else:
        Logger.update(f"Addon: {repository} ({version})")
        Logger.update("✅ Up to date")
        return