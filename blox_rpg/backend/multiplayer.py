rooms = {}

def join(room, user):
    if room not in rooms:
        rooms[room] = []
    if user not in rooms[room]:
        rooms[room].append(user)
    return rooms[room]
