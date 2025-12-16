import random
from fruits.fruit_data import FRUITS, RARITY_CHANCES

SEA_LUCK = {
    1: 1.0,
    2: 1.5,
    3: 2.0,
    4: 3.0,
    5: 4.0
}

class FruitManager:
    def __init__(self, player):
        self.player = player

    def roll_fruit(self):
        luck = SEA_LUCK.get(self.player.sea, 1.0)

        pool = []
        for rarity, chance in RARITY_CHANCES.items():
            pool.extend([rarity] * int(chance * luck))

        chosen_rarity = random.choice(pool)

        fruits = [
            name for name, data in FRUITS.items()
            if data['rarity'] == chosen_rarity
        ]

        return random.choice(fruits)

    def eat_fruit(self, fruit):
        if fruit not in FRUITS:
            return False
        self.player.fruit = fruit
        return True
