import random
from models import Enemy

FRUITS = {
    'Flame': {'damage': 30},
    'Ice': {'freeze': True},
    'Light': {'speed': 2},
    'Dark': {'lifesteal': 10}
}

def create_enemy():
    return Enemy('Bandit', 80, 8)

def use_skill(fruit):
    return FRUITS.get(fruit, {})
