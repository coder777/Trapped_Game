class Commands(object):
    def __init__(self,*args):
        self.commands = {arg.get_name().lower():arg for arg in args}

    def __str__(self, *args, **kwargs):
        return " ".join(self.commands)
    
    def do_command(self,tag_name,args=""):
        if tag_name in self.commands:
            self.commands[tag_name].run(args)
        else:
            print "I don't understand {0}".format(tag_name)
            
class Command(object):
    def __init__(self, name):
        self.name = name

    def __str__(self, *args, **kwargs):
        return self.name
    
    def get_name(self):
        return self.name
    
    def run(self, *args):
        pass
    
class Panic(Command):
    def __init__(self):
        super(Panic,self).__init__("panic")
        
    def run(self, *args):
        print "You run around in a circle, shouting into the void."


class Sit(Command):
   def __init__(self):
	super(Sit,self).__init__("sit")

   def run(self, *args):
	print "You decide to sit & rest and think of your next move."

class Climb(Command):
    def __init__(self,inventory,object_in_room):
        super(Climb,self).__init__("climb")
        self.objects_in_room = object_in_room
        self.inventory = inventory
        
    def run(self,*args):
        if len(args) > 0:
            object_to_climb = args[0]
            if object_to_climb in self.objects_in_room:
                print "You climb {0}".format(object_to_climb)
        else:
            print "I moved my fit up an empty space"
        print "You climbed. What do you have and what do want to do?"
>>>>>>> b07c04f6f08b3ebe74888d56c64c79006618707c
