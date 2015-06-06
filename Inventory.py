class Inventory(object):
    def __init__(self):
        self.inventory = {}
    
    def __str__(self, *args, **kwargs):
        return "{0}".format(" ".join(list(self.inventory)))
    
    def add(self,room_object):
        if room_object.get_name() in self.inventory:
            self.inventory[room_object.get_name()].add()
        else:
            self.inventory[room_object.get_name()] = InventoryItem(room_object,1)
  
    def remove(self,room_object):
        if room_object.get_name() in self.inventory:
            self.inventory[room_object.get_name()].remove()
    
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