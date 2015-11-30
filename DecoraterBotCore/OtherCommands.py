import discord

version = 'v1.0.0.12 Pre-Beta'
sourcelink = ' https://github.com/AraHaan/DecoraterBot/'
sourcelink2 = ' https://github.com/AraHaan/DecoraterBotCore/'
botcommands = 'Available commands:\n\n**::kill <lamp or cliff> <optionally mention someone>**\n**::changelog**\n**::raid <optionally mention where>**\n**::pyversion**\n**::source**\n**::prune <number of messages to remove>**\n**::game <game id in games.json>**'
changelog = "Created DecoraterBot.\n" + version + "\n\nChanges:\n+ Added **::source** command"

def other_commands(client, message):
    if(message.content.startswith('::commands')):
        client.send_message(message.channel, botcommands)
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
    elif(message.content.startswith('::close')):
        client.send_message(message.channel, "**DecoraterBot Status: Offline**")
        os.startfile(".\Decorater.exe")
        client.logout()
    elif(message.content.startswith('#rekt')):
        client.send_message(message.channel, message.author.mention() + "You just pissed yourself didn't you?\ngit gud.")
