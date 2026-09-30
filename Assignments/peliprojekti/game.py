#Used to clear console using system("cls")
from os import system
#Importing methods, objects and variables from Modules
from Modules import settingsMenu, badCommand, play, p, Room, Player
#Importing the "pyfiglet" module for the creation of ascii art from input
import pyfiglet

#Initial input for the player name
name = input("Enter your name: ")
#Set common variables
age = ""
system("cls")
command = ""

#While loop until player inputs a name that isn't empty
while name == "":
    system("cls")
    print("You can not input an empty name!")
    input("Press any key to continue...")
    system("cls")
    name = input("Enter your name: ")
else:
    #While loop until player inputs an age that is a number
    while age == "":
        #Error handling using try/except if player inputs an age that is not a number
        try:
            system("cls")
            age = int(input("Enter your age: "))
        except ValueError:
            system("cls")
            print("You can not input an age that is not a number.")
            input("Press any key to continue...")
            age = ""
        else:
            #Check if player is under the age of 12
            if int(age) < 12:
                system("cls")
                print("The minimum age is 12!")
            else:
                p.name = name
                p.age = age
                p.saveData()
                #Main while loop to display the main menu
                while command.strip().casefold() != "stop" or command.strip().casefold() != "exit" or command.strip().casefold() != "quit" or command.strip().casefold() != "q":
                    system("cls")
                    #Fetches the player's data from the save file
                    #Converts the player name to ascii art and prints it on the main menu
                    print(pyfiglet.figlet_format("Welcome  " + p.loadData()["Player"].title()))
                    print("Available commands: \n\n- Play (play) \n- Settings (settings) \n- Save (save) \n- Load (load) \n- Quit (quit, exit, stop, q)\n")
                    command = input("Enter a command: ")
                    #Displays the "settings" menu for the player
                    if command.strip().casefold() == "settings":
                        settingsMenu()
                    #Displays the "play" menu for the player
                    elif command.strip().casefold() == "play":
                        play()
                    #Saves the game
                    elif command.strip().casefold() == "save":
                        p.saveData()
                        system("cls")
                        print("Saved succesfully!")
                        input("Press any key to continue...")
                    #Displays the "play" menu for the player
                    elif command.strip().casefold() == "load":
                        p.loadData()
                        system("cls")
                        print(f"Name: {p.loadFile["Player"].title()}\nAge: {p.loadFile["Age"]}\nCurrent room: {p.loadFile["Room"].name}")
                        print("Inventory: ")
                        for item in p.loadFile["Items"]:
                            print(f"- {item.name.title()}")
                        input("\nPress any key to continue...")
                    #Stops the program if one of the "quitting" keywords is inputted by the player
                    elif command.strip().casefold() == "stop" or command.strip().casefold() == "exit" or command.strip().casefold() == "quit" or command.strip().casefold() == "q":
                        break
                    #Displays an "Invalid command" message if the player input is not recognized
                    else:
                        badCommand()