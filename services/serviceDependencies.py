import importlib
import os
import sys
from services.serviceLogger import Logger
import settings.settingBot as settingBot


def installAddonsDependencies():
    """Install or upgrade all dependencies from addons."""

    if not settingBot.dependenciesVerification:
        Logger.system("Dependencies verification is disabled")
        return

    allPackageDependencies = []

    # Get "packageDependencies" from all addons
    for root, dirs, files in os.walk("addons"):
        for file in files:
            # Get only init.py files
            if file == "init.py":
                # Convert the file path to a module name
                initFile = os.path.join(root, file).replace(os.sep, ".")[:-3]
                # Import init.py files
                importedFile = importlib.import_module(initFile)
                # Add dependencies from init.py to allPackageDependencies
                allPackageDependencies.extend(importedFile.packageDependencies)

    # Remove duplicates
    allPackageDependencies = list(set(allPackageDependencies))

    # Install dependencies
    for package in allPackageDependencies:
        installDependency(package)


def installDependency(dependencyName: str):
    """Install or upgrade a dependency."""
    Logger.system(f"Installing {dependencyName}")
    os.system(f"{sys.executable} -m pip install {dependencyName} --upgrade")


def installDependenciesFromList(dependencyList: list):
    """Install or upgrade a list of dependencies."""
    for dependencyName in dependencyList:
        installDependency(dependencyName)


def uninstallDependency(dependencyName: str):
    """Uninstall a dependency."""
    Logger.system(f"Uninstalling {dependencyName}")
    os.system(f"{sys.executable} -m pip uninstall {dependencyName} --yes")


def uninstallDependenciesFromList(dependencyList: list):
    """Uninstall a list of dependencies."""
    for dependencyName in dependencyList:
        uninstallDependency(dependencyName)
