import discord

discord_user_id = '94203228043874304'

def debug(client, message):
    if(message.content.startswith('::debug')):
        if message.author.id == discord_user_id:
            debugcode = message.content[len("::debug "):].strip()
            debugcode = eval(debugcode)
            debugcode = str(debugcode)
            client.send_message(message.channel, "```Python\n" + debugcode + "\n```")