import services.serviceDatabase as serviceDatabase 
from services.serviceLogger import consoleLogger

from settings.settingBot import debug


# Permet de définir le salon de logs
def setLogsID(server_ID, logs_ID):
    requestFormat = """
                    UPDATE servers 
                    SET logs_ID = %s
                    WHERE server_ID = %s
                    """
    requestSettings = (logs_ID, server_ID,)
    try:
        if debug == True: 
            consoleLogger.debug("[HANDLER][CONFIGURATION] Adding a log ID to the database. SRV:" + str(server_ID) + " LOGS:" + str(logs_ID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        consoleLogger.error("[HANDLER][CONFIGURATION] DB error setLogsID -> " + str(error))
        

# Permet de définir le niveau de logs
def setLogsLevel(server_ID, logs_level):
    requestFormat = """
                    UPDATE servers 
                    SET logs_level = %s
                    WHERE server_ID = %s
                    """
    requestSettings = (logs_level, server_ID,)
    try:
        if debug == True: 
            consoleLogger.debug("[HANDLER][CONFIGURATION] Definition of the log level in the DB. SRV:" + str(server_ID) + " LOG LEVEL:" + str(logs_level))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        consoleLogger.error("[HANDLER][CONFIGURATION] DB error setLogsLevel -> " + str(error))