#Used to clear console using system("cls")
from os import system
#Importing methods from sibling modules
from .bc import badCommand
from .player import p, showInventory, pickUp, use, move

#Display the "play" menu, from which a player can select to either add to or view their inventory
def play():
    playCommand = ""
    #While loop to display the "play" menu
    while playCommand != "back":
        system("cls")
        print(f"You're in the: {p.currentRoom.name}")
        print("\nAvailable commands: \n\n- Move \n- Pick up (Pick up item) \n- Inventory (Show inventory) \n- Use (Use item)")
        print('"Back" to go back\n')
        playCommand = input("Enter a command: ")
        #Displays the "add item" menu for the player to add items to their inventory
        if playCommand.strip().casefold() == "pickup" or playCommand.strip().casefold() == "pick up":
            pickUp()
        #Displays the inventory the player currently possesses
        elif playCommand.strip().casefold() == "inventory":
            showInventory()
        elif playCommand.strip().casefold() == "use":
            use()
        elif playCommand.strip().casefold() == "move":
            move()
        #Breaks out of the while loop if player command is "back"
        elif playCommand.strip().casefold() == "back":
            break
        #Displays an "Invalid command" screen if the player input is not recognized
        else:
            badCommand()