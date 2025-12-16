from events.event_data import EVENTS

class EventManager:
 def trigger(self, player, event):
  e = EVENTS.get(event)
  if not e or player.sea < e['sea']:
   return False
  player.fragments += e['reward']
  return True
