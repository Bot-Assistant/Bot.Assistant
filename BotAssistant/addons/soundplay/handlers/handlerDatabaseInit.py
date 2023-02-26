import services.serviceDatabase as serviceDatabase

def databaseInit():
    tableName = "addon_soundPlay_settings"
    columns = [
        ["serverID", "BIGINT NOT NULL"],
        ["userID", "BIGINT NOT NULL"],
        ["volume", "FLOAT NOT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)

    tableName = "addon_soundPlay_soundsList"
    columns = [
        ["serverID", "BIGINT NOT NULL"],
        ["folderName", "VARCHAR(255) NOT NULL"],
        ["soundName", "VARCHAR(255) NOT NULL"],
        ["soundPlayCount", "INT DEFAULT 0"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)