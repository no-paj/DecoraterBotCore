import discord

def secret(client, message):
    if(message.content.startswith('::secret')):
        msg = client.send_message(message.channel, 'You Like Weed.')
        client.edit_message(msg, '**I Like Pie.**')