from quests.quest_data import QUESTS

class QuestManager:
    def __init__(self, player):
        self.player = player

    def get_available(self):
        return [
            q for q in QUESTS
            if self.player.sea >= q['sea'] and self.player.level >= q['min_lvl']
        ]

    def complete(self, quest):
        self.player.exp += quest['exp']
        self.player.beli += quest['beli']
        if 'fragments' in quest:
            self.player.fragments += quest['fragments']
