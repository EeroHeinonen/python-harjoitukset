#Used to clear console using system("cls")
from os import system
#Importin method from sibling module
from .bc import badCommand
from .item import Item
from .room import livingRoom

#Initiates the Player class
class PlayerInv:
    def __init__(self, inventory, currentRoom):
        self.inventory = []
        self.currentRoom = currentRoom

currentRoom = livingRoom

#Creates the player object
p = PlayerInv([], currentRoom)

vase = Item("vaasi", 15, 1)
shovel = Item("lapio", 10, 10)
livingRoom.items.extend([vase, shovel])

#Displays the player inventory
def showInventory():
    system("cls")
    #Checks if the inventory is not empty
    if p.inventory:
        #Displays each item inside the list "inventory" in a neatly formatted way
        for item in p.inventory:
            print(f"- {item.name.title()}")
    #Displays a message informing the player that their inventory is empty
    else:
        print("The inventory is empty!")
    input("\nPress any key to continue...")

def pickUp():
    pickUpItem = ""
    while pickUpItem.strip().casefold() != "back":
        system("cls")
        print(f"{p.currentRoom}\n")
        #Checks if the room is not empty
        if p.currentRoom.items:
            #Displays each item inside the list "items" in a neatly formatted way
            for item in p.currentRoom.items:
                print(f"- {item.name.title()}")
            print('\nInput "back" to go back.')
            pickUpItem = input("Input item name to pick up: ")
            #Adds the player input as an item to their inventory, if it is found in the room
            for item in p.currentRoom.items:
                try:
                    if pickUpItem.strip().casefold() == item.name.strip().casefold():
                        p.inventory.append(item)
                        p.currentRoom.items.remove(item)
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
    system("cls")
    use = ""
    #While loop to continue running while player input is something else than "back"
    while use.strip().casefold() != "back":
        #Check if the player's inventory is empty
        if p.inventory:
            pass
            #Print all items in the player's inventory
            print("Available items: \n")
            for item in p.inventory:
                print(f"- {item.name.title()}")
            print('Input "back" to go back.')
            use = input("Input the item to be used: ")
            #For loop to check if player input exists in the player inventory
            for item in p.inventory:
                if use.strip().casefold() == item.name.strip().casefold():
                    #Check if the item has any uses left
                    if item.uses > 0:
                        system("cls")
                        print("Item used!")
                        input("Press any key to continue...")
                        item.uses -= 1
                        #Remove item from player inventory, if it's uses is 0
                        if item.uses == 0:
                            system("cls")
                            print("Item is out of uses and is destroyed!")
                            p.inventory.remove(item)
                            input("Press any key to continue...")

        else:
            print("The inventory is empty!")
            input("\nPress any key to continue...")
            break

def move():
    directionToMove = ""
    while directionToMove != "q":
        system("cls")
        directionToMove = input("Input the direction to move to: ")

        if directionToMove.strip().casefold() in rooms[p.currentRoom.name]:
            p.currentRoom = rooms[p.currentRoom][directionToMove]
        elif directionToMove.strip().casefold() == "back":
            break
        else:
            badCommand()