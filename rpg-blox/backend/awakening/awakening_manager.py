from awakening.awakening_data import AWAKENINGS

class AwakeningManager:
 def awaken(self, player):
  fruit = player.fruit
  if fruit not in AWAKENINGS:
   return False
  cost = AWAKENINGS[fruit]['cost']
  if player.fragments < cost:
   return False
  player.fragments -= cost
  player.awakened = True
  return True
