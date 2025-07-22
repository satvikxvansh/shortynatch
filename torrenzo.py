import discord
from discord.ext import commands
import os
import web_scraper
import requests
from y1 import youtubedownloader

Intents = discord.Intents.all()
Intents.members = True
Intents.message_content = True

token = 'OTg5MDgyuseyourtokenmoforQgYRaNCNAxocO23Wyp7AumeI'         
dictionary = {'link' : [0,0,0,0,0] , 'name' : [0,0,0,0,0] , 'seeder' : [0,0,0,0,0] , 'size' : [0,0,0,0,0]}

client = commands.Bot(command_prefix = '.' , intents = Intents)

@client.event

async def on_ready():
    print('Hello bitches')
    await client.change_presence(activity = discord.Game("with torrents \U0001F609")) 

@client.command()
async def hello(ctx):
  await ctx.send("wassup")

@client.event

async def on_message(message):
        if message.content.startswith('/movie'):
          torrent = message.content
          requested_torrent ='&Category=2030&Category=2040&Category=2045&Query=' + torrent.lstrip("/movie ")
          torrent_request = requested_torrent.replace(' ', '+')
          answer = web_scraper.torrent(torrent_request)

          for i in range(5):
           try:
            name = answer['Title'][i]
            dictionary['seeder'][i] = answer['Seeders'][i]
            dictionary['name'][i] =name
            dictionary['link'][i] = answer['LINK'][i]
            dictionary['size'][i] = answer['Size'][i]
            await message.channel.send(name)
            embedio = discord.Embed(
            title = answer['Title'][i] ,
            description = "",
            colour = discord.Colour.random())
            embedio.set_author(name = message.author.name)
            embedio.add_field(name = 'Seeders' , value = answer['Seeders'][i]) 
            size = int(answer['Size'][i])/1073741824
            embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))  
                
            await message.channel.send(embed=embedio)
            if(i==4):
             await message.channel.send('React with these emojis 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ to indicate your choice')
           except:
            if i==0:
              await message.channel.send("Failed to find anything.... Maybe refine the name..?")
              break
            else:
             await message.channel.send("I failed to find any further results react with  1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ if you like any result.")
             break


        elif message.content.startswith('/tv'):
          torrent = message.content
          requested_torrent ='&Category=5030&Category=5040&Query=' + torrent.lstrip("/tv ")
          torrent_request = requested_torrent.replace(' ', '+')
          answer = web_scraper.torrent(torrent_request)

          for i in range(5):
           try:
            name = answer['Title'][i]
            name = answer['Title'][i]
            dictionary['seeder'][i] = answer['Seeders'][i]
            dictionary['name'][i] =name
            dictionary['link'][i] = answer['LINK'][i]
            dictionary['size'][i] = answer['Size'][i]
            embedio = discord.Embed(
            title = answer['Title'][i] ,
            description = "",
            colour = discord.Colour.random())
            embedio.set_author(name = message.author.name)
            embedio.add_field(name = 'Seeders' , value = answer['Seeders'][i]) 
            size = int(answer['Size'][i])/1073741824
            embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))            
            await message.channel.send(embed=embedio)
            if(i==4):
             await message.channel.send('React with these emojis 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ to indicate your choice')
           except:
            if i==0:
              await message.channel.send("Failed to find anything.... Maybe refine the name..?")
              break
            else:
             await message.channel.send("I failed to find any further results react with  1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ if you like any result.")
             break


        elif message.content.startswith('/anime'):
          torrent = message.content
          requested_torrent ='&Category=100078&Category=100080&Category=100028&Query=' + torrent.lstrip("/anime ")
          torrent_request = requested_torrent.replace(' ', '+')
          answer = web_scraper.torrent(torrent_request)


          for i in range(5):
           try:
            name = answer['Title'][i]
            name = answer['Title'][i]
            dictionary['seeder'][i] = answer['Seeders'][i]
            dictionary['name'][i] =name
            dictionary['link'][i] = answer['LINK'][i]
            dictionary['size'][i] = answer['Size'][i]
            embedio = discord.Embed(
            title = answer['Title'][i] ,
            description = "",
            colour = discord.Colour.random())
            embedio.set_author(name = message.author.name)
            embedio.add_field(name = 'Seeders' , value = answer['Seeders'][i]) 
            size = int(answer['Size'][i])/1073741824
            embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))            
            await message.channel.send(embed=embedio)
            if(i==4):
             await message.channel.send('React with these emojis 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ to indicate your choice')
           except:
            if i==0:
              await message.channel.send("Failed to find anything.... Maybe refine the name..?")
              break
            else:
             await message.channel.send("I failed to find any further results react with  1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ if you like any result.")
             break


        elif message.content.startswith('/game'):
          torrent = message.content
          requested_torrent ='&Category=4050&Query=' + torrent.lstrip("/game ")
          torrent_request = requested_torrent.replace(' ', '+')
          answer = web_scraper.torrent(torrent_request)       

          for i in range(5):
           try:
            name = answer['Title'][i]
            name = answer['Title'][i]
            dictionary['seeder'][i] = answer['Seeders'][i]
            dictionary['name'][i] =name
            dictionary['link'][i] = answer['LINK'][i]
            dictionary['size'][i] = answer['Size'][i]
            embedio = discord.Embed(
            title = answer['Title'][i] ,
            description = "",
            colour = discord.Colour.random())
            embedio.set_author(name = message.author.name)
            embedio.add_field(name = 'Seeders' , value = answer['Seeders'][i]) 
            size = int(answer['Size'][i])/1073741824
            embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))            
            await message.channel.send(embed=embedio)
            if(i==4):
             await message.channel.send('React with these emojis 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ to indicate your choice')
           except:
            if i==0:
              await message.channel.send("Failed to find anything.... Maybe refine the name..?")
              break
            else:
             await message.channel.send("I failed to find any further results react with  1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ if you like any result.")
             break
        elif message.content.startswith('/hello'):
          if(message.author.name == 'druvvv'):
            await message.channel.send("Hello Sir!!\U0001F6D0")
          else:
            await message.channel.send("Hello there!!")
        elif message.content.startswith('/gpa'):
          content = message.content.lstrip('/gpa ')
          sgpa_list = content.split(' ')
          gpa = (float(sgpa_list[0])*25 + float(sgpa_list[1])*24 + float(sgpa_list[2])*24)/73.00
          await message.channel.send('Your GPA is ' +'%.2f' % gpa)

        elif message.content.startswith('/youtube'):
          content = message.content.lstrip('/youtube ')
          youtubedownloader(content)
          await message.channel.send(file = discord.File(f'./youtube.mp4'))
          os.remove(f'./youtube.mp4')





@client.event

async def on_reaction_add(reaction , user):
   if(str(reaction.emoji) == '1️⃣' and reaction.message.author.name == "Torrenzo"):
    # webbrowser.open(answerlist[0])
    name = dictionary['name'][0]
    embedio = discord.Embed(
    title = name ,
    description = "" ,
    colour = discord.Colour.random())
    embedio.set_author(name = user)
    embedio.add_field(name = 'Seeders' , value = dictionary['seeder'][0])
    size = int(dictionary['size'][0])/1073741824
    embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))
    embedio.add_field(name = 'Magnet URL' , value = dictionary['link'][0] , inline = False)
    await reaction.message.channel.send(embed=embedio)

   elif(str(reaction.emoji) == '2️⃣' and reaction.message.author.name == "Torrenzo"):
    name = dictionary['name'][1]
    embedio = discord.Embed(
    title = name , 
    description = "" ,
    colour = discord.Colour.random())
    embedio.set_author(name = user)
    embedio.add_field(name = 'Seeders' , value = dictionary['seeder'][1])
    size = int(dictionary['size'][1])/1073741824
    embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))
    embedio.add_field(name = 'Magnet URL' , value = dictionary['link'][1] , inline = False)
    await reaction.message.channel.send(embed=embedio)

   elif(str(reaction.emoji) == '3️⃣' and reaction.message.author.name == "Torrenzo"): 
    name = dictionary['name'][2]
    embedio = discord.Embed(
    title = name ,
    description = "" ,
    colour = discord.Colour.random())
    embedio.set_author(name = user)
    embedio.add_field(name = 'Seeders' , value = dictionary['seeder'][2])
    size = int(dictionary['size'][2])/1073741824
    embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))
    embedio.add_field(name = 'Magnet URL' , value = dictionary['link'][2] , inline = False)
    await reaction.message.channel.send(embed=embedio)

   elif(str(reaction.emoji) == '4️⃣' and reaction.message.author.name == "Torrenzo"):
    name = dictionary['name'][3]
    embedio = discord.Embed(
    title = name ,
    description = "" ,
    colour = discord.Colour.random())
    embedio.set_author(name = user)
    embedio.add_field(name = 'Seeders' , value = dictionary['seeder'][3])
    size = int(dictionary['size'][3])/1073741824
    embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))
    embedio.add_field(name = 'Magnet URL' , value = dictionary['link'][3] , inline = False)
    await reaction.message.channel.send(embed=embedio)
   
   elif(str(reaction.emoji) == '5️⃣' and reaction.message.author.name == "Torrenzo"):
    name = dictionary['name'][4]
    embedio = discord.Embed(
    title = name ,
    description = "" ,
    colour = discord.Colour.random())
    embedio.set_author(name = user)
    embedio.add_field(name = 'Seeders' , value = dictionary['seeder'][4])
    size = int(dictionary['size'][4])/1073741824
    embedio.add_field(name = 'Size' , value = ('%.2f' % size+'GB'))
    embedio.add_field(name = 'Magnet URL' , value = dictionary['link'][4] , inline = False)
    await reaction.message.channel.send(embed=embedio)



    




client.run(token)

