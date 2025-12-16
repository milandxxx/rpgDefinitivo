from race_upgrades.race_upgrade_data import RACE_UPGRADES

class RaceUpgradeManager:
    def __init__(self, player):
        self.player = player

    def upgrade(self):
        race = self.player.race
        current = self.player.race_version

        if current >= 4:
            return False

        next_version = current + 1
        cost = RACE_UPGRADES[race][next_version]['fragments']

        if self.player.fragments >= cost:
            self.player.fragments -= cost
            self.player.race_version = next_version
            return True
        return False
