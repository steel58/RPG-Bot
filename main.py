import discord
import random
import time
import dnd_char as dd


file = open('key.txt', 'r')
MY_TOKEN = file.read()
file.close()

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

characters = []
character_names = []


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    text = 'No message was generated'
    contents = message.content

    if message.author == client.user:
        return

    if contents.startswith('!hello'):
        await message.channel.send('Hello!')

    if contents.startswith('!new_character'):
        text = new_character(message)
        await message.channel.send(text)

    if contents.startswith('!roll'):
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

        text = f'{person} rolled a total of: {sum(results)}'
        await message.channel.send(text)

    if contents.startswith('!stat_gen'):
        text = stat_gen(message)
        await message.channel.send(text)

    if contents.startswith('!str'):
        words = contents.split(' ')
        char_name = ' '.join(words[1:-1])
        stat = int(words[-1])
        char_index = character_names.index(char_name)
        characters[char_index].set_stat('str', stat)
        bonus = characters[char_index].stat_bonus[0]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

        await message.channel.send(f'{char_name} has strength {sign}{bonus}({stat})')

    if contents.startswith('!dex'):
        words = contents.split(' ')
        char_name = ' '.join(words[1:-1])
        stat = int(words[-1])
        char_index = character_names.index(char_name)
        characters[char_index].set_stat('dex', stat)
        bonus = characters[char_index].stat_bonus[1]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

        await message.channel.send(f'{char_name} has dexterity {sign}{bonus}({stat})')

    if contents.startswith('!con'):
        words = contents.split(' ')
        char_name = ' '.join(words[1:-1])
        stat = int(words[-1])
        char_index = character_names.index(char_name)
        characters[char_index].set_stat('con', stat)
        bonus = characters[char_index].stat_bonus[2]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

        await message.channel.send(f'{char_name} has constitution  {sign}{bonus}({stat})')

    if contents.startswith('!wis'):
        words = contents.split(' ')
        char_name = ' '.join(words[1:-1])
        stat = int(words[-1])
        char_index = character_names.index(char_name)
        characters[char_index].set_stat('wis', stat)
        bonus = characters[char_index].stat_bonus[4]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

        await message.channel.send(f'{char_name} has wisdom {sign}{bonus}({stat})')

    if contents.startswith('!int'):
        words = contents.split(' ')
        if words[1:-1]:
            char_name = ' '.join(words[1:-1])
        else:
            char_name = ' '.join(words[1:])

        char_index = character_names.index(char_name)
        if words[-1].isalpha():
            stat = characters[char_index].stats[3]
            bonus = characters[char_index].stat_bonus[3]

            if bonus < 0:
                sign = ''
            else:
                sign = '+'
        else:
            stat = int(words[-1])
            characters[char_index].set_stat('int', stat)
            bonus = characters[char_index].stat_bonus[3]
            if bonus < 0:
                sign = ''
            else:
                sign = '+'

        await message.channel.send(f'{char_name} has intelegence {sign}{bonus}({stat})')

    if contents.startswith('!cha'):
        words = contents.split(' ')
        char_name = ' '.join(words[1:-1])
        stat = int(words[-1])
        char_index = character_names.index(char_name)
        characters[char_index].set_stat('cha', stat)
        bonus = characters[char_index].stat_bonus[5]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

        await message.channel.send(f'{char_name} has charisma {sign}{bonus}({stat})')
#
#
#
#
#
#
#


def new_character(message):
    person = message.author
    chr_name = ' '.join(message.content.split(' ')[1:])

    if character_names.count(chr_name) == 0:
        character_names.append(chr_name)
        characters.append(dd.DnDCharacter(chr_name))
        text = f'{person.name} created a character named {chr_name}!'
    else:
        text = f'A character named {chr_name} already exists. If you wish to create a new character type "!kill {chr_name}" and then try again.'

    return text


def stat_gen(message):
    all_stats = []
    for _ in range(6):
        stat = []
        for j in range(4):
            stat.append(random.randint(1, 6))
        stat.sort()
        all_stats.append(sum(stat[1:]))

    return f'Stats are {all_stats}'


client.run(MY_TOKEN)
