import discord

from discord.ext import commands


class classBot:
    bot = None
    discord = None
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

    def initialize():
        intents = discord.Intents.all()
        classBot.bot = discord.Bot(intents=intents)
        classBot.discord = discord
        classBot.client = discord.Client
        classBot.commands = commands
