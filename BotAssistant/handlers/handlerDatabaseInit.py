import services.serviceDatabase as serviceDatabase

def databaseInit():
    tableName = "servers"
    columns = [
        ["serverID", "bigint(20) NOT NULL"], 
        ["logsID", "bigint(20) DEFAULT NULL"], 
        ["logsLevel", "int(11) DEFAULT 1"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)
