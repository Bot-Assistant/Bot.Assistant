import services.serviceDatabase as serviceDatabase 
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

# Add a server to the database when the bot join a server
def addServerID(serverID):
    requestFormat = """
                    INSERT INTO servers
                    (serverID)
                    VALUES (%s)
                    """
    requestSettings = (serverID,)
    
    try:
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
        if debug == True: 
            Logger.debug("[HANDLER][CONFIGURATION] Adding a server to the DB " + str(serverID))        
        
    except Exception as error:
        Logger.error("[HANDLER][CONFIGURATION] DB error addServerID -> " + str(error))
        
        
# Delete a server from the database when the bot leave a server
def delServerID(serverID):
    requestFormat = """
                    DELETE 
                    FROM servers
                    WHERE serverID = %s
                    """
    requestSettings = (serverID,)
    try:
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
        
        if debug == True: 
            Logger.debug("[HANDLER][CONFIGURATION] Deleting a server from the DB " + str(serverID))
            
    except Exception as error:
        Logger.error("[HANDLER][CONFIGURATION] DB error delServerID -> " + str(error))