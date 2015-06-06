class Commands(object):
    def __init__(self,*args):
        self.commands = {arg.get_tag().lowercase():arg for arg in args}

    def do_command(self,tag_name,args=""):
        if tag_name in self.commands:
            self.commands[tag_name].run(args)
        else:
            print "I don't understand {0}".format(tag_name)
            
class Command(object):
    def __init__(self, tag):
        self.tag = ""

    def get_tag(self):
        return self.tag
    
    def run(self, args=""):
        pass
    

