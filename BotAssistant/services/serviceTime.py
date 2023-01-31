from datetime import datetime

# Class for getting time
class classTime:
    # Get time in format: HH:MM:SS
    def getHMS():
        now = datetime.now()
        date_time_str = now.strftime("%H:%M:%S")
        return date_time_str

    # Get time in format: DD-MM-YYYY
    def getDMY():
        now = datetime.now()
        date_time_str = now.strftime("%d-%m-%Y")
        return date_time_str