import discord

def games(client, message):
    if(message.content.startswith('::gamelist')):
        file = './games.json'
        client.send_file(message.channel, file)
    elif(message.content.startswith('::game')):
        desgame = message.content[len("::game "):].strip()
        client.change_status(game_id=desgame, idle=True)