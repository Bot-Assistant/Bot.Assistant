import os

from V2.settings import setting_bot


def logo():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

    # Print logo
    print(f"========================================================")
    print(f"      █▄▄ █▀█ ▀█▀ ░ ▄▀█ █▀ █▀ █ █▀ ▀█▀ ▄▀█ █▄░█ ▀█▀     ")
    print(f"      █▄█ █▄█ ░█░ ▄ █▀█ ▄█ ▄█ █ ▄█ ░█░ █▀█ █░▀█ ░█░     ")
    print(f"========================================================")
    print(f"                   Bot Assistant Version                ")
    print(f"                   {setting_bot.bot_version}              ")
    print(f"========================================================")
    print(f"                                                        ")
