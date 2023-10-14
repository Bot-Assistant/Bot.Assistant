import discord
from discord.ext import commands


class BotAssistant:

    bot = None
    discord = None
    discord_commands = None
    client = None
    commands = None

    @staticmethod
    def get_bot():
        return BotAssistant.bot

    @staticmethod
    def get_discord():
        return BotAssistant.discord

    @staticmethod
    def get_client():
        return BotAssistant.client

    @staticmethod
    def get_commands():
        return BotAssistant.commands

    @staticmethod
    def get_discord_commands():
        return BotAssistant.discord_commands

    @staticmethod
    def initialize():
        intents = discord.Intents.all()
        BotAssistant.bot = discord.Bot(intents=intents)
        BotAssistant.discord = discord
        BotAssistant.discord_commands = discord.commands
        BotAssistant.client = discord.Client
        BotAssistant.commands = commands
