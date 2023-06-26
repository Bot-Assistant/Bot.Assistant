import importlib

# Description: Get the permissions list of an addon (excluding Discord permissions)
# Return: List of permissions
def getPermissionsList(addon):
    if addon is None:
        return []

    # Import the addon's init file
    addonInit = importlib.import_module("addons." + addon + ".init")

    # Get the permissions
    commandPermissions = getattr(addonInit, "commandPermissions", {})

    permissions = []

    for key, value in commandPermissions.items():
        # Check if the permission is a Discord permission
        if value.startswith("discord.permission."):
            continue

        permissions.append(value)

    return permissions
