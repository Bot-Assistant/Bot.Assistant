import os
import re
import mysql.connector

import settings.settingBot as settingBot

import services.serviceConsoleMessages as serviceConsoleMessages

def install(defaultDatabase: str):

    if os.path.exists("settings/settingDatabase.py"):
        return

    serviceConsoleMessages.logo()
    
    if settingBot.databaseType == "SQLite":

        print("Please enter the name of the database")
        sqliteName = input("Answer: ")
        
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
        
        print("Please enter the information of the database")
        print("Enter the host name: ")
        databaseHost = input("Answer: ")

        print("Enter the database name: ")
        databaseName = input("Answer: ")

        print("Enter the user name: ")
        databaseUser = input("Answer: ")

        print("Enter the password: ")
        databasePassword = input("Answer: ")

        # Edit the setting
        defaultDatabase = defaultDatabase.replace("defaultHostName", databaseHost)
        defaultDatabase = defaultDatabase.replace("defaultDatabaseName", databaseName)
        defaultDatabase = defaultDatabase.replace("defaultUserName", databaseUser)
        defaultDatabase = defaultDatabase.replace("defaultPassword", databasePassword)

        # Test the connection
        try:
            mysql.connector.connect(host=databaseHost, user=databaseUser, password=databasePassword, database=databaseName)
        except:
            print("The connection to the database failed, please retry")
            os._exit(0)

        # Write the file
        with open("settings/settingDatabase.py", "w") as file:
            file.write(defaultDatabase)