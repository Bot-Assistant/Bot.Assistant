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
        # Connect to the database
        database = mysql.connector.connect(**settingDatabase.connection)

        # Create a cursor
        cursor = database.cursor()

        # Execute the request
        cursor.execute(requestFormat, requestSettings)

        # Commit the changes
        database.commit()

        # Close the cursor
        cursor.close()

        # Close the database
        database.close()


# Find a result in the database and return it
def getInfoRequest(requestFormat, requestSettings):
        # Connect to the database
        database = mysql.connector.connect(**settingDatabase.connection)

        # Create a cursor with cache
        cursor = database.cursor(buffered=True)

        # Execute the request
        cursor.execute(requestFormat, requestSettings)
        
        # Get the result
        result = cursor.fetchall()

        # Close the cursor
        database.commit()

        # Close the database
        cursor.close()

        # Close the database
        database.close()
        
        # Return the result
        return result