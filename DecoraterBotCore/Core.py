import os
import discord
import requests
import io
#import os.path
import ctypes
#import subprocess
#import json
#import socket
#import logging
import random

#logger = logging.getLogger('discord')
#logger.setLevel(logging.ERROR)
#handler = logging.FileHandler(filename='errors.txt', encoding='utf-8', mode='a')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s\n'))
#logger.addHandler(handler)
discord_user_id = '94203228043874304'
discord_server_id = '93740277918871552' #Amiable Server ID.
discord_server_id2 = '81392063312044032' #Ambition Server ID.
discord_server_id3 = '103685935593435136' #Division Server ID.
discord_server_id4 = '106770319661862912' #!catgirls.wtf ! Server ID.
version = 'v1.0.0.12 Pre-Beta'
sourcelink = ' https://github.com/AraHaan/DecoraterBot/'
sourcelink2 = ' https://github.com/AraHaan/DecoraterBotCore/'
botcommands = 'Available commands:\n\n**::kill <lamp or cliff> <optionally mention someone>**\n**::changelog**\n**::raid <optionally mention where>**\n**::pyversion**\n**::source**\n**::prune <number of messages to remove>**\n**::game <game id in games.json>**'
changelog = "Created DecoraterBot.\n" + version + "\n\nChanges:\n+ Added **::source** command"


client = discord.Client()

def changeWindowTitle():
    ctypes.windll.kernel32.SetConsoleTitleA("DecoraterBot " + version)

@client.event
def commands(client, message):
    if message.content is not None:
        file = io.open('log.txt', 'a', encoding='utf-8')
        file.write('Name=' + message.author.name + ' ' + 'ID=' + message.author.id + ' Server=' + message.channel.server.name + ' Channel=' + message.channel.name + ' Message=' + message.content + "\n")
    if(message.content.startswith('::join')):
#        Test code: https://discord.gg/0bdcPnlfrdnn2jgR
        if message.author.id == discord_user_id:
            code = message.content[len("::join "):].strip()
            if code is not None:
                client.invite_by_code(code)
            else:
                client.send_message(message.channnel, 'Sorry,, You did not specify a code to Join a Server.')
    if(message.content.startswith('::kill')):
        for disuser in message.mentions:
            user = discord.utils.find(lambda member: member.name == disuser.name, message.channel.server.members)
            if "lamp" in message.content.split():
                client.send_message(message.channel, message.author.mention() + " took a lamp out and hit " + user.mention() + " in the head and kills them.") 
                break
            if "cliff" in message.content.split():
                client.send_message(message.channel, message.author.mention() + " Binds and gags and throws " + user.mention() + " off a cliff to their death.")
                break
        else:
            if "lamp" in message.content.split():
                client.send_message(message.channel, message.author.mention() + " took a lamp out and hit them in the head and kills them.")
            if "cliff" in message.content.split():
                client.send_message(message.channel, message.author.mention() + " Binds and gags and throws them off a cliff to their death.")
    elif(message.content.startswith('::catgirls')):
        randomnumber = random.randint(1, 15)
        if randomnumber == 1:
            file = './images/9bb44f2a4acee610c940ee0327f2ce8b.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 2:
            file = './images/14653e8c1f0a80296b5a5c01017912c2.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 3:
            file = './images/1112687-R5SDPEW.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 4:
            print(str(randomnumber))
            file = './images/1343675387092.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 5:
            file = './images/1343675387092.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 6:
            file = './images/a53fe33f9089abe6279608238672eec7.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 7:
            file = './images/e64265ec8e9ac1881b41e0ec1aafab63.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 8:
            print(str(randomnumber))
            file = './images/Konachan.com_-_133720_sample.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 9:
            file = './images/sample_9e690f4c5f9871c9a3364e056f9f71eafa425cfd.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 10:
            file = './images/sample-1eeade1870f5ff956d389898e386f80b.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 11:
            file = './images/tumblr_nxz1veWBX01trsoo7o1_540.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 12:
            file = './images/tumblr_ny6rzgsIw51t01xvho1_540.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 13:
            file = './images/tumblr_nyh9sldlw01uaruy3o1_540.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 14:
            file = './images/tumblr_nyh98d8HCr1uj1yeoo1_540.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 15:
            file = './images/tumblr_nyhiunNdN61v00m63o1_500.gif'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        file2 = io.open('images.txt', 'a')
        number = unicode(str(randomnumber), 'utf-8')
        file2.write('Image=' + number + "\n")
    elif(message.content.startswith('::commands')):
        client.send_message(message.channel, botcommands)
    elif(message.content.startswith('::color')):
        if "!pink" in message.content:
            desrole = message.content[len("::color !pink "):].strip()
            role = discord.utils.find(lambda role: role.name == desrole, message.channel.server.roles)
            value = 'ff3054'
            client.edit_role(message.channel.server, role, color=discord.Color(value))
        if "!brown" in message.content:
            desrole = message.content[len("::color !brown "):].strip()
            role = discord.utils.find(lambda role: role.name == desrole, message.channel.server.roles)
            value = '652d2d'
            client.edit_role(message.channel.server, role, color=discord.Color(value))
    elif(message.content.startswith('::changelog')):
        client.send_message(message.channel, changelog)
    elif(message.content.startswith('::raid')):
        result = message.content[len("::raid "):].strip()
        client.send_message(message.channel, '@everyone RAID Boss ' + result)
    elif(message.content.startswith('::pyversion')):
        client.send_message(message.channel, message.author.mention() + " I was made with ``Python v2.7.10 (x86).``\n\nCompiled to exe by py2exe.")
    elif(message.content.startswith('::Libs')):
        libs = 'Libs used: \n```Discord.py, DecoraterBotCore, and other libs```'
        client.send_message(message.channel, libs)
    elif(message.content.startswith('::source')):
        client.send_message(message.channel, message.author.mention() + sourcelink + '\n Core:' + sourcelink2)
    elif(message.content.startswith('::gamelist')):
        file = './games.json'
        client.send_file(message.channel, file)
    elif(message.content.startswith('::game')):
        desgame = message.content[len("::game "):].strip()
        client.change_status(game_id=desgame, idle=True)
    elif(message.content.startswith('::debug')):
        if message.author.id == discord_user_id:
            debugcode = message.content[len("::debug "):].strip()
            debugcode = eval(debugcode)
            debugcode = str(debugcode)
            client.send_message(message.channel, "```Python\n" + debugcode + "\n```")
    elif(message.content.startswith('::close')):
        client.send_message(message.channel, "**DecoraterBot Status: Offline**")
        os.startfile(".\Decorater.exe")
        client.logout()
    elif(message.content.startswith('#rekt')):
        client.send_message(message.channel, message.author.mention() + "You just pissed yourself didn't you?\ngit gud.")
    elif(message.content.startswith('::secret')):
        msg = client.send_message(message.channel, 'You Like Weed.')
        client.edit_message(msg, '**I Like Pie.**')
    elif(message.content.startswith('::prune')):
        if message.channel.server and message.channel.server.id == discord_server_id:
            role4 = discord.utils.find(lambda role: role.name == 'GM', message.channel.server.roles)
            role5 = discord.utils.find(lambda role: role.name == '@admins', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role4 or discord_user_id or role5:
                opt = message.content[len("::prune "):].strip()
                num = 1
                if opt:
                    try:
                        num = int(opt)
                    except:
                        return
                to_remove = [m for m in client.logs_from(message.channel, limit=num + 1)]
                for log_message in to_remove:
                    client.delete_message(log_message)
            else:
                client.send_message(message.channel, 'You are not the Right Role to use this command.')
        if message.channel.server and message.channel.server.id == discord_server_id2:
            role2 = discord.utils.find(lambda role: role.name == 'Leaders', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role2 or discord_user_id:
                opt = message.content[len("::prune "):].strip()
                num = 1
                if opt:
                    try:
                        num = int(opt)
                    except:
                        return
                to_remove = [m for m in client.logs_from(message.channel, limit=num + 1)]
                for log_message in to_remove:
                    client.delete_message(log_message)
            else:
                client.send_message(message.channel, 'You are not the Right Role to use this command.')
        if message.channel.server and message.channel.server.id == discord_server_id3:
            role2 = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
            role3 = discord.utils.find(lambda role: role.name == 'Guild Master', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role2 or discord_user_id or role3:
                opt = message.content[len("::prune "):].strip()
                num = 1
                if opt:
                    try:
                        num = int(opt)
                    except:
                        return
                to_remove = [m for m in client.logs_from(message.channel, limit=num + 1)]
                for log_message in to_remove:
                    client.delete_message(log_message)
            else:
                client.send_message(message.channel, 'You are not the Right Role to use this command.')
        if message.channel.server and message.channel.server.id == discord_server_id4:
            opt = message.content[len("::prune "):].strip()
            num = 1
            if opt:
                try:
                    num = int(opt)
                except:
                    return
            to_remove = [m for m in client.logs_from(message.channel, limit=num + 1)]
            for log_message in to_remove:
                client.delete_message(log_message)
@client.event
def on_error(event, *args, **kwargs):
    logger.exception('Exception occurred in {}'.format(event))