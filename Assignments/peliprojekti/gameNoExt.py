#Used to clear console using system("cls")
from os import system
import os
#Importing methods, objects and variables from Modules
from Modules import settingsMenu, badCommand, play, p, Room, Player, livingRoom, createPlayer, assignNeighbors
import pickle

#Initial input for the player name
name = input("Enter your name: ")
#Set common variables
age = ""
system("cls")
command = ""
fileName = ""

#Assign variables to the instructions and to the story file
with open("Assignments/peliprojekti/ohjeet.txt", "r") as instructions:
    ins = instructions.read()
with open("Assignments/peliprojekti/tarina.txt", "r") as intro:
    intro = intro.read()

#While loop until player inputs a name that isn't empty
while name == "" or name == "q":
    system("cls")
    print('You can not input an empty name or "q"!')
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
                system("cls")
                #Assign room neighbors using function from room.py
                assignNeighbors()
                #Assign player values for loading purposes
                p.name = name
                p.age = age
                print(intro)
                input("Press any key to continue...")
                #Attempt to autoload if a save file exists with the player name
                try:
                    with open("Assignments/peliprojekti/saves/" + name.strip().casefold() + ".pkl", "rb") as saveFile:
                        p.loadFile = pickle.load(saveFile)
                    p.loadData(name.strip().casefold())
                #Create a new save file with the player's name, age + default attributes
                except FileNotFoundError:
                    createPlayer(name, age, [], livingRoom, 100, 0, 1)
                    p.saveData()
                #Main while loop to display the main menu
                while command.strip().casefold() != "stop" or command.strip().casefold() != "exit" or command.strip().casefold() != "quit" or command.strip().casefold() != "q":
                    system("cls")
                    #Main menu ascii art
                    print(r"""

 _  _   __    __   ____   __   ____   __   __ _  __ _   __   __ _    _  _  _  _  __ _  ____  _  _   __  ____  __  ____ 
/ )( \ / _\  / _\ (  _ \ / _\ (  _ \ / _\ (  ( \(  ( \ / _\ (  ( \  / )( \/ )( \(  ( \/ ___)/ )( \ /  \(_  _)(  )(_  _)
) __ (/    \/    \ ) __//    \ )   //    \/    //    //    \/    /  ) __ () \/ (/    /\___ \\ \/ /(  O ) )(   )(   )(  
\_)(_/\_/\_/\_/\_/(__)  \_/\_/(__\_)\_/\_/\_)__)\_)__)\_/\_/\_)__)  \_)(_/\____/\_)__)(____/ \__/  \__/ (__) (__) (__) 


                            """)
                    print("Available commands: \n\n- Play (play) \n- Settings (settings) \n- Save (save) \n- Load (load)\n- Delete (delete)\n- Instructions (ins) \n- Quit (quit, exit, stop, q)\n")
                    command = input("Enter a command: ")
                    #Display the "settings" menu for the player
                    if command.strip().casefold() == "settings":
                        settingsMenu()
                    #Display the "play" menu for the player
                    elif command.strip().casefold() == "play":
                        play()
                    #Save the player's current game state by calling the Player.saveData() method
                    elif command.strip().casefold() == "save":
                        p.saveData()
                        input("Press any key to continue...")
                    #Display the "load" menu
                    elif command.strip().casefold() == "load":
                        #While loop to continue displaying the "load" menu until player input is either "q" or "quit"
                        while fileName.strip().casefold() != "q" or fileName.strip().casefold() != "quit":
                            system("cls")
                            #List all the files in the directory "saves"
                            if os.listdir("Assignments/peliprojekti/saves"):
                                #Prints all the files in the directory
                                print("Save files: \n")
                                for file in os.listdir("Assignments/peliprojekti/saves"):
                                    print(f"- {file}")
                                print('\nInput "q" or "quit" to go back')
                                fileName = input("Input the file name to be loaded: ")
                                if fileName.strip().casefold() == "q" or fileName.strip().casefold() == "quit":
                                    break
                                #Load the selected save file using player input as an argument
                                else:
                                    p.loadData(fileName)
                            #Inform the player there are no saves
                            else:
                                print("The save file directory is empty!")
                                input("Press any key to continuel...")
                                break
                    #Display the "delete" menu
                    elif command.strip().casefold() == "delete":
                        #While loop to display delete menu while player command is not "q" or "quit"
                        while fileName.strip().casefold() != "q" or fileName.strip().casefold() != "quit":
                            system("cls")
                            #List all files in the directory "saves"
                            if os.listdir("Assignments/peliprojekti/saves"):
                                #Print out all files in the directory
                                print("Save files: \n")
                                for file in os.listdir("Assignments/peliprojekti/saves"):
                                    print(f"- {file}")
                                print('\nInput "q" or "quit" to go back')
                                fileName = input("Input the file name to be deleted: ")
                                if fileName.strip().casefold() == "q"or fileName.strip().casefold() == "quit":
                                    break
                                #Delete selected player data by calling the Player.deleteData() method
                                else:
                                    p.deleteData(fileName)
                            #Display a message informing the directory is empty
                            else:
                                print("The save file directory is empty!")
                                input("Press any key to continuel...")
                                break
                    #Display the instructions menu
                    elif command.strip().casefold() == "ins":
                        system("cls")
                        print(ins)
                        input("Press any key to continue...")
                    #Stops the program if one of the "quitting" keywords is inputted by the player
                    elif command.strip().casefold() == "stop" or command.strip().casefold() == "exit" or command.strip().casefold() == "quit" or command.strip().casefold() == "q":
                        break
                    #Displays an "Invalid command" message if the player input is not recognized
                    else:
                        badCommand()