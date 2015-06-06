from Room import FirstRoom
from Map import Map
from Inventory import Inventory

#Start the game
inventory = Inventory()
a_map = Map(FirstRoom(inventory))
current_room = a_map.next_scene()
while not current_room.end_room():
    current_room.enter_room()
    while not current_room.exit_room():
        if current_room.death_occured():
            print "You have died"
            a_map.move_back_to_start()
            break
        string_from_input = raw_input("What do you want do: " )
        current_room.procces_commands(string_from_input)
    current_room = a_map.next_scene()
current_room.enter_room()
