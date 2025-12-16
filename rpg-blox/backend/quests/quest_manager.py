from quests.quest_data import QUESTS

class QuestManager:
    def __init__(self, player):
        self.player = player
        self.active_quest = None
        self.progress = 0

    def available_quests(self):
        return [
            q for q in QUESTS.get(self.player.sea, [])
            if q['level_min'] <= self.player.level <= q.get('level_max', 99999)
        ]

    def start_quest(self, quest_id):
        for q in self.available_quests():
            if q['id'] == quest_id:
                self.active_quest = q
                self.progress = 0
                return True
        return False

    def update_progress(self, target):
        if not self.active_quest:
            return None

        obj = self.active_quest['objective']
        if obj['type'] == 'kill' and obj['target'] == target:
            self.progress += 1
            if self.progress >= obj['amount']:
                self.complete_quest()
                return 'completed'

        return 'progress'

    def complete_quest(self):
        rewards = self.active_quest['rewards']
        self.player.add_xp(rewards.get('xp', 0))
        self.player.money += rewards.get('money', 0)
        self.active_quest = None
        self.progress = 0
