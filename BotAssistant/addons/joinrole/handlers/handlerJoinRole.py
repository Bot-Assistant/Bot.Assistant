import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

def addRole(serverID, role_ID):
    requestFormat = """
                    INSERT INTO onMemberJoin
                    (server_ID, role_ID)
                    VALUES (%s, %s)
                    """
    requestSettings = (serverID, role_ID,)
    try:
        if debug:
            Logger.debug("[HANDLER][JOINROLE][ADD] Adding a role to the DB " + str(serverID) + " " + str(role_ID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][JOINROLE][ADD] DB error addRole -> " + str(error))
        

def deleteRole(role_ID):
    requestFormat = """
                    DELETE 
                    FROM onMemberJoin
                    WHERE role_ID = %s
                    """
    requestSettings = (role_ID,)
    try:
        if debug:
            Logger.debug("[HANDLER][JOINROLE][DELETE] Deleting a role from the DB " + str(role_ID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][JOINROLE][DELETE] DB error deleteRole -> " + str(error))
        
        
def listRole(server_ID):
    requestFormat = """
                    SELECT role_ID
                    FROM onMemberJoin
                    WHERE server_ID = %s;
                    """
    requestSettings = (server_ID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)

        if debug:
            Logger.debug("[HANDLER][JOINROLE][LIST] Retrieving the list of join roles -> " + str(result))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][JOINROLE][LIST] DB error getJoinRole -> " + str(error))