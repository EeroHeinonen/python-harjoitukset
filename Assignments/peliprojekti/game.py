#Used to clear console using system("cls")
from os import system
#Importing other created modules
from Modules import settingsMenu, badCommand, play, player
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
                #Main while loop to display the main menu
                while command.strip().casefold() != "stop" or command.strip().casefold() != "exit" or command.strip().casefold() != "quit":
                    system("cls")
                    #Converts the player name to ascii art and prints it on the main menu
                    print(pyfiglet.figlet_format("Welcome  " + name.title()))
                    print("Available commands: \n\n- Play (play) \n- Settings (settings) \n- Quit (quit, exit, stop, q)\n")
                    command = input("Enter a command: ")
                    #Displays the "settings" menu for the player
                    if command.strip().casefold() == "settings":
                        settingsMenu()
                    #Displays the "play" menu for the player
                    elif command.strip().casefold() == "play":
                        play()
                    #Stops the program if one of the "quitting" keywords is inputted by the player
                    elif command.strip().casefold() == "stop" or command.strip().casefold() == "exit" or command.strip().casefold() == "quit" or command.strip().casefold() == "q":
                        break
                    #Displays an "Invalid command" message if the player input is not recognized
                    else:
                        badCommand()
