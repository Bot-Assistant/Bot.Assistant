import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

# Permet de créer un rôle de réaction dans la base de données
def createReactionRole(serverID, channelID, messageID, roleID, emote, reactionType):
    requestFormat = """
                    INSERT INTO addon_reactionrole_reactions
                    (serverID, channelID, messageID, roleID, emote, reactionType)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
    requestSettings = (serverID, channelID, messageID, roleID, emote, reactionType)
    try:
        if debug == True:
            Logger.debug("[HANDLER][REACTIONROLE] Reaction role create " + str(serverID) + " " + str(messageID) + " " + str(roleID) + " " + str(emote) + " " + str(reactionType))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error createReactionRole -> " + str(error))
            

#Permet de supprimer un rôle de réaction dans la base de données
def deleteReactionRole(serverID, ID):
    requestFormat = """
                    DELETE 
                    FROM addon_reactionrole_reactions
                    WHERE serverID = %s AND ID = %s
                    """
    requestSettings = (serverID, ID)
    try:
        if debug == True:
            Logger.debug("[HANDLER][REACTIONROLE] Deleting reaction role from the DB " + str(ID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error deleteRole -> " + str(error))
            

#Permet de récupérer la liste des rôles de réaction dans la base de données
def getReactionRole(serverID):
    requestFormat = """
                    SELECT ID, channelID, messageID, roleID, emote, reactionType
                    FROM addon_reactionrole_reactions
                    WHERE serverID = %s;
                    """
    requestSettings = (serverID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True:
            Logger.debug("[HANDLER][REACTIONROLE] Retrieving the list of reaction roles -> " + str(serverID))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error getReactionRole -> " + str(error))