import services.serviceTime as serviceTime
import settings.settingBot as settingBot

if settingBot.consoleColor == True:
    purpleColor = "\033[95m"
    blueColor = '\033[94m'

    cyanColor = "\033[96m"
    greenColor = "\033[92m"
    yellowColor = "\033[93m"
    redColor = "\033[91m"

    endColor = "\033[0m"
    boldType = "\033[1m"

else:
    purpleColor = ""
    blueColor = ""

    cyanColor = ""
    greenColor = ""
    yellowColor = ""
    redColor = ""

    endColor = ""
    boldType = ""



class consoleLogger:

    def system(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + purpleColor + "[SYSTEM]" + endColor

        #Set message
        logContent = purpleColor + str(message) + endColor

        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 💜 [System]" + message)
        fileWrited.close()


    def install(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + cyanColor + "[INSTALL]" + endColor

        #Set message
        logContent = cyanColor + boldType + str(message) + endColor
        
        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🟦 [Install]" + message)
        fileWrited.close()
            
        
    def database(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + blueColor + "[DATABASE]" + endColor

        #Set message
        logContent = blueColor + str(message) + endColor

        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🟦 [Database]" + message)
        fileWrited.close()

    
    def update(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + yellowColor + "[UPDATE]" + endColor

        #Set message
        logContent = yellowColor + str(message) + endColor

        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🟨 [Update]" + message)
        fileWrited.close()
        



    def debug(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + cyanColor + "[DEBUG]" + endColor

        #Set message
        logContent = cyanColor + str(message) + endColor

        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🔘 [Debug] " + message)
        fileWrited.close()


    def info(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + greenColor + "[INFO]" + endColor

        #Set message
        logContent = greenColor + str(message) + endColor

        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🟢 [Info] " + message)
        fileWrited.close()


    def warning(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + yellowColor + "[WARNING]" + endColor

        #Set message
        logContent = yellowColor + str(message) + endColor

        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🟡 [Warning] " + message)
        fileWrited.close()


    def error(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + redColor + "[ERROR]" + endColor

        #Set message
        logContent = redColor + str(message) + endColor
        
        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🟠 [Error] " + message)
        fileWrited.close()


    def critical(message):
        #Get time
        timeHMS = serviceTime.classTime.getHMS()
        timeDMY = serviceTime.classTime.getDMY()

        #Set prefix
        prefix = boldType + redColor + "[CRITICAL]" + endColor

        #Set message
        logContent = redColor + boldType + str(message) + endColor

        #Print to console
        print(timeHMS, prefix + logContent)

        #Write to log file
        fileWrited = open(f"logs/{timeDMY}.log", "a", encoding="utf-8")
        fileWrited.write("\n" + timeHMS + " 🔴 [Critical] " + message)
        fileWrited.close()