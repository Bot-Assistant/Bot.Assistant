from services import service_time
from settings import setting_bot

from settings.setting_colors import *


class Logger:

    color_dict = {
        # Initialization logs
        "system": bg_dark_magenta + txt_black,
        "installer": bg_light_cyan + txt_black,
        "update": bg_dark_green + txt_black,

        # Database logs
        "table": txt_dark_yellow,
        "column": txt_dark_blue,

        # Information logs
        "debug": txt_light_cyan,
        "info": txt_light_green,
        "warning": txt_light_yellow,
        "error": txt_light_red,
        "critical": bg_dark_red + txt_white
    }

    prefix_dict = {
        "system": "[SYSTEM]",
        "installer": "[INSTALL]",
        "update": "[UPDATE]",

        "table": "[TABLE]",
        "column": "[COLUMN]",

        "debug": "[DEBUG]",
        "info": "[INFO]",
        "warning": "[WARNING]",
        "error": "[ERROR]",
        "critical": "[CRITICAL]"
    }

    @staticmethod
    def write(message_type, message, write_in_file=True):

        if setting_bot.console_color:
            console_color = Logger.color_dict[message_type]
            prefix = Logger.prefix_dict[message_type]

            end_color = "\033[0m"

        else:
            console_color = ""
            prefix = Logger.prefix_dict[message_type]

            end_color = ""

        if not setting_bot.debug and type == "message_type":
            return

        # Get time
        log_dmy = service_time.get_dmy()
        log_hms = service_time.get_hms()

        # Set message
        log_prefix = console_color + prefix + end_color
        log_message = console_color + message + end_color

        # Print message with Prefix in color and bold
        print(log_hms, log_prefix, log_message)

        # Write message in a file
        if write_in_file:
            file = open("logs/" + log_dmy + ".log", "a", encoding="utf-8")
            file.write("\n" + log_hms + " " + prefix + " " + message)
            file.close()

    # Initialization logs
    @staticmethod
    def system(message, write_in_file=True):
        Logger.write("system", message, write_in_file)

    @staticmethod
    def install(message, write_in_file=True):
        Logger.write("installer", message, write_in_file)

    @staticmethod
    def update(message, write_in_file=True):
        Logger.write("update", message, write_in_file)

    # Database logs
    @staticmethod
    def table(message, write_in_file=True):
        Logger.write("table", message, write_in_file)

    @staticmethod
    def column(message, write_in_file=True):
        Logger.write("column", message, write_in_file)

    # Information logs
    @staticmethod
    def debug(message, write_in_file=True):
        Logger.write("debug", message, write_in_file)

    @staticmethod
    def info(message, write_in_file=True):
        Logger.write("info", message, write_in_file)

    @staticmethod
    def warning(message, write_in_file=True):
        Logger.write("warning", message, write_in_file)

    @staticmethod
    def error(message, write_in_file=True):
        Logger.write("error", message, write_in_file)

    @staticmethod
    def critical(message, write_in_file=True):
        Logger.write("critical", message, write_in_file)
