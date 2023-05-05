import services.serviceDatabase as serviceDatabase 
from services.serviceLogger import Logger

from settings.settingBot import debug

    
# Permet de récupérer le salon de logs
def getLogsID(serverID):
    requestFormat = """
                    SELECT logsID
                    FROM servers
                    WHERE serverID = %s;
                    """
    requestSettings = (serverID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        Logger.debug("[HANDLER][LOGGER][GETCHANNEL] Log ID recovery -> " + str(result[0][0]))
            
        return result[0][0]
    
    except Exception as error:
        Logger.error("[HANDLER][LOGGER][GETCHANNEL] DB error getLogsID -> " + str(error))
        

# Permet de récupérer le niveau de logs
def getLogsLevel(serverID):
    requestFormat = """
                    SELECT logsLevel
                    FROM servers
                    WHERE serverID = %s;
                    """
    requestSettings = (serverID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        Logger.debug("[HANDLER][LOGGER][GETLEVEL] Log level recovery -> "+ str(result[0][0]))
            
        return result[0][0]
    
    except Exception as error:
        Logger.error("[HANDLER][LOGGER][GETLEVEL] DB error getLogsLevel -> " + str(error))