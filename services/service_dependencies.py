import os
import sys

from settings import setting_dependencies

from settings.setting_colors import *


def install_dependency(dependency_pip_name, dependency_module_name):
    # Send installation message
    print(f"Installing/upgrading {dependency_pip_name}...", end="", flush=True)

    # Install or upgrade the dependency in silent mode
    os.system(f"{sys.executable} -m pip install {dependency_pip_name} --upgrade --quiet")

    # Check if the dependency has been installed
    try:
        __import__(dependency_module_name)
        print(txt_light_green + "[OK]" + color_reset)
    except ImportError:
        print(txt_light_red + "[ERROR]" + color_reset + sys.exc_info()[1])
        sys.exit(0)
