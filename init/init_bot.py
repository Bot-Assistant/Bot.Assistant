# IMPORT LIBRARIES
import os
import sys

# IMPORT SERVICES
from services.service_logger import Logger
from services import service_json, service_file_manager

# import tools.toolConfigurator.installSettings as installSettings
# import tools.toolConfigurator.installDatabase as installDatabase
# import tools.toolConfigurator.installToken as installToken

# Content of the setting_database.py file
database_file_content = {
    "connection": {
        "host": "defaultHostName",
        "database": "defaultDatabaseName",
        "user": "defaultUserName",
        "password": "defaultPassword"
    },
    "sqliteFile": "defaultFile"
}

# Content of the settingToken.py file
token_file_content = {
    "token": ""
}


# CHECK CONFIGURATION FILES
# Configuration file verification function
def first_start_check():
    # installSettings.install()
    # installDatabase.install(databaseFileContent)
    # installToken.install(tokenFileContent)

    if os.path.exists("settings/setting_database.json"):
        Logger.info("[CONFIG]Database config file found", False)
    else:
        Logger.system("[CONFIG]Database config file created", False)
        Logger.install("[CONFIG]Please fill the database config file", False)
        service_json.create_json("settings/setting_database.json", database_file_content)
        sys.exit(0)

    # Checking the existence of the settingDatabase.py configuration files
    if os.path.exists("settings/setting_token.json"):
        Logger.info("[CONFIG]Token config file found", False)
    else:
        Logger.system("[CONFIG]Token config file created", False)
        Logger.install("[CONFIG]Please fill the token config file", False)
        service_json.create_json("settings/setting_token.json", token_file_content)
        sys.exit(0)
