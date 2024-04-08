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
            "Acrobatics": 0,
            "Animal Handling": 1,
            "Arcana": 2,
            "Athletics": 3,
            "Deception": 4,
            "History": 5,
            "Insight": 6,
            "Intimidation": 7,
            "Investigation": 8,
            "Medicine": 9,
            "Nature": 10,
            "Perception": 11,
            "Performance": 12,
            "Persuasion": 13,
            "Religion": 14,
            "Slight of Hand": 15,
            "Stealth": 16,
            "Survival": 17,
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

    def __init__(self, name, _class, _str, dex, con, _int, wis, cha,
                 skill_profs=[], prof_bonus=2, speed=30, level=1, hit_die=6,
                 hit_die_count=1):

        self.skill_prof = [0 for _ in range(18)]
        for i in skill_profs:
            self.skill_prof[self.skill_index[i]] = 1
        self.name = name
        self.stats = [_str, dex, con, _int, wis, cha]
        self.stat_bonus = [(i-10) // 2 for i in self.stats]
        self.initiative = self.stat_bonus[self.stat_index['dex']]
        self.saving_throws = [0 for _ in range(6)]
        self.prof_bonus = prof_bonus
        self.skills = []

        for i, s in enumerate(self.skill_base):
            base = self.stat_bonus[self.stat_index[s]]
            bonus = self.skill_prof[i] * prof_bonus

            self.skills.append(base+bonus)

        self.class_ = _class
        self.speed = speed
        self.level = level
        self.hit_die = hit_die
        self.hit_die_max = hit_die_count
        self.hit_die_curent = hit_die_count


class DnDWeapon():
    def __init__(self, name, base_stat, damage_die,
                 damage_die_count=1, damage_type="Piercing"):
        self.name = name
        self.base_stat = base_stat
        self.damage_die = damage_die
        self.damage_die_count = damage_die_count
        self.damgae_type = damage_type


harper = DnDCharacter("Guelph", "Barbarian", 10, 13, 18, 9, 7, 17)

print(len(harper.skill_prof))
