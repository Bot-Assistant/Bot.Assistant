import discord
from discord.ext import commands


class classBot:
    bot = None
    discord = None
    discordCommands = None
    client = None
    commands = None
    
    def getBot():
        return classBot.bot
    
    def getDiscord():
        return classBot.discord
    
    def getClient():
        return classBot.client
    
    def getCommands():
        return classBot.commands

    def getDiscordCommands():
        return classBot.discordCommands

    def initialize():
        intents = discord.Intents.all()
        classBot.bot = discord.Bot(intents=intents)
        classBot.discord = discord
        classBot.discordCommands = discord.commands
        classBot.client = discord.Client
        classBot.commands = commands
