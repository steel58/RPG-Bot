import discord
from discord.ext import commands
import random
import time
import dnd_char as dd


file = open('key.txt', 'r')
MY_TOKEN = file.read()
file.close()

intents = discord.Intents.all()

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

characters = []
character_names = []
all_nicknames = dict()


def get_character_index(name):
    if name in character_names:
        true_name = name
    elif name in all_nicknames:
        true_name = all_nicknames[name]
    else:
        return

    return (true_name, character_names.index(true_name))


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@bot.command(name='hello')
async def hello(ctx):
    print("help me!")
    await ctx.send('Hello!')


@bot.command(name='kill')
async def kill_character(ctx):
    message = ctx.message
    words = message.content.split(' ')
    chr_name = ' '.join(words[1:])
    index = character_names.index(chr_name)
    characters.pop(index)
    character_names.pop(index)

    await ctx.send(f'{chr_name} was removed and can no longer be accessed')


@bot.command(name='nick')
async def nick(ctx):
    message = ctx.message
    halfs = message.content.split('-')
    first_words = halfs[0].split(' ')
    real_name = ' '.join(first_words[1:]).strip()
    nickname = halfs[1].strip()
    tags = []
    if len(halfs) > 2:
        tags = [i.strip() for i in halfs[2:]]

    if nickname in all_nicknames and 'f' not in tags and 'r' not in tags:
        await ctx.send(f'Nickname {nickname} already exists, add -f to overwrite this name')
    elif real_name not in character_names:
        await ctx.send(f'A character named \"{real_name}\" does not exist')
    elif 'r' in tags:
        all_nicknames.pop(nickname)
        await ctx.send(f'Nickname {nickname} was removed')
    else:
        all_nicknames[nickname] = real_name
        await ctx.send(f'{real_name} now has nickname {nickname}')


@bot.command(name='new_character')
async def new_character(ctx):
    message = ctx.message
    person = message.author
    chr_name = ' '.join(message.content.split(' ')[1:])

    if character_names.count(chr_name) == 0:
        character_names.append(chr_name)
        print(character_names)
        characters.append(dd.DnDCharacter(chr_name))
        text = f'{person.name} created a character named {chr_name}!'
    else:
        text = f'A character named {chr_name} already exists. If you wish to create a new character type "!kill {chr_name}" and then try again.'

    await ctx.send(text)


@bot.command(name='roll')
async def roll_switch(ctx):
    message = ctx.message
    words = message.content.lower().split(' ')

    if len(words) == 2:
        await roll(ctx)
    elif len(words) > 2:
        await trait_roll(ctx)
    else:
        await ctx.send("Your command was invalid, too few words.")


async def trait_roll(ctx):
    message = ctx.message
    person = message.author
    words = message.content.lower().split(' ')

    multiplicity = int(words[1].split('d')[0])
    die = int(words[1].split('d')[1])
    d_max = max(die, 1)
    d_min = min(die, 1)

    stat_used = words[-1]
    char_name = ' '.join(words[2:-1])

    char_name, index = get_character_index(char_name)
    character = characters[index]

    bonus = character.get_bonus(stat_used)

    if type(bonus) is str:
        await ctx.send(bonus)
        return

    results = []

    if bonus < 0:
        sign = ''
    else:
        sign = '+'

    await ctx.send(f'Rolling {words[1]} {sign} {bonus}')

    for i in range(multiplicity):
        roll = random.randint(d_min, d_max)
        results.append(roll + bonus)
        await ctx.send(f'{roll} {sign}{bonus}')
        time.sleep(2.4)

    text = f'{person} rolled a total of: {sum(results)}'
    await ctx.send(text)


async def roll(ctx):
    message = ctx.message
    person = message.author
    words = message.content.lower().split(' ')

    multiplicity = int(words[1].split('d')[0])
    die = int(words[1].split('d')[1])
    d_max = max(die, 1)
    d_min = min(die, 1)

    results = []

    await ctx.send(f'Rolling {words[1]}')

    for i in range(multiplicity):
        roll = random.randint(d_min, d_max)
        results.append(roll)
        await ctx.send(f'{roll}')
        time.sleep(2.4)

    if message.content.count('drop') == 1:
        drop = int(message.content.split(' ')[-1])
        results.sort()
        if drop < 0:
            results.reverse()

        results = results[abs(drop):]

    text = f'{person} rolled a total of: {sum(results)}'
    await ctx.send(text)


@bot.command(name='stat_gen')
async def stat_gen(ctx):
    all_stats = []
    for _ in range(6):
        stat = []
        for j in range(4):
            stat.append(random.randint(1, 6))
        stat.sort()
        all_stats.append(sum(stat[1:]))

    await ctx.send(f'Stats are {all_stats}')


@bot.command(name='str')
async def strength(ctx):
    message = ctx.message
    contents = message.content
    words = contents.split(' ')
    if words[1:-1]:
        char_name = ' '.join(words[1:-1])
    else:
        char_name = ' '.join(words[1:])

    char_name, char_index = get_character_index(char_name)
    if words[-1].isalpha():
        stat = characters[char_index].stats[0]
        bonus = characters[char_index].stat_bonus[0]

        if bonus < 0:
            sign = ''
        else:
            sign = '+'
    else:
        stat = int(words[-1])
        characters[char_index].set_stat('str', stat)
        bonus = characters[char_index].stat_bonus[0]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

    await ctx.send(f'{char_name} has strength {sign}{bonus}({stat})')


@bot.command(name='dex')
async def dexterity(ctx):
    message = ctx.message
    contents = message.content
    words = contents.split(' ')
    if words[1:-1]:
        char_name = ' '.join(words[1:-1])
    else:
        char_name = ' '.join(words[1:])

    char_name, char_index = get_character_index(char_name)
    if words[-1].isalpha():
        stat = characters[char_index].stats[1]
        bonus = characters[char_index].stat_bonus[1]

        if bonus < 0:
            sign = ''
        else:
            sign = '+'
    else:
        stat = int(words[-1])
        characters[char_index].set_stat('dex', stat)
        bonus = characters[char_index].stat_bonus[1]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

    await ctx.send(f'{char_name} has dexterity {sign}{bonus}({stat})')


@bot.command(name='con')
async def consitution(ctx):
    message = ctx.message
    contents = message.content
    words = contents.split(' ')
    if words[1:-1]:
        char_name = ' '.join(words[1:-1])
    else:
        char_name = ' '.join(words[1:])

    char_name, char_index = get_character_index(char_name)
    if words[-1].isalpha():
        stat = characters[char_index].stats[2]
        bonus = characters[char_index].stat_bonus[2]

        if bonus < 0:
            sign = ''
        else:
            sign = '+'
    else:
        stat = int(words[-1])
        characters[char_index].set_stat('con', stat)
        bonus = characters[char_index].stat_bonus[2]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

    await ctx.send(f'{char_name} has consitution {sign}{bonus}({stat})')


@bot.command(name='int')
async def intelegence(ctx):
    message = ctx.message
    contents = message.content
    words = contents.split(' ')
    if words[1:-1]:
        char_name = ' '.join(words[1:-1])
    else:
        char_name = ' '.join(words[1:])

    char_name, char_index = get_character_index(char_name)
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

    await ctx.send(f'{char_name} has intelegence {sign}{bonus}({stat})')


@bot.command(name='wis')
async def wisdom(ctx):
    message = ctx.message
    contents = message.content
    words = contents.split(' ')
    if words[1:-1]:
        char_name = ' '.join(words[1:-1])
    else:
        char_name = ' '.join(words[1:])

    char_name, char_index = get_character_index(char_name)
    if words[-1].isalpha():
        stat = characters[char_index].stats[4]
        bonus = characters[char_index].stat_bonus[4]

        if bonus < 0:
            sign = ''
        else:
            sign = '+'
    else:
        stat = int(words[-1])
        characters[char_index].set_stat('wis', stat)
        bonus = characters[char_index].stat_bonus[4]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

    await ctx.send(f'{char_name} has wisdom {sign}{bonus}({stat})')


@bot.command(name='cha')
async def charisma(ctx):
    message = ctx.message
    contents = message.content
    words = contents.split(' ')
    if words[1:-1]:
        char_name = ' '.join(words[1:-1])
    else:
        char_name = ' '.join(words[1:])

    char_name, char_index = get_character_index(char_name)
    if words[-1].isalpha():
        stat = characters[char_index].stats[5]
        bonus = characters[char_index].stat_bonus[5]

        if bonus < 0:
            sign = ''
        else:
            sign = '+'
    else:
        stat = int(words[-1])
        characters[char_index].set_stat('cha', stat)
        bonus = characters[char_index].stat_bonus[5]
        if bonus < 0:
            sign = ''
        else:
            sign = '+'

    await ctx.send(f'{char_name} has charisma {sign}{bonus}({stat})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

bot.run(MY_TOKEN)
