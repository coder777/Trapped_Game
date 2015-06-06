class RoomObjects(object):
    def __init__(self,*args):
        self.room_objects = {arg.get_name().lower():arg for arg in args}

    def __str__(self, *args, **kwargs):
        return " ".join(self.room_objects)
    
    def find_object(self,tag_name):
        if tag_name not in self.room_objects:
            print "I don't see {0}".format(tag_name)
            
class RoomObject(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self, *args, **kwargs):
        return self.description

    def get_name(self):
        return self.name
    
class KeyRoomOne(RoomObject):
    def __init__(self):
        super(KeyRoomOne,self).__init__("key_room_one","A bright shiny brass key.")
    
class VLrock(RoomObject):
    def __init__(self):
        super(VLrock,self).__init__("Very large rock","A very large rock as tall as you are which the key is on top of.")

class Chair(RoomObject):
    def __init__(self):
        super(Chair, self).__init__("chair", "A slightly rusty chair folding chair.")
