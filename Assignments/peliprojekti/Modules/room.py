#Importin methods from sibling modules
from .item import Item, Damaging, Healing, Money
from .enemy import Enemy

#Initiates the room class
class Room:
    def __init__(self, name, items, enemies, neighbors):
        self.name = name
        self.items = []
        self.enemies = []
        self.neighbors = {}

#Create the following objects of "Room" and add them to the list "rooms"
livingRoom = Room("Living room", [], [], {})
street = Room("Street", [], [], {})
gutter = Room("Gutter", [], [], {})
tampere = Room("Tampere", [], [], {})
seinäjoki = Room("Seinäjoki", [], [], {})
kokkola = Room("Kokkola", [], [], {})
kalajoki = Room("Kalajoki", [], [], {}) 
jyväskylä = Room("Jyväskylä", [], [], {})
kuopio = Room("Kuopio", [], [], {})
kajaani = Room("Kajaani", [], [], {})
suomussalmi = Room("Suomussalmi", [], [], {})
oulu = Room("Oulu", [], [], {})
pudasjärvi = Room("Pudasjärvi", [], [], {})
ranua = Room("Ranua", [], [], {})
taivalkoski = Room("Taivalkoski", [], [], {})
kemi = Room("Kemi", [], [], {})
haaparanta = Room("Haaparanta", [], [], {})
store = Room("Store", [], [], {})

rooms = [livingRoom, street, gutter, tampere, seinäjoki, kokkola, kalajoki, jyväskylä, kuopio, kajaani, suomussalmi, oulu, pudasjärvi, ranua, taivalkoski, kemi, haaparanta, store]

#Create item objects and assigns them values aka. name, damage/healing, uses
vase = Damaging("vase", 15, 1)
shovel = Damaging("shovel", 10, 10)
sandwich = Healing("sandwich", 15, 1)
salmiakki = Healing("salmiakki", 10000000, 1)

#Create enemy objects
hobo = Enemy("Homeless", 25, 5, gutter, Money(5))
protester = Enemy("Protester", 30, 7.5, tampere, sandwich)
hobo2 = Enemy("Homeless", 25, 5, seinäjoki, Money(0))

#Add the items and enemies to the room itempools
livingRoom.items.extend([vase, sandwich])
street.items.append(shovel)
gutter.enemies.append(hobo)
tampere.enemies.append(protester)
seinäjoki.enemies.append(hobo2)

#Function to assign the rooms to have "neighbors", which allows player movememnt between rooms using directions
def assignNeighbors():
    livingRoom.neighbors.update({"up": street})
    street.neighbors.update({"down": livingRoom, "left": gutter, "up": tampere})
    gutter.neighbors.update({"right": street})
    tampere.neighbors.update({"down": street, "right": jyväskylä, "left": seinäjoki})
    seinäjoki.neighbors.update({"right": tampere, "up": kokkola})
    kokkola.neighbors.update({"down": seinäjoki, "up": kalajoki})
    kalajoki.neighbors.update({"down": kokkola, "up": oulu, "right": kajaani})
    jyväskylä.neighbors.update({"left": tampere, "right": kuopio})
    kuopio.neighbors.update({"left": jyväskylä, "up": kajaani})
    kajaani.neighbors.update({"down": kuopio, "up": suomussalmi, "left": kalajoki})
    suomussalmi.neighbors.update({"down": kajaani, "up": taivalkoski})
    taivalkoski.neighbors.update({"down": suomussalmi, "left": pudasjärvi})
    oulu.neighbors.update({"down": kalajoki, "up": kemi, "right": pudasjärvi})
    pudasjärvi.neighbors.update({"left": oulu, "right": taivalkoski, "up": ranua})
    ranua.neighbors.update({"left": kemi, "down": pudasjärvi})
    kemi.neighbors.update({"right": ranua, "down": oulu, "left": haaparanta})
    haaparanta.neighbors.update({"right": kemi, "left": store})
    store.neighbors.update({"right": haaparanta})