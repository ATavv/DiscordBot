import discord
import requests
import json

client = discord.Client()



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" +json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

client.run('NzkyNTM0MzQ3MTM5MjUyMjM0.X-fHIA.lS2iO9zLrAcHANYUEEkO3MQNdvE')
