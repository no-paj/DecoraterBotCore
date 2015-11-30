import discord

def kills(client, message):
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