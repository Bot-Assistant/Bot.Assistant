from datetime import datetime


# Get time in format: HH:MM:SS
def getHMS():
    now = datetime.now()
    date_time_str = now.strftime("%H:%M:%S")
    return date_time_str

# Get time in format: DD-MM-YYYY
def getYMD():
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d")
    return date_time_str