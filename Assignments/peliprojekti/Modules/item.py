#Initiates the class Item
class Item:
    def __init__(self, name, uses):
        self.name = name
        self.uses = uses

class Damaging(Item):
    def __init__(self, name, dmg, uses):
        super().__init__(name, uses)
        self.dmg = dmg

class Healing(Item):
    def __init__(self, name, healing, uses):
        super().__init__(name, uses)
        self.healing = healing

class Money(Item):
    def __init__(self, amount, cleanliness):
        self.amount = amount
        self.cleanliness = cleanliness