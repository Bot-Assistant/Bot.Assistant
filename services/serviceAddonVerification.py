import importlib
import os
import importlib_metadata
import time

from services.serviceLogger import Logger
import settings.settingBot as settingBot

def packageVerification():

    if settingBot.addonVerification == False:
        Logger.system("Addon verification is disabled")
        return

    Logger.system("Verifying packages...")
    
    if settingBot.debug:
        print("")

    time.sleep(3)

    packageMissing = []
    addonMissing = []

    addonsList = os.listdir("addons")


    for root, dirs, files in os.walk("addons"):
        for file in files:
            if file == "init.py":
                
                if os.name == 'nt':
                    initFile = os.path.join(root, file).replace("\\", ".")[:-3]
                elif os.name == 'posix':
                    initFile = os.path.join(root, file).replace("/", ".")[:-3]
                else:
                    Logger.system("OS: Unknown")

                importedFile = importlib.import_module(initFile)

                if importedFile.cogEnabled == False:
                    continue

                packageList = []

                dists = importlib_metadata.distributions()
                for dist in dists:
                    packageList.append(dist.metadata["Name"])

                addonName = root.replace("addons\\", "")
                
                if settingBot.debug:
                    Logger.install(f"Addon verification: {addonName}")

                for packageDependency in importedFile.packageDependencies:
                    # Verify if the dependency is installed on python
                    if packageDependency in packageList:
                        if settingBot.debug:
                            Logger.debug(f"Package dependency: {packageDependency} is installed")

                    else:
                        if settingBot.debug:
                            Logger.critical(f"Package dependency: {packageDependency} is not installed")
                        packageMissing.append(packageDependency)

                for addonDependency in importedFile.addonDependencies:

                    # Verify if the addon dependency is installed
                    if addonDependency in addonsList:

                        requiredAddon = f"addons\\{addonDependency}\\init.py"
                        requiredAddon = importlib.import_module(requiredAddon.replace("\\", ".")[:-3])

                        if requiredAddon.cogEnabled == False:
                            if settingBot.debug:
                                Logger.critical(f"Addon dependency: {addonDependency} is not enabled")
                            addonMissing.append(addonDependency)

                        else:
                            if settingBot.debug:
                                Logger.debug(f"Addon dependency: {addonDependency} is installed")

                    else:
                        if settingBot.debug:
                            Logger.critical(f"Addon dependency: {addonDependency} is not installed")
                        addonMissing.append(addonDependency)

                if settingBot.debug:
                    time.sleep(1)
                    print("ㅤ")
    


    if len(addonMissing) > 0 and len(packageMissing) > 0:
        Logger.critical("🛑 Some Addons and Packages are not installed/activated")

        for addon in addonMissing:
            Logger.warning(f"Addon missing: {addon}")
        
        
        command = "pip install"
        for dependency in packageMissing:
            command += f" {dependency}"

        Logger.warning(f"Command to install the dependencies: {command}")
        
        os._exit(0)

    if len(addonMissing) > 0:
        Logger.critical("🛑 Some addons are not installed/activated")

        for addon in addonMissing:
            Logger.warning(f"Addon missing: {addon}")
        
        os._exit(0)

    elif len(packageMissing) > 0:
        Logger.critical("🛑 Some dependencies are not installed/activated")
        
        command = "pip install"
        for dependency in packageMissing:
            command += f" {dependency}"

        Logger.warning(f"Command to install the dependencies: {command}")
        
        os._exit(0)

    else:
        Logger.install("All dependencies are installed")
        Logger.system("The bot will start in 3 seconds")
        time.sleep(3)
        print("")