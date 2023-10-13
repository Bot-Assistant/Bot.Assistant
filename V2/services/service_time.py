from datetime import datetime
from V2.settings import setting_bot


# Get time in format: HH:MM:SS
def get_hms():
    timezone = setting_bot.timezone

    now = datetime.now(timezone)
    date_time_str = now.strftime("%H:%M:%S")
    return date_time_str


# Get time in format: DD-MM-YYYY
def get_dmy():
    timezone = setting_bot.timezone
    now = datetime.now(timezone)
    date_time_str = now.strftime("%Y-%m-%d")
    return date_time_str
