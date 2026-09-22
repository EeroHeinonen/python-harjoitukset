#Used to clear console using system("cls")
from os import system
#Importin method from sibling module
from .bc import badCommand

#Initiates the Player class
class PlayerInv:
    def __init__(self, inventory):
        self.inventory = []

#Creates the player object
player = PlayerInv([])

#Displays the menu for the player to add items to their inventory
def addItem():
    #Sets the "item" variable's value to "0"
    item = "0"
    #While loop to display the menu for the player to add items to their inventory
    while item != "STOP":
        system("cls")
        item = input('Input item to be added (Or "back" to go back): ')
        #Breaks the while loop in the case that the player input is "back"
        if item.strip().casefold() == "back":
            break
        else:
            #Adds the player input as an item to their inventory, if it is not empty
            if item != "":
                player.inventory.append(item)
                print("\nItem added to inventory!\n")
                input('Press any key to continue...')
            #Displays a message informing the player that their input was empty
            else:
                print("\nItem name can not be empty!\n")
                input("Press any key to continue...")

#Displays the player inventory
def showInventory():
    system("cls")
    #Checks if the inventory is not empty
    if player.inventory:
        #Displays each item inside the list "inventory" in a neatly formatted way
        for item in player.inventory:
            print(f"- {item}")
    #Displays a message informing the player that their inventory is empty
    else:
        print("The inventory is empty!")
    input("\nPress any key to continue...")