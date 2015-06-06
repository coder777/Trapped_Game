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
    
    def run(self, list_of_arguments):
        pass
    
class Panic(Command):
    def __init__(self):
        super(Panic,self).__init__("panic")
        
    def run(self, list_of_arguments):
        print "You run around in a circle, shouting into the void."


class Sit(Command):
    def __init__(self):
        super(Sit,self).__init__("sit")

    def run(self, list_of_arguments):
        print "You decide to sit & rest and think of your next move."

class Climb(Command):
    def __init__(self,inventory,object_in_room):
        super(Climb,self).__init__("climb")
        self.objects_in_room = object_in_room
        self.inventory = inventory

    def run(self,list_of_arguments):
        #import pdb; pdb.set_trace()
        if len(list_of_arguments) > 0:
            object_to_climb = list_of_arguments[0]
            
            if self.objects_in_room.find_object(object_to_climb):
                print "You climb {0}".format(object_to_climb)
                if 'chair' in object_to_climb:
                    print "You see a shiny key on top of the large rock."
               
                    
        else:
            print "I moved my fit up an empty space"
        print "You climbed. What do you have and what do want to do?"

