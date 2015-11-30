import os
import discord
import requests
import ctypes
import random
from .Images import images
from .Invite import invite
from .Games import games
from .Logs import logs
from .Kills import kills
from .Colors import colors
from .Secret import secret
from .Debug import debug
from .Prune import prune
from .OtherCommands import other_commands

version = 'v1.0.0.12 Pre-Beta'

client = discord.Client()

def changeWindowTitle():
    ctypes.windll.kernel32.SetConsoleTitleA("DecoraterBot " + version)

@client.event
def commands(client, message):
    logs(client, message)
    invite(client, message)
    kills(client, message)
    images(client, message)
    colors(client, message)
    games(client, message)
    debug(client, message)
    other_commands(client, message)
    secret(client, message)
    prune(client, message)