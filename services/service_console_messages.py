import os

from settings import setting_bot


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
    print(f"                      Bot Assistant                     ")
    print(f"                      {setting_bot.bot_version}         ")
    print(f"========================================================")
    print(f"                                                        ")
