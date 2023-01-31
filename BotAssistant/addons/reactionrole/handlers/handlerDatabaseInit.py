from services.serviceDatabase import makeRequest
from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug

def databaseInit():
    requestFormat = """
                    CREATE TABLE IF NOT EXISTS onRawReactionAdd
                    (
                        ID INT NOT NULL AUTO_INCREMENT,
                        server_ID BIGINT NOT NULL,
                        channel_ID BIGINT NOT NULL,
                        message_ID BIGINT NOT NULL,
                        role_ID BIGINT NOT NULL,
                        emote VARCHAR(255) NOT NULL,
                        reaction_type INT NOT NULL,
                        PRIMARY KEY (ID)
                    ) ENGINE=InnoDB CHARSET=utf8mb4;
                    """
    requestSettings = ()

    try:
        Logger.database("[HANDLER][REACTIONROLE][INIT]Reaction role table init")
        makeRequest(requestFormat, requestSettings)
    
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE][INIT]DB error databaseInit -> " + str(error))