from Room import FirstRoom
from Map import Map


#Start the game
a_map = Map(FirstRoom())
current_room = a_map.next_scene()
while not current_room.end_room():
    current_room.enter_room()
    while not current_room.exit_room():
        if current_room.death_occured():
            print "You have died"
            break
        string_from_input = raw_input("What do you want do: " )
        current_room.procces_commands(string_from_input)
    current_room = a_map.next_scene()
current_room.enter_room()
