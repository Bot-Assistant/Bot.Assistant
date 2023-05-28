import sys
import sqlite3

import mysql.connector

from services.serviceLogger import Logger

import settings.settingDatabase as settingDatabase
import settings.settingBot as settingBot


# Create the database if it does not exist
def databaseCreation(tableName: str, columns: list):
    # Create database
    try:
        Logger.table(f"[CONNECTION][{tableName}][INIT]Table {tableName} initialization...")

        if settingBot.databaseType == "MariaDB":
            # Create Table MariaDB
            requestFormat = f"""
                    CREATE TABLE IF NOT EXISTS {tableName} (
                    ID INT NOT NULL AUTO_INCREMENT,
                    PRIMARY KEY (ID)
                    );
                    """
            requestSettings = ()
        elif settingBot.databaseType == "SQLite":

            if settingDatabase.sqliteFile == "":
                Logger.critical(f"Oups, you forgot to fill in the sqliteFile field in the settingDatabase.py file")
                sys.exit(0)

            # Create Table SQLite
            requestFormat = f"""
                    CREATE TABLE IF NOT EXISTS "{tableName}" (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT
                    )
                    """
            requestSettings = []

        makeRequest(requestFormat, requestSettings)



        # Add columns
        for column in columns:


            if settingBot.databaseType == "MariaDB":
                requestFormat = f"""
                        ALTER TABLE {tableName}
                        ADD COLUMN IF NOT EXISTS {column[0]} {column[1]};
                        """
                requestSettings = ()


            elif settingBot.databaseType == "SQLite":
                
                requestFormat = f"""
                        PRAGMA table_info("{tableName}");
                        """
                requestSettings = []

                result = getInfoRequest(requestFormat, requestSettings)

                columnList = [columnArray[1] for columnArray in result]

                if column[0] not in columnList:
                    requestFormat = f"""
                            ALTER TABLE "{tableName}"
                            ADD COLUMN "{column[0]}" {column[1]};
                            """
                    requestSettings = []
            

            makeRequest(requestFormat, requestSettings)

            Logger.colomn(f"[HANDLER][{tableName}][INIT]Column {column[0]} initialization success")

        Logger.table(f"[HANDLER][{tableName}][INIT]Table {tableName} initialization success")
           
    except Exception as error:
        Logger.critical(f"[HANDLER][{tableName}][INIT]Table {tableName} initialization error -> " + str(error))
        
        # Print the complete error traceback
        Logger.critical(f"[HANDLER][{tableName}][INIT]Table {tableName} initialization error -> " + str(sys.exc_info()))

        # Print database error
        Logger.critical(f"[HANDLER][{tableName}][INIT]Table {tableName} initialization error -> " + str(error.__class__.__name__))

        sys.exit(0)


# Make a request to the database without returning a result
def makeRequest(requestFormat, requestSettings):

        if settingBot.databaseType == "MariaDB":
            # Connect to the database
            database = mysql.connector.connect(**settingDatabase.connection)

        elif settingBot.databaseType == "SQLite":
            # Connect to the database
            database = sqlite3.connect(f"settings/{settingDatabase.sqliteFile}.db")

            requestFormat = requestFormat.replace("%s", "?")

            # Convert the tuple to a list
            requestSettings = list(requestSettings)
                

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

        if settingBot.databaseType == "MariaDB":
            # Connect to the database
            database = mysql.connector.connect(**settingDatabase.connection)
        
        elif settingBot.databaseType == "SQLite":
            # Connect to the database
            database = sqlite3.connect(f"settings/{settingDatabase.sqliteFile}.db")

            requestFormat = requestFormat.replace("%s", "?")

            # Convert the tuple to a list
            requestSettings = list(requestSettings)


        # Create a cursor with cache
        cursor = database.cursor()

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