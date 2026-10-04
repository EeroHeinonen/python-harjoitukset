#Importin methods from sibling modules
from .item import Item, Damaging, Healing
from .enemy import Enemy

#Initiates the room class
class Room:
    def __init__(self, name, items, enemies, neighbors, index):
        self.name = name
        self.items = []
        self.enemies = []
        self.neighbors = {}
        self.index = 0

#Creates the following objects of "Room" and adds them to the list "rooms"
livingRoom = Room("Living room", [], [], {}, 0)
street = Room("Street", [], [], {}, 1)
tampere = Room("Tampere", [], [], {}, 2)
oulu = Room("Oulu", [], [], {}, 3)
kemi = Room("Kemi", [], [], {}, 4)
haaparanta = Room("Haaparanta", [], [], {}, 5)
store = Room("Store", [], [], {}, 6)

rooms = [livingRoom, street, tampere, oulu, kemi, haaparanta, store]

hobo = Enemy("Homeless", 25, 5, street)

#Creates item objects and assigns them values ex. name, damage, uses
vase = Damaging("vase", 15, 1)
shovel = Damaging("shovel", 10, 10)
sandwich = Healing("sandwich", 15, 1)
#Adds the items to the room's itempool
livingRoom.items.extend([vase, sandwich])
street.items.append(shovel)
street.enemies.append(hobo)

#Assigns the rooms to have "neighbors", which allows player movememnt between rooms using directions
def assignNeighbors():
    livingRoom.neighbors.update({"up": street})
    street.neighbors.update({"down": livingRoom, "up": tampere})
    tampere.neighbors.update({"down": street, "up": oulu})