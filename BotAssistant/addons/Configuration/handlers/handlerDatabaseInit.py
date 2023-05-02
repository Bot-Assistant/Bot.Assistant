import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

def databaseInit():
    if settingBot.databaseType == "MariaDB":
    
        tableName = "servers"
        columns = [
            ["logsID", "bigint DEFAULT NULL"], 
            ["logsLevel", "int DEFAULT 1"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        tableName = "permissions"
        columns = [
            ["serverID", "bigint NOT NULL"],
            ["addonName", "varchar(255) NOT NULL"],
            ["permissionName", "varchar(255) NOT NULL"],
            ["roleID", "bigint NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        
        tableName = "servers"
        columns = [
            ["logsID", "integer DEFAULT NULL"], 
            ["logsLevel", "integer DEFAULT 1"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        tableName = "permissions"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["addonName", "text NOT NULL"],
            ["permissionName", "text NOT NULL"],
            ["roleID", "integer NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)