import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

# Save volume in the database
def saveVolume(server_ID, user_ID, volume):
    requestFormat = """
                    INSERT INTO addon_soundPlay_settings
                    (serverID, userID, volume)
                    VALUES (%s, %s, %s)
                    """
    requestSettings = (server_ID, user_ID, volume)
    try:
        if debug == True:
            Logger.debug("[HANDLER][SOUNDPLAY] Saving volume " + str(server_ID) + " " + str(user_ID) + " " + str(volume))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][SOUNDPLAY] DB error saveVolume -> " + error)


# Get volume from the database
def getVolume(server_ID, user_ID):
    requestFormat = """
                    SELECT volume
                    FROM addon_soundPlay_settings
                    WHERE serverID = %s AND userID = %s
                    """
    requestSettings = (server_ID, user_ID)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True:
            Logger.debug("[HANDLER][SOUNDPLAY] Retrieving volume -> " + str(server_ID) + " " + str(user_ID))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][SOUNDPLAY] DB error getVolume -> " + error)


# Update volume in the database
def updateVolume(server_ID, user_ID, volume):
    requestFormat = """
                    UPDATE addon_soundPlay_settings
                    SET volume = %s
                    WHERE serverID = %s AND userID = %s
                    """
    requestSettings = (volume, server_ID, user_ID)
    try:
        if debug == True:
            Logger.debug("[HANDLER][SOUNDPLAY] Updating volume " + str(server_ID) + " " + str(user_ID) + " " + str(volume))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][SOUNDPLAY] DB error updateVolume -> " + error)