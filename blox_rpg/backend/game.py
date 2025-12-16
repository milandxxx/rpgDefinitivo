import random

FRUITS = {
    'Flame': 25,
    'Ice': 15,
    'Dark': 20,
    'Light': 30
}

def random_fruit():
    return random.choice(list(FRUITS.keys()))

def fruit_damage(fruit):
    return FRUITS.get(fruit, 5)
