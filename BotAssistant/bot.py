import os

import services.serviceBotStart as serviceBotStart

# Get Latest Version from GitHub
# Get Actual Version from settingBot.py
try:
    import services.serviceGitHub as serviceGitHub
    import settings.settingBot as settingBot
    latestVersion = serviceGitHub.getLatestRelease("Bot.Assistant", settingBot.botVersion, "Ted-18")
    actualVersion = settingBot.botVersion.replace("v", "")
except Exception as error:
    print(f"Error: {error}")

# Print text logo
import services.serviceConsoleMessages as serviceConsoleMessages
serviceConsoleMessages.logo()

# Check if the version is up to date
if latestVersion == None:
    serviceBotStart.start()

elif actualVersion == latestVersion:
    print(f"Your version is up to date")
    os.system("timeout 5")
    serviceBotStart.start()

elif actualVersion > latestVersion:
    print(f"Your version is a beta version")
    os.system("timeout 5")
    serviceBotStart.start()

elif actualVersion < latestVersion:
    print(f"Your version is outdated but this v0.10.4-alpha can't update automatically")
    print("Skipping update...")
    os.system("timeout 5")
    serviceBotStart.start()

else:
    print(f"An error has occurred")
    os._exit(0)