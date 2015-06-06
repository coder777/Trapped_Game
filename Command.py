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
    

