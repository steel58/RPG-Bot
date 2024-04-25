import json
from dnd_char import DnDCharacter

FILE_PATH = "characters.json"


def load():
    raw_data = []
    try:
        file = open('characters.json', 'r')
        raw_data = file.readlines()
    except:
        file.close()
        return (None, None)

    names = json.loads(raw_data[0].strip())
    char_dicts = json.loads(raw_data[1].strip())
    characters = [DnDCharacter().from_dict(i) for i in char_dicts]
    return (names, characters)


def save(names, characters):
    names_json = json.dumps(names)
    char_dict = [i.__dict__ for i in characters]
    characters_json = json.dumps(char_dict)

    try:
        file = open('characters.json', 'w')
        file.writelines(names_json + '\n')
        file.writelines(characters_json + '\n')
        file.close()
        return 0
    except:
        return -1
