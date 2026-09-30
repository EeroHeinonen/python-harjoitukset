
#Initiates the room class
class Room:
    def __init__(self, name, items, enemies, neighbors, index):
        self.name = name
        self.items = []
        self.enemies = []
        self.neighbors = {}
        self.index = 0

#Creates the following objects of "Room"
livingRoom = Room("Living room", [], [], {}, 0)
street = Room("Street", [], [], {}, 1)
tampere = Room("Tampere", [], [], {}, 2)
oulu = Room("Oulu", [], [], {}, 3)
kemi = Room("Kemi", [], [], {}, 4)
haaparanta = Room("Haaparanta", [], [], {}, 5)
store = Room("Kauppa", [], [], {}, 6)

#Assigns the rooms to have "neighbors", which allows player movememnt between rooms
def assignNeighbors():
    livingRoom.neighbors.update({"up": street})
    street.neighbors.update({"down": livingRoom, "up": tampere})
    tampere.neighbors.update({"down": street, "up": oulu})