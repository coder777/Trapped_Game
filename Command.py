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


class Take(Command):
    def __init__(self,inventory,objects_in_room):
        super(Take,self).__init__("take")
        self.objects_in_room = objects_in_room
        self.inventory = inventory

    def run(self, list_of_arguments):
        if len(list_of_arguments) > 0:
            object_be_taken = list_of_arguments[0]
            if self.objects_in_room.find_object(object_be_taken):
                if self.objects_in_room.get_object(object_be_taken).can_be_taken():
                    print "You take {0}".format(object_be_taken)
                    self.inventory.add(self.objects_in_room.get_object(object_be_taken))
                    print "you know have in your inventory: {0}".format(self.inventory)
                else:
                    print "You can't take {0}.".format(object_be_taken)
            else:
                print "I can't find {0} to take.".format(object_be_taken)
        else:
            print "Not sure what you want take."

class Climb(Command):
    def __init__(self,inventory,object_in_room):
        super(Climb,self).__init__("climb")
        self.objects_in_room = object_in_room
        self.inventory = inventory

    def run(self,list_of_arguments):
        #import pdb; pdb.set_trace() <---to debug
        if len(list_of_arguments) > 0:
            object_to_climb = list_of_arguments[0]
            if self.objects_in_room.find_object(object_to_climb):
                if self.objects_in_room.get_object(object_to_climb).climbable:
                    print "You climb {0}".format(object_to_climb)
                    print "You see a shiny key on top of the large rock."
                    self.objects_in_room.get_object("key_room_one").taken = True
                    
        else:
            print "You can't climb {0}.".format(object_to_climb)

