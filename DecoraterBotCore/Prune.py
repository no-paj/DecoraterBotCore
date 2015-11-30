import discord

discord_user_id = '94203228043874304'
discord_server_id = '93740277918871552' #Amiable Server ID.
discord_server_id2 = '81392063312044032' #Ambition Server ID.
discord_server_id3 = '103685935593435136' #Division Server ID.
discord_server_id4 = '106770319661862912' #!catgirls.wtf ! Server ID.

def prune(client, message):
    if(message.content.startswith('::prune')):
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
                    try:
                        client.delete_message(log_message)
                    except discord.HTTPException:
                        pass
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
                    try:
                        client.delete_message(log_message)
                    except discord.HTTPException:
                        pass
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
                    try:
                        client.delete_message(log_message)
                    except discord.HTTPException:
                        pass
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
                try:
                    client.delete_message(log_message)
                except discord.HTTPException:
                    pass
