#Used to clear console using system("cls")
from os import system
#Imports to exit the program and to delete the player save file after game completion
import os
import sys
#Importing methods from sibling modules
from .bc import badCommand
from .player import createPlayer, showInventory, pickUp, use, move, p
from .room import store, haaparanta
import random

#Display the "play" menu, from which a player can select to either add to or view their inventory
def play():
    #Set enemy health and damage according to player difficulty level
    playCommand = ""
    #While loop to display the "play" menu
    while playCommand != "q":
        #Check if player has reached the last room
        if p.currentRoom.name.strip().casefold() != store.name.strip().casefold():
            system("cls")
            #Display current room information and player information
            print(f"You're in the: {p.currentRoom.name}\n")
            if p.currentRoom.enemies:
                print("Current enemy in room:") 
                for enemy in p.currentRoom.enemies:
                    print(f"{enemy.name}\nHP: {enemy.health}")
                    enemy.attack(p)
            print(f"Player health: {p.health}")
            #Display available commands
            print("\nAvailable commands: \n\n- Move (move) \n- Pick up item (pick up or pickup) \n- Inventory (inventory) \n- Use item (use)")
            print('or "q" to go back\n')
            playCommand = input("Enter a command: ")
            #Display the "add item" menu for the player to add items to their inventory
            if playCommand.strip().casefold() == "pickup" or playCommand.strip().casefold() == "pick up":
                pickUp()
            #Display the "inventory" menu
            elif playCommand.strip().casefold() == "inventory":
                showInventory()
            #Display the "use" menu
            elif playCommand.strip().casefold() == "use":
                use()
            #Display the "move" menu
            elif playCommand.strip().casefold() == "move":
                move()
            #Breaks out of the while loop if player input is "q"
            elif playCommand.strip().casefold() == "q":
                break
            #Displays an "Invalid command" screen if the player input is not recognized
            else:
                badCommand()
        #Display final menu
        else:
            system("cls")
            if p.money >= 100:
                print("You have reached the Haaparanta candy store!\n\nThis is the end of the line.\nNow...\nThe ultimate question...\n\nWill you purchase this piece of salmiakki for a 100 €?")
                print(r"""

   /\
  /  \
 /    \
/      \
\      /
 \    /
  \  /
   \/

                                """)
                print("Yes (y) or no (n)?")
                answer = input()
                if answer.strip().casefold() == "y":
                    system("cls")
                    print(r"""

  ___  __   __ _   ___  ____   __  ____  _  _  __     __  ____  __  __   __ _  ____  _  _  _   
 / __)/  \ (  ( \ / __)(  _ \ / _\(_  _)/ )( \(  )   / _\(_  _)(  )/  \ (  ( \/ ___)/ \/ \/ \  
( (__(  O )/    /( (_ \ )   //    \ )(  ) \/ (/ (_/\/    \ )(   )((  O )/    /\___ \\_/\_/\_/  
 \___)\__/ \_)__) \___/(__\_)\_/\_/(__) \____/\____/\_/\_/(__) (__)\__/ \_)__)(____/(_)(_)(_) 

                                    """)
                    print("The game is officially over now!\nYou managed to get enough money to buy the salmiakki from the candy store\nand you lived your life happily ever after having tasted salmiakki for the last time.\n\nThe End!\n")
                    os.remove("Assignments/peliprojekti/saves/" + p.name + ".pkl")
                    sys.exit()
                elif answer.strip().casefold() == "n":
                    system("cls")
                    for i in range (100):
                        print(r"""

 _  _  __   _  _    ____  __    __   __    _  _  _   
( \/ )/  \ / )( \  (  __)/  \  /  \ (  )  / \/ \/ \  
 )  /(  O )) \/ (   ) _)(  O )(  O )/ (_/\\_/\_/\_/  
(__/  \__/ \____/  (__)  \__/  \__/ \____/(_)(_)(_)  
            

                                    """)
                    sys.exit()
                else:
                    badCommand()
            else:
                print("You don't have enough money yet to buy the salmiakki!")
                input("Press any key to continue...")
                p.currentRoom = haaparanta