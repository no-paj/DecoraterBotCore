import discord

def colors(client, message):
    if(message.content.startswith('::color')):
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