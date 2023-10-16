import os
import sys

from services import service_dependencies, service_console_messages, service_bot
from init import init_bot
from settings import setting_dependencies

from settings.setting_colors import *


def initialization():
    service_console_messages.logo()
    install_bot_dependencies()
    service_bot.BotAssistant.initialize()

    service_console_messages.logo()
    init_bot.first_start_check()


def install_bot_dependencies():

    # PIP
    print("Upgrading pip...", end="", flush=True)
    os.system(f"{sys.executable} -m pip install pip --upgrade --quiet")
    print(txt_dark_green + "[OK]" + color_reset + "\n")

    # DEPENDENCIES
    for dependency in setting_dependencies.dependencies:

        # Get the dependency name
        dependency_pip_name = dependency[0]

        # If the dependency_module_name is empty, the dependency_pip_name will be used
        dependency_module_name = dependency[1]
        if dependency_module_name == "":
            dependency_module_name = dependency_pip_name

        # Install the dependency
        service_dependencies.install_dependency(dependency_pip_name, dependency_module_name)


initialization()
