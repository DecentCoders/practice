rooms = {
    'Hall': {'east': 'Kitchen', 'south': 'Garden'},
    'Kitchen': {'west': 'Hall'},
    'Garden': {'north': 'Hall'}
}

current_room = 'Hall'

while True:
    print(f"\nYou are in the {current_room}.")
    print("Exits:", ", ".join(rooms[current_room].keys()))
    
    move = input("Where do you want to go? (or 'quit'): ").lower()
    
    if move == 'quit':
        break
    
    if move in rooms[current_room]:
        current_room = rooms[current_room][move]
    else:
        print("You can't go that way!")