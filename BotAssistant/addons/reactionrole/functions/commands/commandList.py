import addons.reactionrole.handlers.handlerReactionRole as handlerReactionRole
import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger
            
async def list(ctx, page):
    if ctx.author.guild_permissions.manage_roles:
        #Listing BDD
        liste = handlerReactionRole.getReactionRole(ctx.guild.id)
        
        if len(liste) == 0:
            embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="You have not created any reaction roles.", color=0x00ff00)
            embedSend = await ctx.respond(embed=embed)
            return
        
        if page == None:
            page = 1
        
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="List of actual reaction role list \n The verification can be long \n \n Tu as sélectionné la page numéro **" + str(page) + "**", color=0x00ff00)
        embedSend = await ctx.respond(embed=embed)

        #Liste des reaction roles
        for reaction in liste[page * 25 - 25:page * 25]:
            
            #Verification du role
            guild = serviceBot.classBot.getBot().get_guild(ctx.guild.id)
            role = serviceBot.classBot.getDiscord().utils.get(guild.roles, id=reaction[3])
            
            #Verification du channel
            try:
                channel = serviceBot.classBot.getBot().get_channel(int(reaction[1]))
            except Exception as error:
                print("[Module][OnRawReactionAdd] Get channel error ->" + error)
            

            #Si le channel est trouvé
            if channel != None:
                #Verification du message
                try:
                    message = await channel.fetch_message(reaction[2])                    
                except Exception as error:
                    message = None
                    print("[Module][OnRawReactionAdd] Get message error -> " + str(error))
            
            try:
                #Field du message
    
                
                
                if role == None or channel == None or message == None:
                    embed.add_field(
                        name="ID: " + str(reaction[0]), 

                        value="This reaction role is not working ❌ "
                        +" \n```" 
                        + "Channel: " + str(reaction[1]) 
                        + "\nMessage: " + str(reaction[2]) 
                        + "```", 
                        
                        inline=False)
                else:
                    embed.add_field(
                        name="ID: " + str(reaction[0]),
                        value="This reaction role is working ✅"
                            +" \n```" 
                            + "Channel: " + str(channel) 
                            + "\nMessage: " + str(reaction[2])
                            + "\nEmoji: " + str(reaction[4])
                            + "```", 

                            inline=False)
                                        
                await embedSend.edit_original_response(embed=embed)
            except Exception as error:
                print("[Module][OnRawReactionAdd] Edit message error -> " + str(error))
        
        #Logs
        await serviceDiscordLogger.discordLogger.info("The list of reaction roles has been requested by  " + ctx.author.name, ctx.guild.id)
        
    else:
        #Message Commande
        embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="You do not have permission to execute this command.", color=0xCD2B2B)
        await ctx.respond(embed=embed)
        
        #Logs
        await serviceDiscordLogger.discordLogger.info("The user " + ctx.author.name + " wanted to type the command: /reactionrole list", ctx.guild.id)