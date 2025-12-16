from raids.raid_data import RAIDS

class RaidManager:
    def __init__(self, player):
        self.player = player

    def start_raid(self, raid_name):
        raid = RAIDS.get(raid_name)
        if not raid:
            return False
        if self.player.sea < raid['sea']:
            return False
        return True

    def finish_raid(self, raid_name):
        raid = RAIDS[raid_name]
        self.player.fragments += raid['fragments']
        return raid['fragments']
