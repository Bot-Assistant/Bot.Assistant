import services.serviceDatabase as serviceDatabase 
from services.serviceLogger import Logger

from settings.settingBot import debug


# Permet de définir le salon de logs
def setLogsID(serverID, logsID):
    requestFormat = """
                    UPDATE servers 
                    SET logsID = %s
                    WHERE serverID = %s
                    """
    requestSettings = (logsID, serverID,)
    try:
        Logger.debug("[HANDLER][CONFIGURATION] Adding a log ID to the database. SRV:" + str(serverID) + " LOGS:" + str(logsID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][CONFIGURATION] DB error setLogsID -> " + str(error))
        

# Permet de définir le niveau de logs
def setLogsLevel(serverID, logsLevel):
    requestFormat = """
                    UPDATE servers 
                    SET logsLevel = %s
                    WHERE serverID = %s
                    """
    requestSettings = (logsLevel, serverID,)
    try:
        Logger.debug("[HANDLER][CONFIGURATION] Definition of the log level in the DB. SRV:" + str(serverID) + " LOG LEVEL:" + str(logsLevel))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][CONFIGURATION] DB error setLogsLevel -> " + str(error))