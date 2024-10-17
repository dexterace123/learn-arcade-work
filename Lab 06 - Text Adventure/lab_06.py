class Room:
    """ Hold all attributes that describe a room"""
    def __init__(self, description, north, east, south, west):
        """ Set up the room attributes"""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    # Set up rooms
    room_list = []
    room = Room("You are in a large bedroom.\nThere is a passage to the north and to the east.\n", 3, 1, None, None)
    room_list.append(room)
    room = Room("You are in the southern part of a hallway.\nThe hallway continues north and there is passages to the west and to the east.\n", 4, 2, None, 0)
    room_list.append(room)
    room = Room("You are in the dining room.\nThere is a passage to the north and to the west.\n", 5, None, None, 1)
    room_list.append(room)
    room = Room("You are in a bedroom.\nThere is a passage to the south and to the east.\n", None, 4, 0, None)
    room_list.append(room)
    room = Room("You are in the northern part of a hallway.\nThere is a passage to the north, to the east, and to the west.\n", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("You are in a kitchen.\nThere is a passage to the west and to the south.\n", None, None, 2, 4)
    room_list.append(room)
    room = Room("You are on a balcony.\nThere is a passage to the south.\n", None, None, 4, None)
    room_list.append(room)

    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        prompt = input("What do you want to do: ")
        prompt = prompt.lower()
        if prompt == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif prompt == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif prompt == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif prompt == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif prompt == "q":
            done = True

        else:
            print("Sorry I didn't understand that.")
main()
