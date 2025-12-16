import json, os

SAVE_DIR = 'backend/saves'

def save_player(player):
    path = f'{SAVE_DIR}/{player.name}.json'
    with open(path, 'w') as f:
        json.dump(player.__dict__, f)

def load_player(name):
    path = f'{SAVE_DIR}/{name}.json'
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)
