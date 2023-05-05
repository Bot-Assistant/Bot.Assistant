import os
import re

import settings.settingBot as settingBot

import tools.install.messages.messageLogo as messageLogo

def install(defaultDatabase: str):

    if os.path.exists("settings/settingDatabase.py"):
        return

    messageLogo.send()
    
    if settingBot.databaseType == "SQLite":

        sqliteName = input("Enter the name of the database: ")
        
        # Verify if the database name is valid
       

        pattern = re.compile("^[a-zA-Z0-9_]+$")

        if not pattern.match(sqliteName):
            print("The database name is not valid, please retry")
            os._exit(0)

        # Edit the setting
        defaultDatabase = defaultDatabase.replace("defaultFile", sqliteName)

        # Write the file
        with open("settings/settingDatabase.py", "w") as file:
            file.write(defaultDatabase)


    elif settingBot.databaseType == "MariaDB":

        databaseHost = input("Enter the database host: ")
        databaseName = input("Enter the database name: ")
        databaseUser = input("Enter the database user: ")
        databasePassword = input("Enter the database password: ")

        # Edit the setting
        defaultDatabase = defaultDatabase.replace("defaultHostName", databaseHost)
        defaultDatabase = defaultDatabase.replace("defaultDatabaseName", databaseName)
        defaultDatabase = defaultDatabase.replace("defaultUserName", databaseUser)
        defaultDatabase = defaultDatabase.replace("defaultPassword", databasePassword)

        # Write the file
        with open("settings/settingDatabase.py", "w") as file:
            file.write(defaultDatabase)