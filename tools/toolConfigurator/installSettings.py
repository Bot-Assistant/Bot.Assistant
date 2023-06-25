import os 
import services.serviceConsoleMessages as serviceConsoleMessages
import tools.toolConfigurator.settings.settingBotEditor as settingBotEditor
import tools.toolConfigurator.settings.settingQuestions as settingQuestions

def install():

    if os.path.exists("settings/settingDatabase.py"):
        
        serviceConsoleMessages.logo()
        print("Write 'y' to configure settings, space to skip:")
        if input("Answer: ") != "y":
            return

    settingBotEditor.settingBotBool("consoleColor", settingQuestions.colorSetting())
    settingBotEditor.settingBotBool("debug", settingQuestions.debugSetting())
    settingBotEditor.settingBotBool("addonUpdate", settingQuestions.addonUpdateSetting())
    settingBotEditor.settingBotBool("addonVerification", settingQuestions.addonsSetting())
    settingBotEditor.settingBotBool("dependenciesVerification", settingQuestions.dependenciesSetting())
    

    databaseTypeDict = {
        "1": "MariaDB", 
        "2": "SQLite"
        }
    settingBotEditor.settingBotList("databaseType", settingQuestions.databaseTypeSetting(), databaseTypeDict)