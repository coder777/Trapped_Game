from Command import Commands, Command, Panic, Climb, Sit, Take, Open
from Room_Object import RoomObjects, RoomObject, KeyRoomOne, Chair, VLrock, Door


class Room(object):
    def __init__(self,commands,room_objects,inventory):
        self.commands = commands
        self.room_objects = room_objects
        self.inventory = inventory
        self.room_message = """You have woken up in a dank room. 
        Any resemblance to the Austin Panic Room is purely coincidental.
        You see a Very Large Rock, and a rusty metal Chair. The large gothic Door is locked."""
        self.done = True
        self.death = False
        
    def enter_room(self):
        print self.room_message
        print "The room has: {0}".format(self.room_objects)
        print "The commands you can use are: {0}".format(self.commands)
        
    def procces_commands(self,command):
        self.commands.do_command(command.split(" ")[0].lower(),command.split(" ")[1:])
    
    def exit_room(self):
        return self.done
    
    def end_room(self):
        return False
    
    def death_occured(self):
        return self.death
    
class FirstRoom(Room):

    def __init__(self,inventory):
        room_objects = RoomObjects(KeyRoomOne(),VLrock(),Chair(),Door())
        commands = Commands(Take(inventory,room_objects),Panic(), Sit(), Climb(inventory,room_objects), Open(inventory, room_objects))
        super(FirstRoom, self).__init__(commands,room_objects,inventory)
        self.done = False
        
    def procces_commands(self, command):
        super(FirstRoom,self).procces_commands(command)

    
class EndRoom(Room):
    def __init__(self):
        self.commands = None
        self.room_objects = None
        self.room_message = "You've escaped! Woot!"
        
    def enter_room(self):
        print self.room_message
    
    def end_room(self):
        return True
