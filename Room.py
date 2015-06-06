class Room(object):
    def __init__(self,commands,room_objects):
        self.commands = commands
        self.room_objects = room_objects
        self.room_message = ""
    
    def enter_room(self):
        print self.room_message
        print "Room has: {0}".format(self.room_objects)
        print "Commands: {0}".format(self.commands)
        
    def procces_commands(self,command):
        self.commands(command.split(" ")[0].lowercase(),command.split(" ")[1:])
    