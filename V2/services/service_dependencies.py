import os
import sys

from V2.settings import setting_dependencies


def install_bot_dependencies():

    # PIP
    print("Upgrading pip...", end="", flush=True)
    os.system(f"{sys.executable} -m pip install pip --upgrade --quiet")
    print("[OK]\n")

    # DEPENDENCIES
    for dependency in setting_dependencies.dependencies:

        # Get the dependency name
        dependency_pip_name = dependency[0]

        # If the dependency_module_name is empty, the dependency_pip_name will be used
        dependency_module_name = dependency[1]
        if dependency_module_name == "":
            dependency_module_name = dependency_pip_name

        # Install the dependency
        install_dependency(dependency_pip_name, dependency_module_name)


def install_dependency(dependency_pip_name, dependency_module_name):

    # Send installation message
    print(f"Installing/upgrading {dependency_pip_name}...", end="", flush=True)

    # Install or upgrade the dependency in silent mode
    os.system(f"{sys.executable} -m pip install {dependency_pip_name} --upgrade --quiet")

    # Check if the dependency has been installed
    try:
        __import__(dependency_module_name)
        print("[OK]")
    except ImportError:
        print(f"Error details: {sys.exc_info()[1]}")
        print(f"Error: {dependency_pip_name} has not been installed")
        sys.exit(0)

