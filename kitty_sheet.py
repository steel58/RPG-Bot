class KittySheet():
    def __init__(self, name):
        self.name = name
        self.cute = 1
        self.fierce = 1
        self.cunning = 1
        self.owie_limit = 2
        self.owies = 0
        self.treats = 2
        self.injuries = 0

    def hurt_kitty(self, damage):
        self.owies += damage
        if self.owie_limit < self.owies:
            self.owies = self.owie_limit
            self.injuries += 1

    def set_cute(self, stat):
        self.cute = stat

    def set_fierce(self, stat):
        self.fierce = stat

    def set_cunning(self, stat):
        self.cunning = stat
