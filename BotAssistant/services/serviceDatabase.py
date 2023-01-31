from sys import exit

import mysql.connector
import settings.settingDatabase as settingDatabase
from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug


# Create the database if it does not exist
def bddInit():
    try:
        Logger.database("[CONNECTION]Database connection success")
        
        with mysql.connector.connect(**settingDatabase.connection) as database :
            with database.cursor() as cursor:
                try:
                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS `servers` (\
                        `ID` int(11) NOT NULL AUTO_INCREMENT,\
                        `server_ID` bigint(20) NOT NULL,\
                        `logs_ID` bigint(20) DEFAULT NULL,\
                        `logs_level` int(11) DEFAULT 1,\
                        PRIMARY KEY (`ID`)\
                        ) ENGINE=InnoDB CHARSET=utf8mb4;"
                    )
                    Logger.database("[HANDLER][INIT]Server table init")
                except Exception as error:
                    Logger.error("[TABLE]Table error servers -> " + str(error))
                    
                database.commit()
            
                   
    except Exception as error:
        Logger.critical("[HANDLER][INIT]Database connection error -> " + str(error))
        exit(0)

# Make a request to the database without returning a result
def makeRequest(requestFormat, requestSettings):
        with mysql.connector.connect(**settingDatabase.connection) as database :
            with database.cursor() as cursor:
                cursor.execute(requestFormat, requestSettings)
                database.commit()

# Find a result in the database and return it
def getInfoRequest(requestFormat, requestSettings):
        with mysql.connector.connect(**settingDatabase.connection) as database :
            with database.cursor(buffered=True) as cursor:
                cursor.execute(requestFormat, requestSettings)
                result = cursor.fetchall()
                database.commit()
                return result