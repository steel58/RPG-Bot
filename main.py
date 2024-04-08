import discord
import random
import time


file = open('key.txt', 'r')
MY_TOKEN = file.read()
file.close()

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!new_character'):
        person = message.author
        chr_name = message.content.split(' ')[1]
        await message.channel.send(f'{person.name} created a character named {chr_name}!')

    if message.content.startswith('!roll'):
        person = message.author
        words = message.content.lower().split(' ')

        multiplicity = int(words[1].split('d')[0])
        die = int(words[1].split('d')[1])
        d_max = max(die, 1)
        d_min = min(die, 1)

        results = []

        await message.channel.send(f'Rolling {words[1]}')

        for i in range(multiplicity):
            roll = random.randint(d_min, d_max)
            results.append(roll)
            await message.channel.send(f'{roll}')
            time.sleep(2.4)

        if message.content.count('drop') == 1:
            drop = int(message.content.split(' ')[-1])
            results.sort()
            if drop < 0:
                results.reverse()

            results = results[abs(drop):]
            print(results)

        await message.channel.send(f'Total: {sum(results)}')

    if message.content.startswith('!stat_gen'):
        all_stats = []
        for _ in range(6):
            stat = []
            for j in range(4):
                stat.append(random.randint(1, 6))
            stat.sort()
            all_stats.append(sum(stat[1:]))

        await message.channel.send(f'Stats are {all_stats}')


client.run(MY_TOKEN)
=======
>>>>>>> 25fb4bac4adc152b8e7d787a11b49c5352dbeb28
