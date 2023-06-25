import sys
import time

import services.serviceDependencies as serviceDependencies
import services.serviceBotStart as serviceBotStart
import services.serviceBotUpdater as serviceBotUpdater
import services.serviceConsoleMessages as serviceConsoleMessages
import settings.settingDependencies as settingDependencies
import settings.settingBot as settingBot
import services.serviceGitHub as serviceGitHub

def check_version():
    latestVersion = None
    actualVersion = None

    try:
        latestVersion = serviceGitHub.getLatestRelease("Bot.Assistant", settingBot.botVersion, "Ted-18")
        actualVersion = settingBot.botVersion.replace("v", "")
    except Exception as error:
        print(f"Error: {error}")

    serviceConsoleMessages.logo()

    # Check if the version is up-to-date
    if latestVersion is None:
        serviceBotStart.start()
    elif actualVersion == latestVersion:
        print("Your version is up to date")
        time.sleep(5)
        serviceBotStart.start()
    elif actualVersion > latestVersion:
        print("Your version is a beta version")
        time.sleep(5)
        serviceBotStart.start()
    elif actualVersion < latestVersion:
        if not serviceBotUpdater.updateBot(actualVersion, latestVersion):
            serviceBotStart.start()
    else:
        print("An error has occurred")
        sys.exit(0)

def initialization():
    serviceDependencies.installDependenciesFromList(settingDependencies.dependenciesList)
    check_version()

initialization()
