from os import system

name = input("Enter your name: ")
age = int(input("Enter your age: "))
command = ""
difficulty = "Normal"
inventory = []
item = "0"

def settings():
    global difficulty
    system("cls")
    print("Settings available: \nDifficulty")
    print('"Back" or nothing to go back')
    command = input("Enter a setting to change: ")
    r
    if command == "Difficulty" or command == "difficulty":

        system("cls")
        print("Current difficulty: " + difficulty)
        print("Difficulty settings: \nEasy \nNormal \nHard")
        print('"Back" or nothing to go back')
        command = input("Enter a difficulty to change: ")
        if command == "Easy" or command == "easy":
            difficulty = "Easy"
        elif command == "Normal" or command == "normal":
            difficulty = "Normal"
        elif command == "Hard" or command == "hard":
            difficulty = "Hard"
        elif command != "Back" or command != "back" or command != "BACK":
            pass

        

    return difficulty

def addItem():
    system("cls")
    global item
    while item != "":
        item = input('Input item to be added (Or "back" / nothing to go back): ')
        if item != "back" and item != "Back" and item != "BACK":
            if item != "":
                inventory.append(item)
        else:
            pass

    return item

def showInventory():
    system("cls")
    global item
    for item in inventory:
        print(f"- {item}")
    input('Press any key to continue...')

if age < 12:
    print("The minimum age is 12!")
else:
    while command != "stop" or command != "exit" or command != "quit" or command != "Stop" or command != "Exit" or command != "Quit" or command != "STOP" or command != "EXIT" or command != "QUIT":
        system("cls")
        print(r"""

                                         _  _  ____  __     ___  __   _  _  ____ 
                                        / )( \(  __)(  )   / __)/  \ ( \/ )(  __)
                                        \ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) 
                                        (_/\_)(____)\____/ \___)\__/ \_)(_/(____)


                """)
        print("Available commands: \nPlay (play) \nInventory (add item, show inventory) \nSettings (settings) \nQuit (quit, exit, stop)")
        command = input("Enter a command: ")
        if command == "quit" or command == "exit" or command == "stop":
            break
        elif command == "settings" or command == "Settings" or command == "SETTINGS":
            settings()
        elif command == "add item" or command == "Add Item" or command == "Add item" or command == "add Item" or command == "ADD ITEM" or command == "additem" or command == "Additem"or command == "addItem" or command == "ADDITEM":
            addItem()
        elif command == "inventory" or command == "Inventory" or command == "INVENTORY":
            showInventory()
        elif command == "Play" or command == "play":
            system("cls")
            print("Not yet available!")
            input("Press any key to continue...")
            ## Game code tba
        else:
            system("cls")
            print("Invalid command!")
            input("Press any key to continue...")