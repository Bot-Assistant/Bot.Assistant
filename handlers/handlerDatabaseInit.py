import os

import services.serviceDatabase as serviceDatabase
from services.serviceLogger import Logger

import settings.settingBot as settingBot

def databaseInit():
    if settingBot.databaseType == "MariaDB":

        tableName = "servers"
        columns = [
            ["serverID", "BIGINT NOT NULL"]
        ]

        serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        
        tableName = "servers"
        columns = [
            ["serverID", "integer NOT NULL"]
        ]
        
        serviceDatabase.databaseCreation(tableName, columns)


    else:
        Logger.critical("The database settings are not correct")
        Logger.critical("Please check the settingBot.py file")
        os._exit(1)