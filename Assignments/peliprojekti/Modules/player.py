#Used to clear console using system("cls")
from os import system
import os
#Importing methods from sibling modules
from .room import assignNeighbors, livingRoom, Damaging, Healing, Money, rooms
#Importing the pickle library
import pickle

#Initiates the Player class
class Player:
    def __init__(self, name, age, inventory, currentRoom, health, money, difMult):
        self.name = name
        self.age = age
        self.inventory = []
        self.currentRoom = currentRoom
        self.health = health
        self.money = money
        self.difMult = difMult

    #Save the player data using pickle
    def saveData(self):
        try:
            #Set the path for the save file
            savepath = "Assignments/peliprojekti/saves/" + self.name + ".pkl"
            with open(savepath, "wb") as saveFile:
                #Sets the data to be saved values
                data = {
                    "Player": self.name,
                    "Age": self.age,
                    "Items": self.inventory,
                    "Room": self.currentRoom,
                    "HP": self.health,
                    "Money": self.money,
                    "Difficulty": self.difMult
                    }
                #Saves the data to file according to player name
                pickle.dump(data, saveFile, protocol=pickle.HIGHEST_PROTOCOL)
        #Error handling if there is another error
        except IOError:
            print("There was an error processing the file!")
            input("Press any key to continue...")

    #Load the player data using pickle
    def loadData(self, fileName):
        try:
            #Set the path for the save file loading
            loadpath = "Assignments/peliprojekti/saves/" + fileName + ".pkl"
            #Load the data from the save file and returns the data as "loadFile"
            with open(loadpath, "rb") as saveFile:
                self.loadFile = pickle.load(saveFile)
            system("cls")
            #Inform the player the file has been loaded and set the player variables to variables from the loaded file
            print(f"File {fileName} loaded!")
            self.name = self.loadFile["Player"]
            self.age = self.loadFile["Age"]
            self.inventory = self.loadFile["Items"]
            self.currentRoom = self.loadFile["Room"]
            self.health = self.loadFile["HP"]
            self.money = self.loadFile["Money"]
            self.difMult = self.loadFile["Difficulty"]
            input("Press any key to continue...")
            return self.loadFile
        #Error handling if file does not exist, or if there is another error
        except FileNotFoundError:
            print("File not found!")
        except IOError:
            print("There was an error processing the file!")
            input("Press any key to continue...")

    #Delete the selected player data
    def deleteData(self, fileName):
        #Set the path for the save file deletion
        filePath = "Assignments/peliprojekti/saves/" + fileName + ".pkl"
        try:
            #Check if the selected file exists and remove it if it does
            if os.path.exists(filePath):
                os.remove(filePath)
                system("cls")
                print("Removed!")
                input("Press any key to continue...")
        except FileNotFoundError:
            print("File not found!")

p = Player("", 0, [], livingRoom, 100, 0, 1)

#Creates the player object
def createPlayer(name, age, inventory, currentRoom, health, money, difMult):
    p = Player(name, age, inventory, currentRoom, health, money, difMult)
    
#Set the enemy health and damage according to player difficulty
def setEnemyDif():
    for room in rooms:
        for enemy in room.enemies:
            originalEnemyHPValue, originalEnemyDMGValue = enemy.setOriginalValues()
            enemy.health = originalEnemyHPValue * p.difMult
            enemy.damage = originalEnemyDMGValue * p.difMult

#Displays the player inventory
def showInventory():
    system("cls")
    #Checks if the inventory is not empty
    if p.inventory:
        print("Items in inventory:\n")
        #Displays each item inside the player "inventory" in a neatly formatted way
        for item in p.inventory:
            if issubclass(type(item), Damaging) or issubclass(type(item), Healing):
                print(f"- {item.name.title()}\nUses: {item.uses}\n")
        if p.money > 0:
            print(f"Amount of money: {p.money} €\n")
    #Displays a message informing the player that their inventory is empty
    else:
        print("The inventory is empty!")
    input("Press any key to continue...")

def pickUp():
    pickUpItem = ""
    #While loop to continue picking up items until player input is "q" or "quit"
    while pickUpItem.strip().casefold() != "q":
        system("cls")
        print(f"{p.currentRoom.name}\n")
        #Checks if the room is not empty
        if p.currentRoom.items:
            #Displays each item inside the list "items" in a neatly formatted way
            for item in p.currentRoom.items:
                if issubclass(type(item), Damaging) or issubclass(type(item), Healing):
                    print(f"- {item.name.title()}")
                elif issubclass(type(item), Money):
                    print(f"Money: {item.amount} €")
            print('\nInput "q" to go back.')
            pickUpItem = input("or input item name to pick up: ")
            #Add the player input as an item to their inventory, if it is found in the room
            for item in p.currentRoom.items:
                #Check if the item is already in the player's inventory
                if item not in p.inventory:
                    #Check if item is of class "Damaging" or "Healing"
                    if issubclass(type(item), Damaging) or issubclass(type(item), Healing):
                        if pickUpItem.strip().casefold() == item.name.strip().casefold():
                            #Add the item to the player's inventory
                            p.inventory.append(item)
                            #Remove the item from the current room's items list
                            p.currentRoom.items.remove(item)
                            p.saveData()
                            system("cls")
                            print("Item added to inventory!\n")
                            pickUpItem = ""
                            input('Press any key to continue...')
                    #If neither is true and the player input is "money" add the amount of money in the room to the player's total money and remove the item object "Money" from the current room
                    elif pickUpItem.strip().casefold() == "money":
                        p.money += item.amount
                        p.currentRoom.items.remove(item)
                        p.saveData()
                        system("cls")
                        if item.cleanliness == "clean":
                            print("Money added to inventory!\n")
                        elif item.cleanliness == "dirty":
                            print("Money added to inventory!\n You monster... \n")
                        pickUpItem = ""
                        input('Press any key to continue...')
                else:
                    #Add the uses of the new item to the item already in the player inventory to avoid overlap
                    for instances in p.inventory:
                        instances.uses += item.uses
                    #Remove the item from the current room's items list
                    p.currentRoom.items.remove(item)
                    p.saveData()
                    system("cls")
                    print("Item added to inventory!\n")
                    pickUpItem = ""
                    input('Press any key to continue...')
        #If the room is empty, display a message notifying the player of this
        else:
            print("The room is empty!\n")
            input('Press any key to continue...')
            break

#Display "use" menu for the player to use items
def use():
    use = ""
    #While loop to continue running while player input is something else than "q"
    while use.strip().casefold() != "q":
        system("cls")
        #Check if the player's inventory is empty
        if p.inventory:
            pass
            #Print all items in the player's inventory
            print("Available items: \n")
            for item in p.inventory:
                print(f"- {item.name.title()}\nUses: {item.uses}\n")
            print('\nInput "q" to go back.')
            use = input("or input the item to be used: ")
            #For loop to check if player input exists in the player inventory
            for item in p.inventory:
                #Check if the item is found in the player inventory
                if use.strip().casefold() == item.name.strip().casefold():
                    #Check if the item has any uses left
                    if item.uses > 0:
                        #Check what class the "item" is
                        if issubclass(type(item), Damaging):
                            #Check if there are enemies in the current room and damage the enemy if one is present in the current room
                            if p.currentRoom.enemies:
                                for enemy in p.currentRoom.enemies:
                                    try:
                                        #Call the Enemy.takeDmg() function to calculate damage dealt
                                        enemy.takeDmg(item)
                                        item.uses -= 1
                                        p.saveData()
                                        use = "q"
                                    except OSError:
                                        pass
                            #Informs the player if there is no enemies in the room
                            else:
                                system("cls")
                                print("There are no enemies in the current room!")
                                input("Press any key to continue...")
                                use = "q"
                        #Check what class the "item" is
                        elif issubclass(type(item), Healing):
                            #Heals the player for the amount that the used item heals
                            p.health += item.healing
                            system("cls")
                            print(f"You healed for {item.healing} hp, your current health is {p.health}!")
                            input("Press any key to continue...")
                            item.uses -= 1
                            p.saveData()
                            use = "q"

                #Remove item from player inventory, if it's uses is 0
                if item.uses == 0:
                    system("cls")
                    print("Item is out of uses and is destroyed!")
                    p.inventory.remove(item)
                    p.saveData()
                    input("Press any key to continue...")
        #Inform the player that they have no usable items
        else:
            print("There are no usable items!")
            input("\nPress any key to continue...")
            break

#Display "move" menu for the player 
def move():
    directionToMove = ""
    #While loop to ask player for their movement input
    while directionToMove != "q":
        system("cls")
        directionToMove = input('Input "q" or "quit" to go back \nor input the direction to move to ("up", "down", "left", "right"): ')

        #Checks if the movement input is possible
        if directionToMove.strip().casefold() in p.currentRoom.neighbors:
            #Change the player's current room to wanted room
            p.currentRoom = p.currentRoom.neighbors[directionToMove.strip().casefold()]
            p.saveData()
            break

        #Breaks out of the loop if player input is either "quit" or "q"
        elif directionToMove.strip().casefold() == "quit" or directionToMove.strip().casefold() == "q":
            break

        #Inform player that the direction is not possible
        else:
            system("cls")
            directionToMove = ""
            print("Direction not available!")
            input("Press any key to continue...")