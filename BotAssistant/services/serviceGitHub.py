import requests
import time

from services.serviceLogger import consoleLogger as Logger


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


    if version != gitRepository.json()['tag_name']:
        Logger.update(f"Addon: {repository} ({version})")
        Logger.update(f"New version available: {gitRepository.json()['tag_name']}")
        Logger.update(f"Download link: {repositoryReleaseUrl}")
        time.sleep(5)
        return
    
    else:
        Logger.update(f"Addon: {repository} ({version})")
        Logger.update("✅ Up to date")
        return