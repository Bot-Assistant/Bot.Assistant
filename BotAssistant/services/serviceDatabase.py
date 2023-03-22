import mysql.connector
import settings.settingDatabase as settingDatabase
from services.serviceLogger import consoleLogger as Logger
import sys
import settings.settingBot as settingBot


# Create the database if it does not exist
def databaseCreation(tableName: str, columns: list):
    # Create database
    try:
        Logger.database(f"[CONNECTION][{tableName}][INIT]Table {tableName} initialization...")

        # Create Table
        requestFormat = f"""
                CREATE TABLE IF NOT EXISTS {tableName} (
                    ID INT NOT NULL AUTO_INCREMENT,
                    PRIMARY KEY (ID)
                    );
                """
        requestSettings = ()

        makeRequest(requestFormat, requestSettings)

        # Add columns
        for column in columns:
            requestFormat = f"""
                    ALTER TABLE {tableName}
                    ADD COLUMN IF NOT EXISTS """ + column[0] + """ """ + column[1] + """;
                    """
            requestSettings = ()

            makeRequest(requestFormat, requestSettings)

            if settingBot.debug:
                Logger.debug(f"[HANDLER][{tableName}][INIT]Column {column[0]} initialization success")

        Logger.database(f"[HANDLER][{tableName}][INIT]Table {tableName} initialization success")
           
    except Exception as error:
        Logger.critical(f"[HANDLER][{tableName}][INIT]Table {tableName} initialization error -> " + str(error))
        sys.exit(0)


# Make a request to the database without returning a result
def makeRequest(requestFormat, requestSettings):
        
        database = mysql.connector.connect(**settingDatabase.connection)
        cursor = database.cursor()

        cursor.execute(requestFormat, requestSettings)

        database.commit()
        cursor.close()
        database.close()


# Find a result in the database and return it
def getInfoRequest(requestFormat, requestSettings):
        
        database = mysql.connector.connect(**settingDatabase.connection)
        cursor = database.cursor(buffered=True)

        cursor.execute(requestFormat, requestSettings)
        
        result = cursor.fetchall()

        database.commit()
        cursor.close()
        database.close()
       
        return result