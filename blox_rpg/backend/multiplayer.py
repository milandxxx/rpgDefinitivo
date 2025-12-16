rooms = {}

def join_room(room, player):
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(player)
    return rooms[room]
