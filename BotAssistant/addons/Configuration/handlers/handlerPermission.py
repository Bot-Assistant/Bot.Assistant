import services.serviceDatabase as serviceDatabase 
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug


# Add permissions to the database
def addPermission(serverID, addonName, permissionName, roleID):
    requestFormat = """
                    INSERT INTO permissions
                    (serverID, addonName, permissionName, roleID)
                    VALUES (%s, %s, %s, %s)
                    """
    requestSettings = (serverID, addonName, permissionName, roleID)
    
    try:
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
        if debug == True: 
            Logger.debug("[HANDLER][BOTASSISTANT] Adding a permission to the DB " + str(serverID))        
        
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error addPermission -> " + str(error))


# Remove permissions from the database
def removePermission(serverID, permissionName, roleID):
    requestFormat = """
                    DELETE 
                    FROM permissions
                    WHERE serverID = %s AND permissionName = %s AND roleID = %s
                    """
    requestSettings = (serverID, permissionName, roleID)
    try:
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
        
        if debug == True: 
            Logger.debug("[HANDLER][BOTASSISTANT] Deleting a permission from the DB " + str(serverID))
            
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error delPermission -> " + str(error))


# Get permissions with a specific roleID
def getPermissionsByRoleID(serverID, roleID):
    requestFormat = """
                    SELECT addonName, permissionName
                    FROM permissions
                    WHERE serverID = %s AND roleID = %s
                    """
    requestSettings = (serverID, roleID)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True: 
            Logger.debug("[HANDLER][BOTASSISTANT] Get permissions from the DB " + str(result))
            
        return result
        
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error getPermissionsByRoleID -> " + str(error))


# Get list of roles in the database
def getRoles(serverID):
    requestFormat = """
                    SELECT roleID
                    FROM permissions
                    WHERE serverID = %s
                    """
    requestSettings = (serverID)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True: 
            Logger.debug("[HANDLER][BOTASSISTANT] Get roles from the DB " + str(result))
            
        return result
        
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error getRoles -> " + str(error))


def permissionExists(serverID, permissionName, roleID):
    requestFormat = """
                    SELECT addonName, permissionName, roleID
                    FROM permissions
                    WHERE serverID = %s AND permissionName = %s AND roleID = %s
                    """
    requestSettings = (serverID, permissionName, roleID)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True: 
            Logger.debug("[HANDLER][BOTASSISTANT] Get permissions from the DB " + str(result))
            
        if result == []:
            return False
        else:
            return True
        
    except Exception as error:
        Logger.error("[HANDLER][BOTASSISTANT] DB error permissionExists -> " + str(error))