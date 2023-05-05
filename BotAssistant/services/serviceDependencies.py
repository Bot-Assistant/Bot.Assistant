import importlib
import os

from services.serviceLogger import Logger

import settings.settingBot as settingBot

def installDependencies():

    if settingBot.dependenciesVerification == False:
        Logger.system("Dependencies verification is disabled")
        return

    # Get "packageDependencies" from all addons
    allPackageDependencies = []

    # Get list of dependencies from requirements.txt
    requirementsFile = open("requirements.txt", "r")
    
    # Split the file in lines
    packageList = requirementsFile.read().splitlines()

    # Add dependencies from requirements.txt in allPackageDependencies
    for package in packageList:
        allPackageDependencies.append(package)

    # Get "packageDependencies" from all addons
    for root, dirs, files in os.walk("addons"):
        for file in files:

            # Get only init.py files
            if file == "init.py":
                
                # If the OS is Windows
                if os.name == 'nt':
                    initFile = os.path.join(root, file).replace("\\", ".")[:-3]
                # If the OS is Linux
                elif os.name == 'posix':
                    initFile = os.path.join(root, file).replace("/", ".")[:-3]
                # If the OS is unknown
                else:
                    Logger.system("OS: Unknown")
                    exit(1)

                # Import init.py files
                importedFile = importlib.import_module(initFile)

                # Add dependencies from init.py in allPackageDependencies
                for package in importedFile.packageDependencies:
                    allPackageDependencies.append(package)

    # Remove duplicates 
    allPackageDependencies = list(dict.fromkeys(allPackageDependencies))

    # Open requirements.txt in write mode
    requirementsFile = open("requirements.txt", "w")

    # Clear requirements.txt
    requirementsFile.write("")

    # Log all dependencies
    print("ㅤ")
    Logger.install("Dependencies: " + package)

    # Write dependencies in requirements.txt
    for package in allPackageDependencies:

        Logger.install(package)

        requirementsFile.write(package + "\n")

        try:    
            os.system(f"pip install {package} --upgrade")
        except:
            Logger.warning(f"Failed to install {package}")

    print("ㅤ")