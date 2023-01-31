import addons.reactionrole.handlers.handlerReactionRole as handlerReactionRole
import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger

async def create(ctx, channel_id, message_id, role, emote, reactionType):
    if ctx.author.guild_permissions.manage_roles:
        
        channel = None
        message = None
        
        embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="New reaction role added \n This may take some time.", color=0x00ff00)
        embedSend = await ctx.respond(embed=embed)
        
        #Verification du channel
        try:
            channel = serviceBot.classBot.getBot().get_channel(int(channel_id))
        except Exception as error:
            print("[Module][OnRawReactionAdd] Get channel error ->" + error)
        
        #Si le channel est trouvé
        if channel != None:
            #Verification du message
            try:
                message = await channel.fetch_message(int(message_id))
            except Exception as error:
                message = None
                print("[Module][OnRawReactionAdd] Get message error -> " + str(error))
            

        #Field du message
        if channel != None and message != None:
            #Message Commande
            embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="New reaction role added ", color=0x00ff00)
            embed.add_field(name="Guild ID", value=str(ctx.guild.id) + " -> " + ctx.guild.name, inline=False)
            embed.add_field(name="Channel ID", value=str(channel_id) + " -> " + channel.name, inline=False)
            embed.add_field(name="Message ID", value=str(message_id), inline=False)
            embed.add_field(name="Role ID", value=str(role.id) + " -> " +  role.name, inline=False)
            embed.add_field(name="Emote", value=str(emote), inline=False)
            embed.add_field(name="Type of reaction", value=str(reactionType), inline=False)
            await embedSend.edit_original_response(embed=embed)
            
            match reactionType:
                case "Ajoute/Supprime le role":
                    reactionType = 2
                case "Ajoute le role":
                    reactionType = 1
                case "Supprime le role": 
                    reactionType = 0
            
            #Add reaction
            try:
                await message.add_reaction(emote)
            except Exception as error:
                print("[Module][OnRawReactionAdd] Add reaction error -> " + str(error))
                
                #Message Commande
                embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="Emote not found on this server.", color=0xCD2B2B)
                await ctx.respond(embed=embed)
                
                return
            
            #Ajout BDD
            handlerReactionRole.createReactionRole(ctx.guild.id, channel_id, message_id, role.id, emote, reactionType)
            
            #Logs
            await serviceDiscordLogger.discordLogger.warn("A new reaction role has been created by " + ctx.author.name + " -> " + role.name, ctx.guild.id)
        else:
            #Message Commande
            embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="The channel or message ID was not found on this server.", color=0xCD2B2B)
            await ctx.respond(embed=embed)