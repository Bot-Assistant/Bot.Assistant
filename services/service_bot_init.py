# IMPORT LIBRARIES
import os
from sys import exit

# IMPORT SERVICES
from services.service_logger import Logger
#
# import tools.toolConfigurator.installSettings as installSettings
# import tools.toolConfigurator.installDatabase as installDatabase
# import tools.toolConfigurator.installToken as installToken

# Content of the setting_database.py file
databaseFileContent = """# Please fill in the fields below to configure the database
connection = {
    "host": "defaultHostName",
    "database": "defaultDatabaseName",
    "user": "defaultUserName",
    "password": "defaultPassword"
}

# Only for sqlite
# Do not let this field empty if you use sqlite
sqliteFile = "defaultFile"
"""

# Content of the settingToken.py file
tokenFileContent = """# Please fill in the field below to configure the bot token
token = ""
"""


# CREATION OF CONFIGURATION FILES
# Initialization function of the setting_token.py file
def database_file_init():
    file = open("settings/setting_database.py", "w")
    file.write(databaseFileContent)
    file.close()
    Logger.system("[CONFIG]Database config file created", False)
    Logger.install("[CONFIG]Please fill the database config file", False)
    exit(0)


# Function to initialize the setting_token.py file
def token_file_init():
    file = open("settings/setting_token.py", "w")
    file.write(tokenFileContent)
    file.close()
    Logger.system("[CONFIG]Token config file created", False)
    Logger.install("[CONFIG]Please fill the token config file", False)
    exit(0)


# CHECK CONFIGURATION FILES
# Configuration file verification function
def first_start_check():
    # installSettings.install()
    # installDatabase.install(databaseFileContent)
    # installToken.install(tokenFileContent)

    if os.path.exists("settings/setting_database.py"):
        Logger.info("[CONFIG]Database config file found", False)
    else:
        Logger.warning("[CONFIG]Database config file not found", False)
        database_file_init()

    # Checking the existence of the settingDatabase.py configuration files
    if os.path.exists("settings/setting_token.py"):
        Logger.info("[CONFIG]Token config file found", False)
    else:
        Logger.warning("[CONFIG]Token config file not found", False)
        token_file_init()
