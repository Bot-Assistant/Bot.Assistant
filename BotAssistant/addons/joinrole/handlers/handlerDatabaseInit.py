from services.serviceDatabase import makeRequest
from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug

def databaseInit():
    requestFormat = """
                    CREATE TABLE IF NOT EXISTS onMemberJoin
                    (
                        server_ID BIGINT NOT NULL,
                        role_ID BIGINT NOT NULL
                    ) ENGINE=InnoDB CHARSET=utf8mb4;
                    """
    requestSettings = ()

    try:
        Logger.database("[HANDLER][JOINROLE][INIT]Join role table init")
        makeRequest(requestFormat, requestSettings)
    
    except Exception as error:
        Logger.error("[HANDLER][JOINROLE][INIT]DB error databaseInit -> " + str(error))
