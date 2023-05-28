import os

import settings.settingBot as settingBot

def logo():

    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

    #Print logo
    print(f"========================================================")
    print(f"      █▄▄ █▀█ ▀█▀ ░ ▄▀█ █▀ █▀ █ █▀ ▀█▀ ▄▀█ █▄░█ ▀█▀     ")
    print(f"      █▄█ █▄█ ░█░ ▄ █▀█ ▄█ ▄█ █ ▄█ ░█░ █▀█ █░▀█ ░█░     ")
    print(f"========================================================")
    print(f"                   Bot Assistant Version                ")
    print(f"                   {settingBot.botVersion}              ")
    print(f"========================================================")
    print(f"                                                        ")
