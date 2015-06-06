class RoomObjects(object):
    def __init__(self,*args):
        self.room_objects = {arg.get_name().lower():arg for arg in args}

    def __str__(self, *args, **kwargs):
        return " ".join(self.room_objects)
    
    def find_object(self,tag_name):
        if tag_name not in self.room_objects:
            print "I don't see {0}".format(tag_name)
        else:
            return True
            
class RoomObject(object):
    def __init__(self, name, description, taken, climbable):
        self.name = name
        self.description = description
        self.taken = taken
        self.climbable = climbable
        
    def __str__(self, *args, **kwargs):
        return self.description

    def get_name(self):
        return self.name

    def can_be_taken(self):
        return self.taken

    def can_climb(self):
        return self.climbable

class KeyRoomOne(RoomObject):
    def __init__(self):
        super(KeyRoomOne,self).__init__("key_room_one","A bright shiny brass key.", True, False)
    
class VLrock(RoomObject):
    def __init__(self):
        super(VLrock,self).__init__("Very large rock","A very large rock as tall as you!", False, False)

class Chair(RoomObject):
    def __init__(self):
        super(Chair, self).__init__("chair", "A slightly rusty chair folding chair.", True, True)

class Door(RoomObject):
    def __init__(self):
        super(Door,self).__init__("Door", "A large gothic door", False, False)
