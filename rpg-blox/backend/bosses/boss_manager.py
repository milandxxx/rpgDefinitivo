from bosses.boss_data import BOSSES

class BossManager:
    def __init__(self, player):
        self.player = player

    def defeat(self, boss):
        drops = BOSSES[boss]['drops']
        for k,v in drops.items():
            setattr(self.player, k, getattr(self.player, k, 0) + v)
        return drops
