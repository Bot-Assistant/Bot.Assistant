import services.serviceDatabase as serviceDatabase

def databaseInit():
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