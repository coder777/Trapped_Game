from Room import EndRoom

class Map(object):
    def __init__(self, *args):
        if len(args) > 0:
            self.path = args
            self.current_room = -1
        else:
            return EndRoom()

    def next_scene(self):
        self.current_room = self.current_room+1
        if self.current_room >= len(self.path):
            return EndRoom()
        else:
            return self.path[self.current_room]
        
    def move_back_to_start(self):
        self.current_room = -1
        self.path[0].done = False
        self.path[0].death = False
        
    def move_to_end(self):
        self.current_room = len(self.path)