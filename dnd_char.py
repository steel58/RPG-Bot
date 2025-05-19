class DnDCharacter():
    stat_index = {
            "str": 0,
            "dex": 1,
            "con": 2,
            "int": 3,
            "wis": 4,
            "cha": 5,
            }

    skill_index = {
            "acrobatics": 0,
            "acro": 0,
            "animal handling": 1,
            "animal": 1,
            "anhan": 1,
            "arcana": 2,
            "arc": 2,
            "athletics": 3,
            "ath": 3,
            "deception": 4,
            "dec": 4,
            "history": 5,
            "his": 5,
            "insight": 6,
            "ins": 6,
            "intimidation": 7,
            "intim": 7,
            "investigation": 8,
            "inv": 8,
            "medicine": 9,
            "med": 9,
            "nature": 10,
            "nat": 10,
            "perception": 11,
            "perc": 11,
            "performance": 12,
            "perf": 12,
            "persuasion": 13,
            "pers": 13,
            "religion": 14,
            "rel": 14,
            "slight of hand": 15,
            "slight": 15,
            "soh": 15,
            "stealth": 16,
            "stl": 16,
            "survival": 17,
            "sur": 17,
            }

    skill_base = [
            "dex",
            "wis",
            "int",
            "str",
            "cha",
            "int",
            "wis",
            "cha",
            "int",
            "wis",
            "int",
            "wis",
            "cha",
            "cha",
            "int",
            "dex",
            "dex",
            "wis",
            ]

    def __init__(self, name="", _class="", _str=0, dex=0, con=0, _int=0, wis=0,
                 cha=0, skill_profs=[], prof_bonus=2, speed=30, level=1,
                 hit_die=6, hit_die_count=1, health=1):

        self.skill_prof = [0 for _ in range(18)]
        self.name = name
        self.stats = [_str, dex, con, _int, wis, cha]
        self.stat_bonus = [(i-10) // 2 for i in self.stats]
        self.initiative = self.stat_bonus[self.stat_index['dex']]
        self.pasive_perception = self.stat_bonus[self.stat_index['wis']] + prof_bonus + 10;
        self.saving_throws = [0 for _ in range(6)]
        self.skill_bonus = [0 for _ in range(18)]
        self.misc_profs = []
        self.prof_bonus = prof_bonus
        self.class_ = _class
        self.speed = speed
        self.level = level
        self.hit_die = hit_die
        self.hit_die_max = hit_die_count
        self.hit_die_curent = hit_die_count
        self.health = self.hit_die + self.stat_bonus[2]
        self.background = ""
        self.player_name = ""
        self.race = ""
        self.xp = 0
        self.personality = []
        self.ideals = []
        self.bonds = []
        self.flaws = []
        self.copper = 0
        self.silver = 0
        self.gold = 0
        self.electrum = 0
        self.platinum = 0
        self.spell_slots = [0 for _ in range(9)]
        self.spells_cantrip = []
        self.spells_lvl1 = []
        self.spells_lvl2 = []
        self.spells_lvl3 = []
        self.spells_lvl4 = []
        self.spells_lvl5 = []
        self.spells_lvl6 = []
        self.spells_lvl7 = []
        self.spells_lvl8 = []
        self.spells_lvl9 = []

    def set_stat(self, stat_name, stat_value):
        index = self.stat_index[stat_name]
        self.stats[index] = stat_value
        self.stat_bonus[index] = (stat_value - 10) // 2
        if stat_name == 'wis':
            self.pasive_perception = self.stat_bonus[self.stat_index['wis']] + self.prof_bonus + 10;

        self.update_skills(stat_name)

    def update_skills(self, base_stat):
        for (i, stat) in enumerate(self.skill_base):
            if stat == base_stat:
                stat_index = self.stat_index[stat]
                prof = self.prof_bonus * self.skill_prof[i]
                self.skill_bonus[i] = prof + self.stat_bonus[stat_index]

    def get_bonus(self, word):
        if word in self.stat_index:
            return self.stat_bonus[self.stat_index[word]]
        elif word.lower() in self.skill_index:
            return self.skill_bonus[self.skill_index[word]]
        elif word.lower() == 'prof' or word.lower() == 'proficiency':
            return self.prof_bonus
        else:
            return "This is not a valid skill or stat"

    def from_dict(self, _dict):
        for trait in _dict:
            setattr(self, trait, _dict[trait])
        return self

    copper_convert = {
            'c': 1
            's': 0.1
            'e': 0.02
            'g': 0.01
            'p': 0.001
            }

    silver_convert = {
            'c': 10
            's': 1
            'e': 0.2
            'g': 0.1
            'p': 0.01
            }

    electrum_convert = {
            'c': 50
            's': 5
            'e': 1
            'g': 0.5
            'p': 0.05
            }

    gold_convert = {
            'c': 100
            's': 10
            'e': 2
            'g': 1
            'p': 0.1
            }

    platinum_convert = {
            'c': 1000
            's': 100
            'e': 50
            'g': 10
            'p': 1
            }

    def currency_convert(count, start, finish):
        if start.lower()[0] == c:
            return copper_convert[finish.lower()[0]] * count
        elif start.lower()[0] == s:
            return silver_convert[finish.lower()[0]] * count
        elif start.lower()[0] == e:
            return electrum_convert[finish.lower()[0]] * count
        elif start.lower()[0] == g:
            return gold_convert[finish.lower()[0]] * count
        elif start.lower()[0] == p:
            return platinum_convert[finish.lower()[0]] * count
        else:
            return None
        


class DnDWeapon():
    def __init__(self, name, base_stat, damage_die,
                 damage_die_count=1, damage_type="Piercing"):
        self.name = name
        self.base_stat = base_stat
        self.damage_die = damage_die
        self.damage_die_count = damage_die_count
        self.damage_type = damage_type
