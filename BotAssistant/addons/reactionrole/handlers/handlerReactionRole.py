import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import consoleLogger as Logger

from settings.settingBot import debug

# Permet de créer un rôle de réaction dans la base de données
def createReactionRole(server_ID, channel_ID, message_ID, role_ID, emote, reactionType):
    requestFormat = """
                    INSERT INTO onRawReactionAdd
                    (server_ID, channel_ID, message_ID, role_ID, emote, reaction_type)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
    requestSettings = (server_ID, channel_ID, message_ID, role_ID, emote, reactionType)
    try:
        if debug == True:
            Logger.debug("[HANDLER][REACTIONROLE] Reaction role create " + str(server_ID) + " " + str(message_ID) + " " + str(role_ID) + " " + str(emote) + " " + str(reactionType))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error createReactionRole -> " + error)
            

#Permet de supprimer un rôle de réaction dans la base de données
def deleteReactionRole(server_ID, ID):
    requestFormat = """
                    DELETE 
                    FROM onRawReactionAdd
                    WHERE server_ID = %s AND ID = %s
                    """
    requestSettings = (server_ID, ID)
    try:
        if debug == True:
            Logger.debug("[HANDLER][REACTIONROLE] Deleting reaction role from the DB " + str(ID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error deleteRole -> " + error)
            

#Permet de récupérer la liste des rôles de réaction dans la base de données
def getReactionRole(server_ID):
    requestFormat = """
                    SELECT ID, channel_ID, message_ID, role_ID, emote, reaction_type
                    FROM onRawReactionAdd
                    WHERE server_ID = %s;
                    """
    requestSettings = (server_ID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        if debug == True:
            Logger.debug("[HANDLER][REACTIONROLE] Retrieving the list of reaction roles -> " + str(server_ID))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error getReactionRole -> " + error)