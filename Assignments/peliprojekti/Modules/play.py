#Used to clear console using system("cls")
from os import system
#Importing methods from sibling modules
from .bc import badCommand
from .player import showInventory, addItem

#Display the "play" menu, from which a player can select to either add to or view their inventory
def play():
    playCommand = ""
    #While loop to display the "play" menu
    while playCommand != "back":
        system("cls")
        print("Available commands: \n\n- Add item \n- Inventory (Show inventory)\n")
        print('"Back" to go back\n')
        playCommand = input("Enter a command: ")
        #Displays the "add item" menu for the player to add items to their inventory
        if playCommand.strip().casefold() == "additem" or playCommand.strip().casefold() == "add item":
            addItem()
        #Displays the inventory the player currently possesses
        elif playCommand.strip().casefold() == "inventory":
            showInventory()
        #Breaks out of the while loop if player command is "back"
        elif playCommand.strip().casefold() == "back":
            break
        #Displays an "Invalid command" screen if the player input is not recognized
        else:
            badCommand()