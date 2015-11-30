import discord
import random
import io
from os.path import isfile, join

def images(client, message):
    if(message.content.startswith('::catgirls')):
        mypath = './images/'
        images = [f.name for f in listdir(mypath) if isfile(join(mypath, f))]
        image = random.choice(images)
        client.send_message(message.channel, 'Image: ')
        client.send_file(message.channel, mypath + image)
        
        file2 = io.open('images.txt', 'a')
        file2.write('Image=' + image + "\n")
