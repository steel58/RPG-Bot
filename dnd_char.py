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

    skill_prof = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            ]

    def __init__(self, name, _class, _str, dex, con, _int, wis, cha,
                 prof_bonus=2, ):
        self.name = name
        self.stats = [_str, dex, con, _int, wis, cha]
        self.stat_bonus = [(i-10) // 2 for i in self.stats]
        self.saving_throws = [0 for _ in range(6)]
        self.prof_bonus = prof_bonus
        self.skills = []

        for i in self.skill_base:
            base = self.stat_bonus[self.stat_index[i]]
            bonus = self.skill_prof[i] * prof_bonus

            self.skills.append(base+bonus)

        self.class_ = _class


harper = DnDCharacter("Guelph", "Barbarian", 10, 13, 18, 9, 7, 17)

print(len(harper.skill_prof))
