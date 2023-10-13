import os

import settings.settingBot as settingBot


def settingBotBool(setting: str ,value: bool):

    # Convert the value to a boolean
    if value == "y":
        value = True
    elif value == "n":
        value = False
    else:
        print("Invalid answer. Restart the bot and try again.")
        os._exit(0)

    # Open the settingBot.py file
    file = open("settings/settingBot.py","r", encoding="utf-8")
    fileContent = file.read()
    file.close()

    # Edit the setting
    if value == True:
        fileContent = fileContent.replace(f"{setting} = False", f"{setting} = True")    
    elif value == False:
        fileContent = fileContent.replace(f"{setting} = True", f"{setting} = False")
    else:
        print("Invalid value. Restart the bot and try again.")
        os._exit(0)

    # Save the setting
    file = open("settings/settingBot.py","w")
    file.write(fileContent)
    file.close()

    # Update the variable
    variable = f"settingBot.{setting} = {value}"
    print(variable)
    exec(variable)


def settingBotList(setting: str, value: int, choices: dict):

    # Get the index of the value
    try:
        newValue = choices[value]
        settingBot.databaseType = newValue
    except:
        print("Invalid value. Restart the bot and try again.")
        os._exit(0)

    # Open the settingBot.py file
    file = open("settings/settingBot.py","r", encoding="utf-8")
    fileContent = file.read()
    file.close()

    # Replace the line with the new value
    line = fileContent.split("\n")
    for i in range(len(line)):
        if setting in line[i]:
            line[i] = f"{setting} = \"{newValue}\""
            break

    # Rebuild the file
    fileContent = ""
    for i in range(len(line)):
        fileContent += line[i] + "\n"

    # Remove the last \n
    fileContent = fileContent[:-1]

    # Save the setting
    file = open("settings/settingBot.py","w")
    file.write(fileContent)
    file.close()

    # Update the variable
    variable = f"settingBot.{setting} = \"{newValue}\""
    exec(variable)

