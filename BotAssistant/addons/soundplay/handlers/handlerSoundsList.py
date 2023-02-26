import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug


# ADD SOUND
# Add a sound in the database
def addSound(server_ID, folderName, soundName, soundPlayCount):
    requestFormat = """
                    INSERT INTO addon_soundPlay_soundsList (serverID, folderName, soundName, soundPlayCount)
                    VALUES (%s, %s, %s, %s)
                    """
    requestSettings = (server_ID, folderName, soundName, soundPlayCount)
    try:
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
        if debug == True:
            Logger.debug("[HANDLER][SOUNDPLAY] Adding sound -> " + str(server_ID) + " " + str(folderName) + " " + str(soundName) + " " + str(soundPlayCount))
    
    except Exception as error:
        Logger.error("[HANDLER][SOUNDPLAY] DB error addSound -> " + str(error))



# REMOVE SOUND
# Remove a sound from the database
def removeSound(server_ID, folderName, soundName):
    requestFormat = """
                    DELETE FROM addon_soundPlay_soundsList
                    WHERE serverID = %s AND folderName = %s AND soundName = %s
                    """
    requestSettings = (server_ID, folderName, soundName)
    try:
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
        if debug == True:
            Logger.debug("[HANDLER][SOUNDPLAY] Removing sound -> " + str(server_ID) + " " + str(folderName) + " " + str(soundName))
    
    except Exception as error:
        Logger.error("[HANDLER][SOUNDPLAY] DB error removeSound -> " + str(error))



# UPDATE SOUND PLAY COUNT
# Update sound play count in the database
def updateSoundPlayCount(server_ID, folderName, soundName, soundPlayCount):
    requestFormat = """
                    UPDATE addon_soundPlay_soundsList
                    SET soundPlayCount = %s
                    WHERE serverID = %s AND folderName = %s AND soundName = %s
                    """
    requestSettings = (soundPlayCount, server_ID, folderName, soundName)
    try:
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
        if debug == True:
            Logger.debug("[HANDLER][SOUNDPLAY] Updating sound play count -> " + str(server_ID) + " " + str(folderName) + " " + str(soundName) + " " + str(soundPlayCount))
    
    except Exception as error:
        Logger.error("[HANDLER][SOUNDPLAY] DB error updateSoundPlayCount -> " + str(error))



# GETTERS
# Get all sounds information from the database
# Returned data: (folderName, soundName, soundPlayCount)
def getAllSoundsInfo(server_ID):
    requestFormat = """
                    SELECT folderName, soundName, soundPlayCount
                    FROM addon_soundPlay_soundsList
                    WHERE serverID = %s
                    """
    requestSettings = (server_ID)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True:
            Logger.debug("[HANDLER][SOUNDPLAY] Retrieving all sounds information -> " + str(server_ID))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][SOUNDPLAY] DB error getAllSoundsInfo -> " + str(error))