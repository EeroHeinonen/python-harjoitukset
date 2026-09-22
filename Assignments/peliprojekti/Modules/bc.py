#Used to clear console using system("cls")
from os import system

#Clears the console and displays an 'Invalid command' message
def badCommand():
    system("cls")
    print("Invalid command!")
    input("Press any key to continue...")
    system("cls")