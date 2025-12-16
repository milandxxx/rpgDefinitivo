class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 50
        self.attack = 5

    def move_towards(self, px, py):
        if self.x < px: self.x += 1
        if self.x > px: self.x -= 1
        if self.y < py: self.y += 1
        if self.y > py: self.y -= 1
