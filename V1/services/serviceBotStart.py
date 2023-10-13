def start():

    # INIT FILE SYSTEM
    import services.serviceFileManager as serviceFileManager
    serviceFileManager.createFolder("logs")

    # INIT CONFIG FILE SYSTEM
    import services.serviceFirstInit as serviceFirstInit
    serviceFirstInit.firstStartCheck()

    # ADDON UPDATER
    import services.serviceAddonUpdater as serviceAddonUpdater
    serviceAddonUpdater.updateAddon()

    # Install dependencies from addons
    import services.serviceDependencies as serviceDependencies
    serviceDependencies.installAddonsDependencies()

    import services.serviceAddonVerification as serviceAddonVerification
    serviceAddonVerification.packageVerification()

    import services.serviceConsoleMessages as serviceConsoleMessages
    serviceConsoleMessages.logo()

    # INIT LOG SYSTEM
    from services.serviceLogger import Logger
    Logger.system("[BOT]The bot is loading")

    # INIT DATABASE
    import handlers.handlerDatabaseInit as handlerDatabaseInit
    handlerDatabaseInit.databaseInit()

    # INIT BOT 
    import services.serviceBot as serviceBot
    serviceBot.classBot.initialize()
    bot = serviceBot.classBot.getBot()


    # █▀█ █▄░█   █▀█ █▀▀ ▄▀█ █▀▄ █▄█
    # █▄█ █░▀█   █▀▄ ██▄ █▀█ █▄▀ ░█░
    import services.serviceConsole as serviceConsole
    import functions.events.eventOnReady as eventOnReady
    @bot.event
    async def on_ready():
        Logger.system("The bot is now online")
        eventOnReady.onReady()
        serviceConsole.consoleCommand()



    import handlers.handlersServer as handlersServer
    @bot.event
    async def on_guild_join(guild):
        handlersServer.addServerID(guild.id)

    @bot.event
    async def on_guild_remove(guild):
        handlersServer.delServerID(guild.id)


    # ▄▀█ █▀▄ █▀▄ █▀█ █▄░█ █▀
    # █▀█ █▄▀ █▄▀ █▄█ █░▀█ ▄█
    from services.serviceCogLoad import importCogs
    importCogs()

    # START THE BOT
    import settings.settingToken as settingToken
    bot.run(settingToken.token)