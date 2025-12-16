import random, time
from fruits.fruit_data import FRUITS
from fruit_shop.fruit_prices import PRICES

ROTATION_TIME = 60 * 30  # 30 minutos

class FruitShop:
    def __init__(self):
        self.last_rotation = time.time()
        self.stock = self.roll_stock()

    def roll_stock(self):
        return random.sample(list(FRUITS.keys()), 5)

    def update(self):
        if time.time() - self.last_rotation >= ROTATION_TIME:
            self.stock = self.roll_stock()
            self.last_rotation = time.time()

    def get_stock(self):
        self.update()
        result = []
        for fruit in self.stock:
            rarity = FRUITS[fruit]['rarity']
            result.append({
                'name': fruit,
                'rarity': rarity,
                'price': PRICES[rarity]
            })
        return result

    def buy(self, player, fruit_name):
        if fruit_name not in self.stock:
            return False, 'No disponible'
        rarity = FRUITS[fruit_name]['rarity']
        price = PRICES[rarity]
        if player.beli < price:
            return False, 'Beli insuficiente'
        player.beli -= price
        player.fruit = fruit_name
        return True, fruit_name
