import services.serviceDatabase as serviceDatabase 
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

    
# Permet de récupérer le salon de logs
def getLogsID(server_ID):
    requestFormat = """
                    SELECT logs_ID
                    FROM servers
                    WHERE server_ID = %s;
                    """
    requestSettings = (server_ID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True: 
            Logger.debug("[HANDLER][LOGGER][GETCHANNEL] Log ID recovery -> " + str(result[0][0]))
            
        return result[0][0]
    
    except Exception as error:
        Logger.error("[HANDLER][LOGGER][GETCHANNEL] DB error getLogsID -> " + str(error))
        

# Permet de récupérer le niveau de logs
def getLogsLevel(server_ID):
    requestFormat = """
                    SELECT logs_level
                    FROM servers
                    WHERE server_ID = %s;
                    """
    requestSettings = (server_ID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True: 
            Logger.debug("[HANDLER][LOGGER][GETLEVEL] Log level recovery -> "+ str(result[0][0]))
            
        return result[0][0]
    
    except Exception as error:
        Logger.error("[HANDLER][LOGGER][GETLEVEL] DB error getLogsLevel -> " + str(error))