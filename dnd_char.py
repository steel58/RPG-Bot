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

    def __init__(self, name, _class="", _str=0, dex=0, con=0, _int=0, wis=0,
                 cha=0, skill_profs=[], prof_bonus=2, speed=30, level=1,
                 hit_die=6, hit_die_count=1):

        self.skill_prof = [0 for _ in range(18)]
        self.name = name
        self.stats = [_str, dex, con, _int, wis, cha]
        self.stat_bonus = [(i-10) // 2 for i in self.stats]
        self.initiative = self.stat_bonus[self.stat_index['dex']]
        self.saving_throws = [0 for _ in range(6)]
        self.skill_bonus = [0 for _ in range(18)]

        self.prof_bonus = prof_bonus
        self.class_ = _class
        self.speed = speed
        self.level = level
        self.hit_die = hit_die
        self.hit_die_max = hit_die_count
        self.hit_die_curent = hit_die_count

    def set_stat(self, stat_name, stat_value):
        index = self.stat_index[stat_name]
        self.stats[index] = stat_value
        self.stat_bonus[index] = (stat_value - 10) // 2
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
        else:
            return "This is not a valid skill or stat"


class DnDWeapon():
    def __init__(self, name, base_stat, damage_die,
                 damage_die_count=1, damage_type="Piercing"):
        self.name = name
        self.base_stat = base_stat
        self.damage_die = damage_die
        self.damage_die_count = damage_die_count
        self.damage_type = damage_type


if __name__ == "__main__":
    harper = DnDCharacter("Guelph", "Barbarian", 10, 13, 18, 9, 7, 17)

    print(len(harper.skill_prof))
