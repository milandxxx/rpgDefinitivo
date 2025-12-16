from items.item_data import ITEMS

class ItemManager:
    def __init__(self, player):
        self.player = player

    def equip(self, item_name):
        item = ITEMS.get(item_name)
        if not item:
            return False

        for stat, value in item.items():
            setattr(self.player, stat, getattr(self.player, stat, 0) + value)
        return True
