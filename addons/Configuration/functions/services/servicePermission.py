# PERMISSIONS CHECK
import addons.Configuration.init as init
import services.serviceResponse as serviceResponse
import services.servicePermissionManager as servicePermissionManager

async def permissionCheck(ctx, permissionName: str) -> bool:
    permissionNeeded = init.commandPermissions[permissionName]
    permissionBool = await servicePermissionManager.messageAuthorHasPermission(ctx, permissionNeeded)

    if permissionBool != True:
        await serviceResponse.noPermission(ctx, permissionNeeded)
        return False
    
    return True