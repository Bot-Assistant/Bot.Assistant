[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=for-the-badge)](https://www.python.org/)
[![wakatime](https://wakatime.com/badge/user/f59667a1-6452-42a0-8127-4e5133353d0b/project/4447d8de-24b5-46bf-9d97-047ba49109b6.svg?style=for-the-badge)](https://wakatime.com/badge/user/f59667a1-6452-42a0-8127-4e5133353d0b/project/4447d8de-24b5-46bf-9d97-047ba49109b6)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](http://perso.crans.org/besson/LICENSE.html)

[![Latest release](https://badgen.net/github/release/Ted-18/Bot.Assistant?style=for-the-badge)](https://github.com/Ted-18/Bot.Assistant/releases)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?style=for-the-badge)](https://github.com/Naereen/badges/)


# Bot.Assistant
![image](https://user-images.githubusercontent.com/84779771/229033259-682fb313-9dbd-41c0-aabd-1041e94c434f.png)



**Need help or informations?** [Join our Discord](https://discord.gg/xJ7tmEUnc3)

## Introduction
An open source Python (Py-Cord) Discord bot with addons features.

This bot is inspired by game servers like Minecraft. You will be able to configure the bot as well as addons in the folder provided for that purpose. Once this is done, you just have to restart the bot and that's it!


## Available features
- A discord/console logger
- An addon management system
- A tool for cleaning cache files
- An advanced permissions system (custom permissions or discord)
- A GitHub update checking system
- A system of verification of pip modules
- A simplified database usage system


## Prerequisites
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

- A **compatible database**
- Python 3.10 recommended **with PIP**
- Active bot discord token


## Compatibility
![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Apple](https://img.shields.io/badge/Apple-%23000000.svg?style=for-the-badge&logo=apple&logoColor=white)

🔰 We **recommend** using the [Pterodactyl](https://pterodactyl.io/) tool.
| OS Compatibility | Database Compatibility |
|------------------|------------------------|
| Linux ✅          | Maria DB ✅             |
| Windows ✅        | SQLite ✅               |
| MacOS (Linux) ✅  | MySQL ❌                |


## Installation
### Manual Installation
1. Download the bot
2. Extract the bot
3. Open CMD.exe and write the command below.
  - `pip install py-cord mysql-connector-python importlib_metadata requests prettytable`
4. Make sure you have created a database
5. Run bot.py with Python (run.bat on windows)
6. Configure the bot database when the bot create the file `settingDatabase.py`
7. Restart the bot
8. Configure the bot token when the bot create the file `settingToken.py`
9. (Facultative) Install addons in the folder `addons`
10. Restart the bot
11. Enjoy!


## Configuration
### Database 
```py
# Please fill in the fields below to configure the database
connection = {
    "host": "",
    "database": "",
    "user": "",
    "password": ""
}
```
### Token
```py
# Please fill in the field below to configure the bot token
token = ""
```


## Addons available
- [Join Role](https://github.com/Ted-18/Bot.Assistant-JoinRole)
- [Reaction Role](https://github.com/Ted-18/Bot.Assistant-ReactionRole)
- [Level System](https://github.com/Ted-18/Bot.Assistant-LevelSystem)
- [Sound Play](https://github.com/Ted-18/Bot.Assistant-SoundPlay)
