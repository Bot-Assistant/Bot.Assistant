# Github informations
enableGithub = False
author = ""
repository = ""
version = ""

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "configuration"

# Name of the file containing the cog
cogFile = "cogConfiguration"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python",
    "prettytable"
]

# List of addons required by the addon
addonDependencies = []

# List of permissions required by the addon
addonPermissions = [
    "send_messages"
]

# Name of the command and the permission associated with it
# The permission can be a discord permission or a custom permission
commandPermissions = {
    # Permission to edit the bot's logs channel
    "cmdLogsChannel" : "configuration.logs.channel",

    # Permission to edit the bot's logs level
    "cmdLogsLevel" : "configuration.logs.level",
    
    # Permission to add permissions of a role
    "cmdPermissionAdd" : "discord.permission.manage_roles",

    # Permission to remove permissions of a role
    "cmdPermissionRemove" : "discord.permission.manage_roles",

    # Permission to list the permissions of a role
    "cmdPermissionList" : "discord.permission.manage_roles",

    # Permission to check the bot's permissions
    "cmdRequirements" : "discord.permission.manage_guild"
}