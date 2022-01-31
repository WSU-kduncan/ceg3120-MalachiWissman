import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')

        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
     )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    star_wars_quotes = [
        'I find your lack of faith disturbing.',
        'Do. Or do not. There is no try.',
        'There’s always a bigger fish.',
        'You can’t stop the change, any more than you can stop the suns from setting.',
    ]

    talladega_nights_quotes = [
        'You Sound Like A Dog With Peanut Butter On The Roof Of Your Mouth.',
        'Shake And Bake!!',
        'Well, Let Me Just Quote The Late-Great Colonel Sanders, Who Said... Im Too Drunk To Taste This Chicken.',
        'Dear 8 Pounds 6 Ounces Newborn Infant Jesus, Dont Even Know A Word Yet.',
        'Tom Cruise, Use Your Witchcraft On Me To Get The Fire Off Me!',
    ]

    if message.content == 'gonk!':
        response = random.choice(star_wars_quotes)
        await message.channel.send(response)
    if message.content == 'race!':
        response = random.choice(talladega_nights_quotes)
        await message.channel.send(response)

client.run(TOKEN)
