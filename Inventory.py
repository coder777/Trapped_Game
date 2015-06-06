class Inventory(object):
    def __init__(self):
        self.inventory = {}
    
    def __str__(self, *args, **kwargs):
        #import pdb; pdb.set_trace()
        return "You have {0}".format(" ".join(list(self.inventory)))
    
    def add(self,room_object):
        if room_object.get_name() in self.inventory:
            self.inventory[room_object].add()
        else:
            self.inventory[room_object] = InventoryItem(room_object.get_name(),1)
  
    def remove(self,room_object):
        if room_object.get_name() in self.inventory:
            self.inventory[room_object].remove()
    
    def has(self,room_object):
        if room_object.get_name() in self.inventory:
            True
        else:
            False
                    
class InventoryItem(object):
    def __init__(self,name,amount=1):
        self.name = name
        self.amount = amount

    def add(self):
        self.amount = self.amount+1
    
    def remove(self):
        self.amount = self.amount-1
        if self.amount < 0:
            self.amount = 0