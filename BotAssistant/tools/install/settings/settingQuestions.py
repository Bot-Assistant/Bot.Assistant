import tools.install.messages.messageLogo as messageLogo

def colorSetting():
    messageLogo.send()
    print("Do you see the color of the text below?")
    print(" ")
    print("  \033[91m" + "RED" + "\033[0m  ")
    print("  \033[92m" + "GREEN" + "\033[0m")
    print("  \033[94m" + "BLUE" + "\033[0m ")
    print("  \033[101m" + "RED" + "\033[0m  ")
    print("  \033[102m" + "GREEN" + "\033[0m")
    print("  \033[104m" + "BLUE" + "\033[0m ")

    print(" ")
    print("Do you see the color of the text below? (y/n)")
    answer = input("Answer: ")

    return answer

def debugSetting():
    messageLogo.send()
    print("Do you want to enable debug mode? (y/n)")
    answer = input("Answer: ")

    return answer

def addonsSetting():
    messageLogo.send()
    print("Do you want to verify the addons? (y/n)")
    answer = input("Answer: ")

    return answer

def dependenciesSetting():
    messageLogo.send()
    print("Do you want to verify the dependencies? (y/n)")
    answer = input("Answer: ")

    return answer

def databaseTypeSetting():
    messageLogo.send()
    print("Choose the database type:")
    print(" ")
    print("1. MariaDB")
    print("2. SQLite")
    print(" ")
    print("Choose the database type:")
    answer = input("Answer: ")

    return answer