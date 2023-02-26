import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

def addRole(serverID, roleID):
    requestFormat = """
                    INSERT INTO addon_joinrole_roles
                    (serverID, roleID)
                    VALUES (%s, %s)
                    """
    requestSettings = (serverID, roleID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][JOINROLE][ADD] Adding a role to the DB " + str(serverID) + " " + str(roleID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][JOINROLE][ADD] DB error addRole -> " + str(error))
        

def deleteRole(serverID, roleID):
    requestFormat = """
                    DELETE FROM addon_joinrole_roles
                    WHERE serverID = %s AND roleID = %s;
                    """
    requestSettings = (serverID, roleID,)
    try:
        if debug == True:
            Logger.debug("[HANDLER][JOINROLE][DELETE] Deleting a role from the DB " + str(roleID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][JOINROLE][DELETE] DB error deleteRole -> " + str(error))
        
        
def listRole(serverID):
    requestFormat = """
                    SELECT roleID
                    FROM addon_joinrole_roles
                    WHERE serverID = %s;
                    """
    requestSettings = (serverID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if debug == True:
            Logger.debug("[HANDLER][JOINROLE][LIST] Retrieving the list of join roles -> " + str(result))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][JOINROLE][LIST] DB error listRole -> " + str(error))