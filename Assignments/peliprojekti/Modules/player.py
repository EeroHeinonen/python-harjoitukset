#Used to clear console using system("cls")
from os import system
#Importing methods from sibling modules
from .room import assignNeighbors, livingRoom, Damaging, Healing, rooms
#Importing the json library
import json
import pickle

#Initiates the Player class
class Player:
    def __init__(self, name, age, inventory, currentRoom, health, difMult):
        self.name = name
        self.age = age
        self.inventory = []
        self.currentRoom = currentRoom
        self.health = health
        self.difMult = difMult

    #Saves the player data using pickle
    def saveData(self):
        try:
            with open("save.pkl", "wb") as saveFile:
                #Sets the data to be saved values
                data = {
                    "Player": self.name,
                    "Age": self.age,
                    "Items": self.inventory,
                    "Room": self.currentRoom,
                    "HP": self.health,
                    "Difficulty": self.difMult
                    }
                #Saves the data to file known as "save.pkl"
                pickle.dump(data, saveFile, protocol=pickle.HIGHEST_PROTOCOL)
        #Error handling if file does not exist, or if there is another error
        except FileNotFoundError:
            print("File not found!")
            input("Press any key to continue...")
        except IOError:
            print("There was an error processing the file!")
            input("Press any key to continue...")

    #Loads the player data using pickle
    def loadData(self):
        try:
            #Loads the data from "save.pkl" and returns the data as "loadFile"
            with open("save.pkl", "rb") as saveFile:
                self.loadFile = pickle.load(saveFile)
            return self.loadFile
        #Error handling if file does not exist, or if there is another error
        except FileNotFoundError:
            print("File not found!")
            input("Press any key to continue...")
        except IOError:
            print("There was an error processing the file!")
            input("Press any key to continue...")

    def takeDmg(self, enemy):
        self.health -= enemy.damage
        if self.health <= 0:
            self.health = 0
            GameOver = true
    
    #Set the enemy health and damage according to player difficulty
    def setEnemyDif(self):
        for room in rooms:
            for enemy in room.enemies:
                enemy.health = enemy.health * self.difMult
                enemy.damage = enemy.damage * self.difMult

currentRoom = livingRoom

#Creates the player object
p = Player("", 0, [], currentRoom, 100, 1)
#Displays the player inventory
def showInventory():
    p.loadData()
    system("cls")
    #Checks if the inventory is not empty
    if p.inventory:
        print("Items in inventory:")
        #Displays each item inside the player "inventory" in a neatly formatted way
        for item in p.inventory:
            print(f"- {item.name.title()}\nUses: {item.uses}\n")
    #Displays a message informing the player that their inventory is empty
    else:
        print("The inventory is empty!")
    input("\nPress any key to continue...")

def pickUp():
    p.loadData()
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
    p.loadData()
    use = ""
    #While loop to continue running while player input is something else than "back"
    while use.strip().casefold() != "q":
        system("cls")
        #Check if the player's inventory is empty
        if p.inventory:
            pass
            #Print all items in the player's inventory
            print("Available items: \n")
            for item in p.loadFile["Items"]:
                print(f"- {item.name.title()}\nUses: {item.uses}\n")
            print('\nInput "q" to go back.')
            use = input("or input the item to be used: ")
            #For loop to check if player input exists in the player inventory
            for item in p.inventory:
                if use.strip().casefold() == item.name.strip().casefold():
                    #Check if the item has any uses left
                    if item.uses > 0:
                        #Check if there are enemies in the current room
                        if issubclass(type(item), Damaging):
                            #Damage the enemy if one is present in the current room
                            try:
                                for enemy in p.currentRoom.enemies:
                                    enemy.health -= item.dmg
                                system("cls")
                                print("Item used!")
                                #Inform the player of the damage they did
                                if enemy.health > 0:
                                    print(f"You did {item.dmg} damage and the enemy's health was lowered to {enemy.health}!")
                                    input("Press any key to continue...")
                                else:
                                    print("You have defeated the enemy!")
                                    #Delete the enemy object from the current rooms enemies list
                                    try:
                                        enemy.health = 0
                                        p.currentRoom.enemies.remove(enemy)
                                    except IndexError:
                                        pass
                                    input("Press any key to continue...")
                                item.uses -= 1
                                p.saveData()
                            except IndexError:
                                pass
                        elif issubclass(type(item), Healing):
                            #Heals the player for the amount
                            p.health += item.healing
                            print(f"You healed for {item.healing} amount, your current health is {p.health}!")
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
    p.loadData()
    directionToMove = ""
    #While loop to ask player for their movement input
    while directionToMove != "q":
        system("cls")
        directionToMove = input('Input "q" or "quit" to go back \nor input the direction to move to ("up", "down", "left", "right"): ')

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