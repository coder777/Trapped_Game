class Room(object):
    def __init__(self,commands):
        self.commands = commands
        self.room_message = ""
    
    def enter_room(self):
        print self.room_message
        print "Commands: {0}".format(list(self.commands))
        
    def procces_commands(self,command):
        self.commands(command.split(" ")[0].lowercase(),command.split(" ")[1:])
    