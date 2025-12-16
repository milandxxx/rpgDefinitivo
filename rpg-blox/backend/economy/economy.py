class Economy:
    def __init__(self, player):
        self.player = player

    def add_beli(self, amount):
        self.player.beli += amount

    def spend_beli(self, amount):
        if self.player.beli >= amount:
            self.player.beli -= amount
            return True
        return False

    def add_fragments(self, amount):
        self.player.fragments += amount

    def spend_fragments(self, amount):
        if self.player.fragments >= amount:
            self.player.fragments -= amount
            return True
        return False
