import sys
import threading
import os

from services import serviceCleaner as cleaner
from services.serviceLogger import consoleLogger as Logger


def stopCommand():
    def stop():
        
        print("Type 'stop' to stop the bot and clean the files")

        while True:

            input = sys.stdin.readline()

            if "stop" in input:
                Logger.system("The bot is now offline")
                cleaner.clean(".")
                os._exit(0)
            
            elif "exit" in input:
                Logger.system("The bot is now offline")
                os._exit(0)
                
        
    threadStop = threading.Thread(target=stop)
    threadStop.start()