class Player:
    def __init__(self, level):
        self.level = level
        self.hp = 100 + level * 12
        self.stamina = 100 + level * 8
        self.atk = 10 + level * 2
        self.defense = 5 + level * 1.5
