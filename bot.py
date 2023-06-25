import sys
import time

import services.serviceBotStart as serviceBotStart
import services.serviceBotUpdater as serviceBotUpdater
import services.serviceConsoleMessages as serviceConsoleMessages

# Get Latest Version from GitHub
# Get Actual Version from settingBot.py

latestVersion = None
actualVersion = None

try:
    import services.serviceGitHub as serviceGitHub
    import settings.settingBot as settingBot

    latestVersion = serviceGitHub.getLatestRelease("Bot.Assistant", settingBot.botVersion, "Ted-18")
    actualVersion = settingBot.botVersion.replace("v", "")
except Exception as error:
    print(f"Error: {error}")

serviceConsoleMessages.logo()

# Check if the version is up-to-date
if latestVersion is None:
    serviceBotStart.start()

elif actualVersion == latestVersion:
    print(f"Your version is up to date")
    time.sleep(5)
    serviceBotStart.start()

elif actualVersion > latestVersion:
    print(f"Your version is a beta version")
    time.sleep(5)
    serviceBotStart.start()

elif actualVersion < latestVersion:
    if not serviceBotUpdater.updateBot(actualVersion, latestVersion):
        serviceBotStart.start()

else:
    print(f"An error has occurred")
    sys.exit(0)
