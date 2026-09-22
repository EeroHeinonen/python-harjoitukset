#Used to clear console using system("cls")
from os import system
#Importin method from sibling module
from .bc import badCommand

#Sets common variables
settingsCommand = ""
difficulty = "Normal"

#Displays the "settings" menu
def settingsMenu():
    #Sets the "settingCommand" variable to be used across methods
    global settingsCommand
    settingsCommand = ""
    #While loop to display the "settings" menu
    while settingsCommand.strip().casefold() != "back":
        system("cls")
        print("Settings available: \n\n- Difficulty\n")
        print('"Back" to go back\n')
        settingsCommand = input("Enter a setting to change: ")
        #Displays the "difficulty settings" menu
        if settingsCommand.strip().casefold() == "difficulty":
            difficultySetting()
        #Breaks the while loop in the case that the player input is "back"
        elif settingsCommand.strip().casefold() == "back":
            break
        #Displays an "Invalid command" message if the player input is not recognized
        else:
            badCommand()
    #Returns the player chosen difficulty as a variable
    return difficulty

#Displays the "difficulty settings" menu
def difficultySetting():
    #Sets the variables to be used across methods
    global settingsCommand
    global difficulty
    #While loop to display the "difficulty settings" menu
    while settingsCommand.strip().casefold() != "back":
        system("cls")
        print("Current difficulty: " + difficulty)
        print("Difficulty settings: \n\n- Easy \n- Normal \n- Hard\n")
        print('"Back" to go back')
        settingsCommand = input("Enter a difficulty option: ")
        #Sets the game difficulty to easy
        if settingsCommand.strip().casefold() == "easy":
            difficulty = "Easy"
        #Sets the game difficulty to normal
        elif settingsCommand.strip().casefold() == "normal":
            difficulty = "Normal"
        #Sets the game difficulty to hard
        elif settingsCommand.strip().casefold() == "hard":
            difficulty = "Hard"
        #Returns from the "difficulty settings" menu to the "settings" menu
        elif settingsCommand.strip().casefold() == "back":
            settingsMenu()
        #Displays an "Invalid command" message if the player input is not recognized
        else:
            badCommand()