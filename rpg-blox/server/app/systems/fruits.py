import random

FRUITS = [
    {"name":"Flame","rarity":0.4},
    {"name":"Ice","rarity":0.25},
    {"name":"Light","rarity":0.15},
    {"name":"Dark","rarity":0.1},
    {"name":"Dragon","rarity":0.05},
    {"name":"Chrono","rarity":0.03},
    {"name":"Void","rarity":0.02}
]

def roll_fruit():
    r = random.random()
    total = 0
    for f in FRUITS:
        total += f["rarity"]
        if r <= total:
            return f["name"]
    return None
