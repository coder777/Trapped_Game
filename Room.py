from Command import Commands, Command
from Room_Object import RoomObjects, RoomObject

class Room(object):
    def __init__(self,commands,room_objects):
        self.commands = commands
        self.room_objects = room_objects
        self.room_message = ""
        self.done = True
        self.death = False
        
    def enter_room(self):
        print self.room_message
        print "Room has: {0}".format(self.room_objects)
        print "Commands: {0}".format(self.commands)
        
    def procces_commands(self,command):
        self.commands.do_command(command.split(" ")[0].lower(),command.split(" ")[1:])
    
    def exit_room(self):
        return self.done
    
    def end_room(self):
        return False
    
    def death_occured(self):
        return self.death
    
class FirstRoom(Room):
    def __init__(self):
        commands = Commands(Command("take"),Command("panic"))
        room_objects = RoomObjects(RoomObject("key","a shiny key"),RoomObject("door","a thick metal panel with a handle"))
        super(FirstRoom, self).__init__(commands,room_objects)
        self.done = False
        
    def procces_commands(self, command):
        self.done = True
        super(FirstRoom,self).procces_commands(command)

    
class EndRoom(Room):
    def __init__(self):
        self.commands = None
        self.room_objects = None
        self.room_message = "Game Over"
        
    def enter_room(self):
        print self.room_message
    
    def end_room(self):
        return True