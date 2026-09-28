class Room:
    def __init__(self, name, items, enemies):
        self.name = name
        self.items = []
        self.enemies = []

livingRoom = Room("Living room", [], [])
street = Room("Street", [], [])
tampere = Room("Tampere", [], [])
oulu = Room("Oulu", [], [])
kemi = Room("Kemi", [], [])
haaparanta = Room("Haaparanta", [], [])
store = Room("Kauppa", [], [])

rooms = [livingRoom, street, tampere, oulu, kemi, haaparanta, store]