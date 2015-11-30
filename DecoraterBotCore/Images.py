import discord
import random
import io

def images(client, message):
    if(message.content.startswith('::catgirls')):
        randomnumber = random.randint(1, 43)
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
        if randomnumber == 16:
            file = './images/20151129121812e68.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 17:
            file = './images/20151129121818f9f.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 18:
            file = './images/20151129121826d6a.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 19:
            file = './images/20151129121842d11.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 20:
            file = './images/20151129121844edb.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 21:
            file = './images/20151129121846da0.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 22:
            file = './images/20151129121848ef3.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 23:
            file = './images/20151129121901d57.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 24:
            file = './images/20151129121915b23.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 25:
            file = './images/20151129121923ec6.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 26:
            file = './images/20151129121925d15.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 27:
            file = './images/201511291218105a9.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 28:
            file = './images/201511291218162ab.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 29:
            file = './images/201511291218241de.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 30:
            file = './images/201511291218302de.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 31:
            file = './images/201511291218341f8.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 32:
            file = './images/201511291218366bc.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 33:
            file = './images/201511291218526bf.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 34:
            file = './images/201511291218546e8.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 35:
            file = './images/201511291219035cf.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 36:
            file = './images/201511291219138c0.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 37:
            file = './images/2015112912180884a.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 38:
            file = './images/20151129121838459.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 39:
            file = './images/20151129121905757.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 40:
            file = './images/tumblr_nyenqpib0y1uuunxio1_540.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 41:
            file = './images/tumblr_nykzh8JQpM1qa63ddo1_540.png'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 42:
            file = './images/c20557cef189eb39fd9bdfaf838e17fb.jpg'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        if randomnumber == 43:
            file = './images/b937e2243f69483030ae55a413cc7548.gif'
            client.send_message(message.channel, 'Image: ' + str(randomnumber))
            client.send_file(message.channel, file)
        file2 = io.open('images.txt', 'a')
        number = unicode(str(randomnumber), 'utf-8')
        file2.write('Image=' + number + "\n")