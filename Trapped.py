from sys import exit
from Room import FirstRoom, EndRoom

class Scene(object):

    def enter(self):
        print "Not ready yet"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
        

class Death(Scene):

    def enter(self):
        pass

class Rock(Scene):

    def enter(self):
        pass

class Party(Scene):

    def enter(self):
        pass

class Snakes(Scene):

    def enter(self):
        pass


class Map(object):
    def __init__(self, *args):
        if len(args) > 0:
            self.path = args
            self.current_room = -1
        else:
            return EndRoom()

    def next_scene(self):
        self.current_room = self.current_room+1
        if self.current_room == len(self.path):
            return EndRoom()
        else:
            return self.path[self.current_room]

#Start the game
a_map = Map(FirstRoom())
current_room = a_map.next_scene()
while not current_room.end_room():
    current_room.enter_room()
    while not current_room.exit_room():
        string_from_input = raw_input("What do you want do: " )
        current_room.procces_commands(string_from_input)
    current_room = a_map.next_scene()
current_room.enter_room()

#room = a_map.next_scene()
#a_game = Engine(a_map)
#a_game.play()
