from haki.haki_data import HAKI

class HakiManager:
 def train(self, player, haki):
  if haki not in HAKI:
   return False
  player.haki = haki
  return True
