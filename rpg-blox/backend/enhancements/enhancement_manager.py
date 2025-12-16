class EnhancementManager:
 def upgrade_weapon(self, player, weapon):
  level = weapon.get('level',0)
  if level >= 10:
   return False
  cost = (level+1)*100000
  if player.beli < cost:
   return False
  player.beli -= cost
  weapon['damage'] += 20*(level+1)
  weapon['level'] = level+1
  return True
