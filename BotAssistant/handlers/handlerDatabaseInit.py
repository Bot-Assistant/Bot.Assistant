import services.serviceDatabase as serviceDatabase

def databaseInit():
    tableName = "servers"
    columns = [
        ["serverID", "bigint NOT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)
