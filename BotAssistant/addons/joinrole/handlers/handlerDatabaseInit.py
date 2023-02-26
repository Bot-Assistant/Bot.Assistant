import services.serviceDatabase as serviceDatabase

# Create the database if it does not exist
def databaseInit():
    # Table structure
    tableName = "addon_joinrole_roles"
    columns = [
        ["serverID", "BIGINT NOT NULL"], 
        ["roleID", "BIGINT NOT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)

