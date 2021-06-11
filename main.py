import discord
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.BaseLoader)

client = discord.Client()
prefix = config['prefix']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix+'ping'):
        await message.channel.send('Pong!')

client.run(config['token'])
