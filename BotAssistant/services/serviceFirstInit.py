# IMPORT LIBRARIES
import os
from sys import exit

# IMPORT SERVICES
from services.serviceLogger import consoleLogger as Logger

# Content of the settingDatabase.py file
databaseFileContent = """# Please fill in the fields below to configure the database
connection = {
    "host": "",
    "database": "",
    "user": "",
    "password": ""
}

# Only for sqlite
# ⚠️ Do not let this field empty if you use sqlite
sqliteFile = "defaultFile"
"""

# Content of the settingToken.py file
tokenFileContent = """# Please fill in the field below to configure the bot token
token = ""
"""

# CREATION OF CONFIGURATION FILES
# Initialization function of the settingDatabase.py file
def databaseFileInit():    
    file = open("settings/settingDatabase.py","w")
    file.write(databaseFileContent)
    file.close()
    Logger.system("[CONFIG]Database config file created")
    Logger.install("[CONFIG]Please fill the database config file")
    exit(0)

# Function to initialize the settingToken.py file
def tokenFileInit():    
    file = open("settings/settingToken.py","w")
    file.write(tokenFileContent)
    file.close()
    Logger.system("[CONFIG]Token config file created")
    Logger.install("[CONFIG]Please fill the token config file")
    exit(0)
    

# CHECK CONFIGURATION FILES
# Configuration file verification function
def firstStartCheck():
    
    # Checking the existence of the settingToken.py configuration files
    if os.path.exists("settings/settingDatabase.py"): 
        Logger.info("[CONFIG]Database config file found")
    else:
        Logger.warning("[CONFIG]Database config file not found")
        databaseFileInit()
        
    # Checking the existence of the settingDatabase.py configuration files
    if os.path.exists("settings/settingToken.py"): 
        Logger.info("[CONFIG]Token config file found")
    else:
        Logger.warning("[CONFIG]Token config file not found")
        tokenFileInit()