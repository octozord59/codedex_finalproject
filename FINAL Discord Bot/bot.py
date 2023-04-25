import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_joke():
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  json_data = json.loads(response.text)
  print(response)
  return json_data['setup']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

        if message.content.startswith('$joke'):
            await message.channel.send(get_joke())
            


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA5NjYxNzA3NTM3MzUwNjYyMQ.GmlxDP.qtqCKQ5ScgsHyqbqCRZYqiOl4KcfH-xO9SYncEaa')