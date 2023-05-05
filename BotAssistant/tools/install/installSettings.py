import tools.install.messages.messageLogo as messageLogo
import tools.install.settings.settingBotEditor as settingBotEditor
import tools.install.settings.settingQuestions as settingQuestions

def install():

    messageLogo.send()
    if input("Write 'y' to configure settings, space to skip:") != "y":
        return

    settingBotEditor.settingBotBool("consoleColor", settingQuestions.colorSetting())
    settingBotEditor.settingBotBool("debug", settingQuestions.debugSetting())
    settingBotEditor.settingBotBool("addonVerification", settingQuestions.addonsSetting())
    settingBotEditor.settingBotBool("dependenciesVerification", settingQuestions.dependenciesSetting())
    

    databaseTypeDict = {
        "1": "MariaDB", 
        "2": "SQLite"
        }
    settingBotEditor.settingBotList("databaseType", settingQuestions.databaseTypeSetting(), databaseTypeDict)