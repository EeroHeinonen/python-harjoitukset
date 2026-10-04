#Used to clear console using system("cls")
from os import system
#Importing methods from sibling modules
from .bc import badCommand
from .player import p, showInventory, pickUp, use, move
from .room import assignNeighbors

#Display the "play" menu, from which a player can select to either add to or view their inventory
def play():
    assignNeighbors()
    #Set enemy health and damage according to player difficulty level
    playCommand = ""
    #While loop to display the "play" menu
    while playCommand != "q":
        system("cls")
        print(f"You're in the: {p.currentRoom.name}\n")
        if p.currentRoom.enemies:
            print("Current enemy in room:") 
            for enemy in p.currentRoom.enemies:
                print(f"{enemy.name}\nHP: {enemy.health}")
        print("\nAvailable commands: \n\n- Move (move) \n- Pick up item (pick up or pickup) \n- Inventory (inventory) \n- Use item (use)")
        print('or "q" to go back\n')
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
        #Breaks out of the while loop if player input is "q"
        elif playCommand.strip().casefold() == "q":
            break
        #Displays an "Invalid command" screen if the player input is not recognized
        else:
            badCommand()