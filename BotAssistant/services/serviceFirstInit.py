# IMPORT LIBRARIES
import os
import sys

# IMPORT SERVICES
from services.serviceLogger import consoleLogger as Logger

# Contenu du fichier settingsDatabase.py
databaseFileContent = """# Veuillez remplir les champs ci-dessous pour configurer la base de donnees
connection = {
    "host": "",
    "database": "",
    "user": "",
    "password": ""
}
"""

# Contenu du fichier settingsToken.py
tokenFileContent = """# Veuillez remplir le champ ci-dessous pour configurer le token du bot
token = ""
"""

# CREATION DES FICHIERS DE CONFIGURATION
# Fonction d'initialisation du fichier settingDatabase.py
def databaseFileInit():    
    file = open("settings/settingDatabase.py","w")
    file.write(databaseFileContent)
    file.close()
    Logger.system("[CONFIG]Database config file created")
    Logger.install("[CONFIG]Please fill the database config file")
    sys.exit(0)

# Fonction d'initialisation du fichier settingsToken.py
def tokenFileInit():    
    file = open("settings/settingToken.py","w")
    file.write(tokenFileContent)
    file.close()
    Logger.system("[CONFIG]Token config file created")
    Logger.install("[CONFIG]Please fill the token config file")
    sys.exit(0)
    

# VERIFICATION DES FICHIERS DE CONFIGURATION
# Fonction de vérification des fichiers de configuration
def firstStartCheck():
    
    # Vérification de l'existence des fichiers de configuration settingsToken.py
    if os.path.exists("settings/settingDatabase.py"): 
        Logger.info("[CONFIG]Database config file found")
    else:
        Logger.warning("[CONFIG]Database config file not found")
        databaseFileInit()
        
    # Vérification de l'existence des fichiers de configuration settingDatabase.py
    if os.path.exists("settings/settingToken.py"): 
        Logger.info("[CONFIG]Token config file found")
    else:
        Logger.warning("[CONFIG]Token config file not found")
        tokenFileInit()