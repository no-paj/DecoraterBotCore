import discord
import io

def logs(client, message):
    if message.content is not None:
        file = io.open('log.txt', 'a', encoding='utf-8')
        file.write('Name=' + message.author.name + ' ' + 'ID=' + message.author.id + ' Server=' + message.channel.server.name + ' Channel=' + message.channel.name + ' Message=' + message.content + "\n")