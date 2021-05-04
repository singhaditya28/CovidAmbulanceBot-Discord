import discord
import os
import search_runpee
from dotenv import load_dotenv

# Use python-dotenv pakcage to get variables stored in .env file of your project
load_dotenv()

client = discord.Client()

hello_message = '''**Hello there!** *I\'m the fidgeting bot from Aditya. 
Please use me by typing* **`$amb city_name`** *to show available ambulance services in your area.* 
For Example - **`$amb delhi`** '''

#read my manual by typing $help or $commands while I\'m looking around in this server.'''

no_result_message = '''Sorry :pensive: , we can\'t find any services in the area you are searching for. We may not have found anything about it yet, 
but you can try again later or try changing the area. :pray: '''

# instantiate RunPeeWeb class from search_runpee.py
runpee_web = search_runpee.RunPeeWeb()

@client.event
async def on_ready():
  print(f'{client.user} is now online!')

@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  

  
  if message.content.startswith(f'$hello'):
    await message.channel.send(hello_message)
  
  if f'$amb' in message_content:

    key_words, search_words = runpee_web.key_words_search_words(message_content)
    result_links, anylink = runpee_web.search(key_words)
    links = runpee_web.send_link(result_links, search_words, anylink)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)


client.run(os.getenv('TOKEN'))
