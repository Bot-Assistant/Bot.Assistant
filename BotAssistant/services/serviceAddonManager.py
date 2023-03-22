
import importlib

# Description: Get the permissions list of an addon (without discord permissions)
# Return: List of permissions
def getPermissionsList(addon):

    if addon is None:
        return []

    # Import the init file of the addon
    addonInit = importlib.import_module("addons." + addon + ".init")

    # Get the permissions
    commandPermissions = addonInit.commandPermissions

    permissions = []

    for key, value in commandPermissions.items():
        
        # Check if the permission is a discord permission
        if value.startswith("discord.permission."):
            continue

        permissions.append(value)

    return permissions


