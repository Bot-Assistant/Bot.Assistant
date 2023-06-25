import handlers.handlersServer as handlersServer

# Init BotAssistant
import services.serviceBot as serviceBot
bot = serviceBot.classBot.getBot()

def onReady():
    # Verify bot - database server list
    serversList = handlersServer.getServers()

    # Verify if a server is not in the database
    for server in bot.guilds:
        if server.id not in [server[0] for server in serversList]:
            handlersServer.addServerID(server.id)
    
    # Verify if a server is not in the bot server list
    for server in serversList:
        if bot.get_guild(server[0]) is None:
            handlersServer.delServerID(server[0])