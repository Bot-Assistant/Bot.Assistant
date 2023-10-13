import services.serviceTime as serviceTime
import settings.settingBot as settingBot

class Logger:

    # TEXT COLORS
    # -- Dark --
    # Dark Red: \033[31m HEX: #800000
    # Dark Green: \033[32m HEX: #008000
    # Dark Yellow: \033[33m HEX: #808000
    # Dark Blue: \033[34m HEX: #000080
    # Dark Magenta: \033[35m HEX: #800080
    # Dark Cyan: \033[36m HEX: #008080
    
    
    # -- Light --
    # Light Red: \033[91m HEX: #FF0000
    # Light Green: \033[92m HEX: #00FF00
    # Light Yellow: \033[93m HEX: #FFFF00
    # Light Blue: \033[94m HEX: #0000FF
    # Light Magenta: \033[95m HEX: #FF00FF
    # Light Cyan: \033[96m HEX: #00FFFF
    

    # BACKGROUND COLORS
    # -- Dark --
    # Dark Red Background: \033[41m HEX: #800000
    # Dark Green Background: \033[42m HEX: #008000
    # Dark Yellow Background: \033[43m HEX: #808000
    # Dark Blue Background: \033[44m HEX: #000080
    # Dark Magenta Background: \033[45m HEX: #800080
    # Dark Cyan Background: \033[46m HEX: #008080
    

    # -- Light --
    # Light Red Background: \033[101m HEX: #FF0000
    # Light Green Background: \033[102m HEX: #00FF00
    # Light Yellow Background: \033[103m HEX: #FFFF00
    # Light Blue Background: \033[104m HEX: #0000FF
    # Light Magenta Background: \033[105m HEX: #FF00FF
    # Light Cyan Background: \033[106m HEX: #00FFFF
    

    # -- Black --
    # Black: \033[30m HEX: #000000
    # Dark Gray: \033[90m HEX: #808080
    # Light Gray: \033[37m HEX: #C0C0C0
    # White: \033[97m HEX: #FFFFFF

    # Black Background: \033[40m HEX: #000000
    # Dark Gray Background: \033[100m HEX: #808080
    # Light Gray Background: \033[47m HEX: #C0C0C0
    # White Background: \033[107m HEX: #FFFFFF


    # -- Other --
    # Reset: \033[0m
    # Bold: \033[1m
    # Underline: \033[4m
    # Reversed: \033[7m




    colorDict = {
        # Initialization logs
        "system": "\033[45m\033[97m", # Background #800080 Text #FFFFFF
        "install": "\033[46m\033[97m", # Background #008080 Text #FFFFFF
        "update": "\033[42m\033[97m", # Background #008000 Text #FFFFFF

        # Database logs
        "table": "\033[33m", # Background - Text #808000
        "colomn": "\033[34m", # Background - Text #000080

        # Information logs
        "debug": "\033[96m", # Background - Text #00FFFF
        "info": "\033[92m", # Background - Text #00FF00
        "warning": "\033[93m", # Background - Text #FFFF00
        "error": "\033[91m", # Background - Text #FF0000
        "critical": "\033[41m\033[97m" # Background #800000 Text #FFFFFF
    }


    prefixDict = {
        "system": "[SYSTEM]",
        "install": "[INSTALL]",
        "update": "[UPDATE]",

        "table": "[TABLE]",
        "colomn": "[COLOMN]",

        "debug": "[DEBUG]",
        "info": "[INFO]",
        "warning": "[WARNING]",
        "error": "[ERROR]",
        "critical": "[CRITICAL]"
    }

    
    def write(type, message):

        if settingBot.consoleColor == True:
            consoleColor = Logger.colorDict[type]
            prefix = Logger.prefixDict[type]

            endColor = "\033[0m"
            
        else:
            consoleColor = ""
            prefix = Logger.prefixDict[type]

            endColor = ""

        if settingBot.debug == False and type == "debug":
            return

        # Get time
        logYMD = serviceTime.getYMD()
        logHMS = serviceTime.getHMS()

        # Set message
        logPrefix = consoleColor + prefix + endColor
        logMessage = consoleColor + message + endColor

        # Print message with Prefix in color and bold
        print(logHMS, logPrefix, logMessage)

        # Write message in a file
        file = open("logs/" + logYMD + ".log", "a", encoding="utf-8")
        file.write("\n" + logHMS + " " + prefix + " " + message)
        file.close()

    # Initialization logs
    def system(message):
        Logger.write("system", message)

    def install(message):
        Logger.write("install", message)

    def update(message):
        Logger.write("update", message)


    # Database logs
    def table(message):
        Logger.write("table", message)

    def colomn(message):
        Logger.write("colomn", message)


    # Information logs
    def debug(message):
        Logger.write("debug", message)

    def info(message):
        Logger.write("info", message)

    def warning(message):
        Logger.write("warning", message)

    def error(message):
        Logger.write("error", message)

    def critical(message):
        Logger.write("critical", message)