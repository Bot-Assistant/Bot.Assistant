import services.serviceTime as serviceTime

purpleColor = "\033[95m"
blueColor = '\033[94m'

cyanColor = "\033[96m"
greenColor = "\033[92m"
yellowColor = "\033[93m"
redColor = "\033[91m"

endColor = "\033[0m"
boldType = "\033[1m"


class consoleLogger:

    def install(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + cyanColor + "[INSTALL]" + endColor

        #Set message
        logContent = cyanColor + boldType + str(message) + endColor
        
        #Print to console
        print(time, prefix + logContent)
    
        
    def system(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + purpleColor + "[SYSTEM]" + endColor

        #Set message
        logContent = purpleColor + str(message) + endColor

        #Print to console
        print(time, prefix + logContent)
        
        
    def database(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + blueColor + "[DATABASE]" + endColor

        #Set message
        logContent = blueColor + str(message) + endColor

        #Print to console
        print(time, prefix + logContent)
        

    def debug(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + cyanColor + "[DEBUG]" + endColor

        #Set message
        logContent = cyanColor + str(message) + endColor

        #Print to console
        print(time, prefix + logContent)


    def info(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + greenColor + "[INFO]" + endColor

        #Set message
        logContent = greenColor + str(message) + endColor

        #Print to console
        print(time, prefix + logContent)


    def warning(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + yellowColor + "[WARNING]" + endColor

        #Set message
        logContent = yellowColor + str(message) + endColor

        #Print to console
        print(time, prefix + logContent)


    def error(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + redColor + "[ERROR]" + endColor

        #Set message
        logContent = redColor + str(message) + endColor
        
        #Print to console
        print(time, prefix + logContent)


    def critical(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + redColor + "[CRITICAL]" + endColor

        #Set message
        logContent = redColor + boldType + str(message) + endColor

        #Print to console
        print(time, prefix + logContent)


    def update(message):
        #Get time
        time = serviceTime.classTime.getHMS()

        #Set prefix
        prefix = boldType + yellowColor + "[UPDATE]" + endColor

        #Set message
        logContent = yellowColor + str(message) + endColor

        #Print to console
        print(time, prefix + logContent)