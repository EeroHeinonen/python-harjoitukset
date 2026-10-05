#Importin methods from sibling modules
from .item import Item, Damaging, Healing, Money
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
kitchen = Room("Kitchen", [], [], {})
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

rooms = [livingRoom, street, gutter, tampere, seinäjoki, kokkola, kalajoki, jyväskylä, kuopio, kajaani, suomussalmi, oulu, pudasjärvi, ranua, taivalkoski, kemi, haaparanta, hardwareStore, store]

def populateRooms():
    #Create item objects and assigns them values aka. name, damage/healing, uses
    vase = Damaging("vase", 15, 1)
    shovel = Damaging("shovel", 10, 10)
    baseballBat = Damaging("baseball bat", 25, 15)
    hammer = Damaging("hammer", 20, 20)
    baton = Damaging("baton", 30, 99)
    sandwich = Healing("sandwich", 15, 1)
    candy = Healing("ässä mix hedelmä", 20, 1)

    #Create enemy objects
    hobo = Enemy("Homeless", 20, 5, gutter, Money(random.randint(0, 10), "clean"))
    hobo2 = Enemy("Homeless", 20, 5, suomussalmi, Money(random.randint(0, 10), "clean"))
    hobo3 = Enemy("Homeless with a knife", 30, 15, pudasjärvi, Money(20, "clean"))
    hobo4 = Enemy("Homeless", 20, 5, kalajoki, Money(random.randint(0, 10), "clean"))
    hobo5 = Enemy("Homeless who knows martial arts", 35, 10, ranua, Money(15, "clean"))
    innocentPerson = Enemy("Innocent person", 25, 0, taivalkoski, Money(50, "dirty"))
    antiEnvironmentalist = Enemy("Anti-environmentalist", 15, 15, tampere, shovel)
    antiEnvironmentalist2 = Enemy("Anti-environmentalist", 15, 15, jyväskylä, sandwich)
    antiEnvironmentalist3 = Enemy("Anti-environmentalist", 15, 15, seinäjoki, candy)
    antiEnvironmentalist4 = Enemy("Anti-environmentalist", 15, 15, oulu, sandwich)
    antiEnvironmentalist5 = Enemy("Anti-environmentalist", 15, 15, kuopio, candy)
    borderPatrol = Enemy("Border patrol", 40, 30, tornio, baton)

    #Add the items to room items
    livingRoom.items.append(vase)
    kitchen.items.append(sandwich)
    street.items.append(Money(random.randint(5, 10)))
    kajaani.items.append(shovel)
    kemi.items.append(Money(random.randint(10, 15)))
    kokkola.items.append(Money(random.randint(5, 10)))
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
    livingRoom.neighbors.update({"up": street, "left": kitchen})
    kitchen.neighbors.update({"right": livingRoom})
    street.neighbors.update({"down": livingRoom, "left": gutter, "up": tampere})
    gutter.neighbors.update({"right": street})
    tampere.neighbors.update({"down": street, "right": jyväskylä, "left": seinäjoki, "up": hardwareStore})
    seinäjoki.neighbors.update({"right": tampere, "up": kokkola})
    kokkola.neighbors.update({"down": seinäjoki, "up": kalajoki})
    kalajoki.neighbors.update({"down": kokkola, "up": oulu, "right": kajaani})
    jyväskylä.neighbors.update({"left": tampere, "right": kuopio})
    kuopio.neighbors.update({"left": jyväskylä, "up": kajaani, "right": hardwareStore})
    kajaani.neighbors.update({"down": kuopio, "up": suomussalmi, "left": kalajoki})
    suomussalmi.neighbors.update({"down": kajaani, "up": taivalkoski})
    taivalkoski.neighbors.update({"down": suomussalmi, "left": pudasjärvi})
    oulu.neighbors.update({"down": kalajoki, "up": kemi, "right": pudasjärvi, "left": hardwareStore})
    pudasjärvi.neighbors.update({"left": oulu, "right": taivalkoski, "up": ranua})
    ranua.neighbors.update({"left": kemi, "down": pudasjärvi})
    kemi.neighbors.update({"right": ranua, "down": oulu, "left": haaparanta})
    haaparanta.neighbors.update({"right": kemi, "left": tornio, "down": hardwareStore})
    tornio.neighbors.update({"right": haaparanta, "left": store})
    hardwareStore.neighbors.update({"up": haaparanta, "left": kuopio, "down": tampere, "right": oulu})
    store.neighbors.update({"right": tornio})