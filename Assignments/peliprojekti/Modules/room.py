class Room:
    def __init__(self, name, items, enemies, neighbors):
        self.name = name
        self.items = []
        self.enemies = []
        self.neighbors = []

livingRoom = Room("Living room", [], [], [])
street = Room("Street", [], [], [])
tampere = Room("Tampere", [], [], [])
oulu = Room("Oulu", [], [], [])
kemi = Room("Kemi", [], [], [])
haaparanta = Room("Haaparanta", [], [], [])
store = Room("Kauppa", [], [], [])

livingRoom.neighbors = [street]


# def assignNeighbors():
#     livingRoom.neighbors.extend(livingRoom)
#     street.neighbors.extend(livingRoom, tampere)