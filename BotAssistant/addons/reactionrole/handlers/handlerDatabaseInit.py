import services.serviceDatabase as serviceDatabase

def databaseInit():
    tableName = "addon_reactionrole_reactions"
    columns = [
        ["serverID", "BIGINT NOT NULL"],
        ["channelID", "BIGINT NOT NULL"],
        ["messageID", "BIGINT NOT NULL"],
        ["roleID", "BIGINT NOT NULL"],
        ["emote", "VARCHAR(255) NOT NULL"],
        ["reactionType", "INT NOT NULL"]
    ]
    serviceDatabase.databaseCreation(tableName, columns)