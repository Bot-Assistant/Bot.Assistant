How to build an addon for BotAssistant:
    Create a new folder in the addons folder called <addonname>
    
    Create a new file in the folder called cog<Addonname>.py
        Add in this file all your commands for the bot.
    
    Create a new folder named "functions" in the folder <addonname>
        Add in this folder all the functions you need for your addon.

        For example: If you need a function to get the current the name of all users and send an embed to them.
            Create a new file in the folder "functions" called "func<CommandName>.py"
            Add in this file the function you need.

        You can use all the functions from the main bot in your addon. (For example: import services.serviceDiscordLogger)

    If you need to use the database you can createFolder named "handlers".
        So you can now use "import services.serviceDatabase as serviceDatabase" in your addon.
        You can now copy and paste another handler to create your own.

    
    If I can give you a method, think about your needs when using the database. 
    Make a useful function(s) for your addon and then create your command.
    Take inspiration from already existing addons. 

    Dont forget to add your addon to the addons list in the main bot file.