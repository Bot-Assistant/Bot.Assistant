import discord
import asyncio

async def discordLogin(token: str) -> bool:

    # Create a client
    client = discord.Bot(intents=discord.Intents.all())

    # Try to login
    try:
        await client.login(token)

        print("Logged in, token is valid")
        print(" ")
        print("Intents verification... (5 secondes)")

        loop = asyncio.get_event_loop()
        task = loop.create_task(client.connect())
        
        await asyncio.sleep(5)
        await client.close()

        if task.result() == None:
            print("Intents are valid")
            return True
    
    except:
        return False
    finally:
        await client.close()
    
def verification(token: str) -> bool:
    loop = asyncio.get_event_loop()
    valid = loop.run_until_complete(discordLogin(token))
    return valid
    

    