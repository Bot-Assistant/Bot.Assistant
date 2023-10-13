import os

import services.serviceTokenVerificator as tokenVerificator

import services.serviceConsoleMessages as serviceConsoleMessages


def install(defaultToken: str):

    if os.path.exists("settings/settingToken.py"):
        return

    serviceConsoleMessages.logo()

    print("Please enter the token of the bot")
    token = input("Answer: ")

    serviceConsoleMessages.logo()
    valid = tokenVerificator.verification(token)

    if not valid:
        serviceConsoleMessages.logo()
        print("Something went wrong!")
        print("")
        print("Verify this things:")
        print("1. You are connected to the internet")
        print("2. The token is valid and is not expired")
        print("3. You have enabled all the intents in the developer portal")
        os._exit(0)

    tokenValue = f"token = \"{token}\""

    # Edit the setting
    defaultToken = defaultToken.replace("token = \"\"", tokenValue)

    # Write the file
    with open("settings/settingToken.py", "w") as file:
        file.write(defaultToken)