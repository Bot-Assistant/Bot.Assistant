import sys
import threading
import os

import services.serviceCleaner as cleaner
from services.serviceLogger import Logger


def consoleCommand():

    def console():
        
        print("Type 'stop [-c]' to stop the bot and clean the files")

        while True:

            input = sys.stdin.readline()

            if "stop -c" in input:
                Logger.system("The bot is now offline and the files are cleaned")
                cleaner.clean(".")
                os._exit(0)
            
            elif "stop" in input:
                Logger.system("The bot is now offline")
                os._exit(0)

            else:
                Logger.system("The command is not valid")
                
        
    threadStop = threading.Thread(target=console)

    threadStop.start()