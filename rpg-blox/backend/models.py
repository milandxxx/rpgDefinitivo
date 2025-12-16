def xp_necesaria(nivel):
    if nivel < 1000:
        return nivel * 150
    elif nivel < 3000:
        return nivel * 250
    elif nivel < 5000:
        return nivel * 400
    else:
        return nivel * 600

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.money = 0
        self.sea = 1
        self.max_level = 7500

    def add_xp(self, amount):
        if self.level >= self.max_level:
            return

        self.xp += amount
        while self.xp >= xp_necesaria(self.level) and self.level < self.max_level:
            self.xp -= xp_necesaria(self.level)
            self.level += 1
