#Used to clear console using system("cls")
from os import system
#Importing methods from sibling modules
from .item import Item
from .room import assignNeighbors, livingRoom
#Importing the json library
import json
import pickle

#Initiates the Player class
class Player:
    def __init__(self, name, age, inventory, currentRoom):
        self.name = name
        self.age = age
        self.inventory = []
        self.currentRoom = currentRoom

    def saveData(self):
        try:
            with open("save.pkl", "wb") as saveFile:
                data = {
                    "Player": self.name,
                    "Age": self.age,
                    "Items": self.inventory,
                    "Room": self.currentRoom
                    }
                pickle.dump(data, saveFile, protocol=pickle.HIGHEST_PROTOCOL)
        except FileNotFoundError:
            print("File not found!")
        except IOError:
            print("There was an error processing the file!")

    def loadData(self):
        try:
            with open("save.pkl", "rb") as saveFile:
                self.loadFile = pickle.load(saveFile)
            return self.loadFile
        except FileNotFoundError:
            print("File not found!")
        except IOError:
            print("There was an error processing the file!")



currentRoom = livingRoom

#Creates the player object
p = Player("", 0, [], currentRoom)

#Creates item objects and assigns them values ex. name, damage, uses
vase = Item("vaasi", 15, 1)
shovel = Item("lapio", 10, 10)
#Adds the items to the room's itempool
livingRoom.items.extend([vase, shovel])

#Displays the player inventory
def showInventory():
    system("cls")
    #Checks if the inventory is not empty
    if p.inventory:
        #Fetches the player's data from the save file
        #Displays each item inside the player "inventory" in a neatly formatted way
        for item in p.inventory:
            print(f"- {item.name.title()}")
    #Displays a message informing the player that their inventory is empty
    else:
        print("The inventory is empty!")
    input("\nPress any key to continue...")

def pickUp():
    pickUpItem = ""
    while pickUpItem.strip().casefold() != "q":
        system("cls")
        print(f"{p.loadFile["Room"].name}\n")
        #Checks if the room is not empty
        if p.currentRoom.items:
            #Displays each item inside the list "items" in a neatly formatted way
            for item in p.currentRoom.items:
                print(f"- {item.name.title()}")
            print('\nInput "q" to go back.')
            pickUpItem = input("or input item name to pick up: ")
            #Adds the player input as an item to their inventory, if it is found in the room
            for item in p.currentRoom.items:
                try:
                    if pickUpItem.strip().casefold() == item.name.strip().casefold():
                        p.inventory.append(item)
                        p.currentRoom.items.remove(item)
                        p.saveData()
                        system("cls")
                        print("Item added to inventory!\n")
                        pickUpItem = ""
                        input('Press any key to continue...')
                except IndexError:
                    pass

        else:
            print("The room is empty!\n")
            input('Press any key to continue...')
            break

def use():
    use = ""
    #While loop to continue running while player input is something else than "back"
    while use.strip().casefold() != "q":
        system("cls")
        #Check if the player's inventory is empty
        if p.inventory:
            pass
            #Print all items in the player's inventory
            print("Available items: \n")
            for item in p.inventory:
                print(f"- {item.name.title()}")
            print('\nInput "q" to go back.')
            use = input("or input the item to be used: ")
            #For loop to check if player input exists in the player inventory
            for item in p.inventory:
                if use.strip().casefold() == item.name.strip().casefold():
                    #Check if the item has any uses left
                    if item.uses > 0:
                        system("cls")
                        print("Item used!")
                        input("Press any key to continue...")
                        item.uses -= 1
                        p.saveData()
                        #Remove item from player inventory, if it's uses is 0
                        if item.uses == 0:
                            system("cls")
                            print("Item is out of uses and is destroyed!")
                            p.inventory.remove(item)
                            p.saveData()
                            input("Press any key to continue...")

        else:
            print("The inventory is empty!")
            input("\nPress any key to continue...")
            break

def move():
    directionToMove = ""
    #While loop to ask player for their movement input
    while directionToMove != "q":
        system("cls")
        directionToMove = input('Input "q" or "quit" to go back \nor input the direction to move to: ')

        #Checks if the movement input is possible
        if directionToMove.strip().casefold() in p.currentRoom.neighbors:
            p.currentRoom = p.currentRoom.neighbors[directionToMove.strip().casefold()]
            p.saveData()
            break
        
        #Breaks out of the loop if player input is either "quit" or "q"
        elif directionToMove.strip().casefold() == "quit" or directionToMove.strip().casefold() == "q":
            break

        else:
            system("cls")
            directionToMove = ""
            print("Direction not available!")
            input("Press any key to continue...")