import services.serviceDatabase as serviceDatabase 
from services.serviceLogger import Logger

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
        
        Logger.debug("[HANDLER][BOTASSISTANT] Adding a server to the DB " + str(serverID))        
        
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error addServerID -> " + str(error))
        
        
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
        
        
        Logger.debug("[HANDLER][BOTASSISTANT] Deleting a server from the DB " + str(serverID))
            
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error delServerID -> " + str(error))

# Get servers from the database
def getServers():
    requestFormat = """
                    SELECT serverID
                    FROM servers
                    """
    requestSettings = ()
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        Logger.debug("[HANDLER][BOTASSISTANT] Get servers from the DB " + str(result))
            
        return result
        
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error getServers -> " + str(error))