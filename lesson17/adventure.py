# rooms = {
#     'hall': {'north': 'kitchen', 'east': 'bedroom', 'item': None},
#     'kitchen': {'south': 'hall', 'item': 'key'},
#     'bedroom': {'west': 'hall', 'item': 'treasure'}
# }

# current_room = 'hall'
# inventory = []

# print("Welcome to the game! Write commands like 'go north' or 'take key'.")

# while True:
#     print("\nYou are in", current_room)
#     if rooms[current_room]['item']:
#         print("You see:", rooms[current_room]['item'])

#     command = input("> ")

#     if command.startswith("go "):
#         direction = command.split()[1]
#         if direction in rooms[current_room]:
#             current_room = rooms[current_room][direction]
#         else:
#             print("You can't go there.")
    
#     elif command.startswith("take "):
#         item = command.split()[1]
#         if rooms[current_room].get('item') == item:
#             inventory.append(item)
#             rooms[current_room]['item'] = None
#             print(f"You took{item}.")
#         else:
#             print("This is not here.")
    
#     elif command == "inventory":
#         print("You have:", inventory)
    
#     elif command == "quit":
#         print("Exit the game.")
#         break

#     else:
#         print("I can't understand you.")

rooms = {
    'hall': {
        'north': 'kitchen', 
        'east': 'bedroom', 
        'item': None
    },
    'kitchen': {
        'south': 'hall', 
        'item': 'key'
    },
    'bedroom': {
        'west': 'hall', 
        'item': 'treasure'
        }
}

room = 'hall'
bag = []

print("Welcome to the game!")

while True:
    print("You are in", room)
    item = rooms[room]['item']
    if item:
        print("You see a", item)

    cmd = input("Write commands like 'go north' or 'take key'.\n>> ")

    if cmd.startswith("go "):
        dir = cmd.split()[1]
        if dir in rooms[room]:
            room = rooms[room][dir]
        else:
            print("You can't go there.")

    elif cmd.startswith("take "):
        thing = cmd.split()[1]
        if rooms[room]['item'] == thing:
            bag.append(thing)
            rooms[room]['item'] = None
            print("You took", thing)
        else:
            print("Nothing to take.")

    elif cmd == "inventory":
        print("Bag:", bag)

    elif cmd == "quit":
        print("Exit the game.")
        break

    else:
        print("Unknown command.")