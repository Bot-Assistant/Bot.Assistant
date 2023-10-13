import services.serviceDatabase as serviceDatabase
from services.serviceLogger import Logger


# Verify if the role has the permission bool
def roleHasPermission(serverID, permissionName, roleID):
    requestFormat = """
                    SELECT *
                    FROM permissions
                    WHERE serverID = %s AND permissionName = %s AND roleID = %s
                    """
    requestSettings = (serverID, permissionName, roleID)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        Logger.debug("[HANDLER][BOTASSISTANT] Verify if the role has the permission " + str(result))
            
        if result == []:
            return False
        else:
            return True
        
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error roleHasPermission -> " + str(error))
        return False