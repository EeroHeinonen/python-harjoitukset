#Importin methods from sibling modules
from .item import Damaging, Healing, Money
from .enemy import Enemy
import random

#Initiates the room class
class Room:
    def __init__(self, name, items, enemies, neighbors):
        self.name = name
        self.items = []
        self.enemies = []
        self.neighbors = {}

#Create the following objects of "Room" and add them to the list "rooms"
livingRoom = Room("Living room", [], [], {})
backyard = Room("Backyard", [], [], {})
kitchen = Room("Kitchen", [], [], {})
hardwareStore = Room("Backyard", [], [], {})
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
tornio = Room("Tornio", [], [], {})
hardwareStore = Room("Hardware store", [], [], {})
store = Room("Store", [], [], {})

rooms = [livingRoom, kitchen, backyard, street, gutter, tampere, seinäjoki, kokkola, kalajoki, jyväskylä, kuopio, kajaani, suomussalmi, oulu, pudasjärvi, ranua, taivalkoski, kemi, haaparanta, hardwareStore, store]

def populateRooms():
    #Create item objects and assigns them values aka. name, damage/healing, uses
    vase = Damaging("vase", 15, 1)
    shovel = Damaging("shovel", 10, 10)
    shovel2 = Damaging("shovel", 10, 10)
    baseballBat = Damaging("baseball bat", 25, 15)
    hammer = Damaging("hammer", 20, 20)
    baton = Damaging("baton", 30, 99)
    sandwich = Healing("sandwich", 20, 1)
    sandwich2 = Healing("sandwich", 20, 1)
    sandwich3 = Healing("sandwich", 20, 1)
    candy = Healing("candy", 15, 1)
    candy2 = Healing("candy", 15, 1)

    #Create enemy objects
    hobo = Enemy("Homeless", 20, 5, gutter, Money(random.randint(0, 10), "clean"))
    hobo2 = Enemy("Homeless", 20, 5, suomussalmi, Money(random.randint(0, 10), "clean"))
    hobo3 = Enemy("Homeless with a knife", 30, 15, pudasjärvi, Money(20, "clean"))
    hobo4 = Enemy("Homeless", 20, 5, kalajoki, Money(random.randint(0, 10), "clean"))
    hobo5 = Enemy("Homeless who knows martial arts", 35, 10, ranua, Money(15, "clean"))
    innocentPerson = Enemy("Innocent person", 25, 0, taivalkoski, Money(50, "dirty"))
    antiEnvironmentalist = Enemy("Anti-environmentalist", 15, 15, tampere, shovel2)
    antiEnvironmentalist2 = Enemy("Anti-environmentalist", 15, 15, jyväskylä, sandwich2)
    antiEnvironmentalist3 = Enemy("Anti-environmentalist", 15, 15, seinäjoki, candy)
    antiEnvironmentalist4 = Enemy("Anti-environmentalist", 15, 15, oulu, sandwich3)
    antiEnvironmentalist5 = Enemy("Anti-environmentalist", 15, 15, kuopio, candy2)
    borderPatrol = Enemy("Border patrol", 40, 30, tornio, baton)

    #Add the items to room items
    livingRoom.items.append(vase)
    kitchen.items.append(sandwich)
    street.items.append(Money(random.randint(5, 10), "clean"))
    kajaani.items.append(shovel)
    kemi.items.append(Money(random.randint(10, 15), "clean"))
    kokkola.items.append(Money(random.randint(5, 10), "clean"))
    backyard.items.append(shovel)
    hardwareStore.items.extend([shovel, baseballBat, hammer, baton])

    #Add enemies to room enemies
    gutter.enemies.append(hobo)
    suomussalmi.enemies.append(hobo2)
    pudasjärvi.enemies.append(hobo3)
    kalajoki.enemies.append(hobo4)
    ranua.enemies.append(hobo5)
    taivalkoski.enemies.append(innocentPerson)
    tampere.enemies.append(antiEnvironmentalist)
    jyväskylä.enemies.append(antiEnvironmentalist2)
    seinäjoki.enemies.append(antiEnvironmentalist3)
    oulu.enemies.append(antiEnvironmentalist4)
    kuopio.enemies.append(antiEnvironmentalist5)
    tornio.enemies.append(borderPatrol)

#Function to assign the rooms to have "neighbors", which allows player movememnt between rooms using directions
def assignNeighbors():
    livingRoom.neighbors.update({"u": street, "l": kitchen})
    kitchen.neighbors.update({"r": livingRoom, "d": backyard})
    backyard.neighbors.update({"u": kitchen})
    street.neighbors.update({"d": livingRoom, "l": gutter, "u": tampere})
    gutter.neighbors.update({"r": street})
    tampere.neighbors.update({"d": street, "r": jyväskylä, "l": seinäjoki})
    seinäjoki.neighbors.update({"r": tampere, "u": kokkola})
    kokkola.neighbors.update({"d": seinäjoki, "u": kalajoki})
    kalajoki.neighbors.update({"d": kokkola, "u": oulu, "r": kajaani})
    jyväskylä.neighbors.update({"l": tampere, "r": kuopio})
    kuopio.neighbors.update({"l": jyväskylä, "u": kajaani})
    kajaani.neighbors.update({"d": kuopio, "u": suomussalmi, "l": kalajoki})
    suomussalmi.neighbors.update({"d": kajaani, "u": taivalkoski})
    taivalkoski.neighbors.update({"d": suomussalmi, "l": pudasjärvi})
    oulu.neighbors.update({"d": kalajoki, "u": kemi, "r": pudasjärvi})
    pudasjärvi.neighbors.update({"l": oulu, "r": taivalkoski, "u": ranua})
    ranua.neighbors.update({"l": kemi, "d": pudasjärvi})
    kemi.neighbors.update({"r": ranua, "d": oulu, "l": tornio})
    haaparanta.neighbors.update({"l": store, "r": tornio})
    tornio.neighbors.update({"l": haaparanta, "r": kemi, "d": hardwareStore})
    hardwareStore.neighbors.update({"u": tornio})
    store.neighbors.update({"r": haaparanta})