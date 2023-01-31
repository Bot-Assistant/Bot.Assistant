serviceBot:
    /!\ This file is very important. The defaults functions of the use this file. /!\
    This file allows you to recover and replace an "import discord".
    If your bot becomes very big an optimization is required.

    Functions in this file:
    getBot()
    getDiscord()
    getClient()
    getCommands()


serviceDatabase:
    /!\ This file is very important. The defaults functions of the use this file. /!\
    This file contain all the functions to interact with the database.

    Functions in this file:
    makeRequest() - Make a request to the database but don't return anything. We use this function to insert, remove or update something in the database.
    getInfoRequest() - Make a request to the database and return the result. We use this function to get the information in the database.


serviceDiscordLogger:
    /!\ This file is very important. The defaults functions of the use this file. /!\
    This file contain all the functions to send logs to Discord.

    Functions in this file:
    discordLogger.debug() - Send a message with "debug" level. (Level 1 in the database)
    discordLogger.info() - Send a message with "info" level. (Level 2 in the database)
    discordLogger.warning() - Send a message with "warning" level. (Level 3 in the database)
    discordLogger.error() - Send a message with "error" level. (Level 4 in the database)
    discordLogger.critical() - Send a message with "critical" level. (Level 5 in the database)

serviceFileManager:
    /!\ This file is very important. The defaults functions of the use this file. /!\
    This file contain all the functions to interact with the file system.
    You can create folder and write files.

    Functions in this file:
    createFolder() - Create a folder.
    writeFile() - Write a file.

serviceFirstInit:
    /!\ This file is very important. The defaults functions of the use this file. /!\
    This file contain all the functions to initialize the bot for the first time.
    This file is only used when the bot is launched.

    If you edit this file, be careful because you can break the bot.
    This file is used to create settingToken ans settingDatabase.

serviceLogger:
    /!\ This file is very important. The defaults functions of the use this file. /!\
    This file contain all the functions to send logs to the console.
    This logger is more complete than the Discord logger.

    Functions in this file:
    consoleLogger.install() - Send a log with "install" tag and color.
    consoleLogger.system() - Send a log with "system" tag and color.
    consoleLogger.database() - Send a log with "database" tag and color.
    consoleLogger.debug() - Send a log with "debug" tag and color.
    consoleLogger.info() - Send a log with "info" tag and color.
    consoleLogger.warning() - Send a log with "warning" tag and color.
    consoleLogger.error() - Send a log with "error" tag and color.
    consoleLogger.critical() - Send a log with "critical" tag and color.

serviceTime:
    /!\ This file is very important. The defaults functions of the use this file. /!\
    This file contain all the functions to get the time.

    Functions in this file:
    getHMS() - Get the time in hours, minutes and seconds.
    getDMY() - Get the date in day, month and year.