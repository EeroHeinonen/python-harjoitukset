from os import system

##Projekti 1
name = input("Enter your name: ")
system("cls")
command = ""
difficulty = "Normal"
inventory = []
item = "0"

##Projekti 3
def settings():
    global command
    while command.strip().casefold() != "back":
        system("cls")
        print("Settings available: \n\n- Difficulty\n")
        print('"Back" to go back\n')
        command = input("Enter a setting to change: ")

        if command.strip().casefold() == "difficulty":
            difficultySetting()

        elif command.strip().casefold() == "back":
            pass

        else:
            badCommand() 

    return difficulty

##Projekti 3
def difficultySetting():
    global difficulty
    global command
    while command.strip().casefold() != "back":
        system("cls")
        print("Current difficulty: " + difficulty)
        print("Difficulty settings: \n\n- Easy \n- Normal \n- Hard\n")
        print('"Back" to go back')
        command = input("Enter a difficulty option: ")
        if command.strip().casefold() == "easy":
            difficulty = "Easy"
        elif command.strip().casefold() == "normal":
            difficulty = "Normal"
        elif command.strip().casefold() == "hard":
            difficulty = "Hard"
        elif command.strip().casefold() == "back":
            pass
        else:
            badCommand()

##Projekti 3
def addItem():
    global item
    while item != "STOP":
        system("cls")
        item = input('Input item to be added (Or "back" to go back): ')
        if item.strip().casefold() == "back":
            break
        else:
            if item != "":
                inventory.append(item)
                print("\nItem added to inventory!\n")
                input('Press any key to continue...')
            else:
                print("\nItem name can not be empty!\n")
                input('Press any key to continue...')

    return item

##Projekti 3
def showInventory():
    system("cls")
    global item
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("The list is empty!")
    input('Press any key to continue...')

def play():
    global command
    while command != "back":
        system("cls")
        print("Available commands: \n\n- Add item \n- Inventory (Show inventory)\n")
        print('"Back" to go back\n')
        command = input("Enter a command: ")
        if command.strip().casefold() == "additem" or command.strip().casefold() == "add item":
            addItem()
        elif command.strip().casefold() == "inventory":
            showInventory()
        else:
            badCommand()

def badCommand():
    system("cls")
    print("Invalid command!")
    input("Press any key to continue...")
    system("cls")

while name == "":
    system("cls")
    print("You can not input an empty name!")
    input("Press any key to continue...")
    system("cls")
    name = input("Enter your name: ")
if name != "":
    ##Projekti 2
    age = input("Enter your age: ")
    while age == "":
        system("cls")
        print("You can not input an empty age!")
        input("Press any key to continue...")
        system("cls")
        age = input("Enter your age: ")
        
    if int(age) < 12:
        system("cls")
        print("The minimum age is 12!")
    else:
        while command.strip().casefold() != "stop" or command.strip().casefold() != "exit" or command.strip().casefold() != "quit":
            system("cls")
            print(r"""

                                             _  _  ____  __     ___  __   _  _  ____ 
                                            / )( \(  __)(  )   / __)/  \ ( \/ )(  __)
                                            \ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) 
                                            (_/\_)(____)\____/ \___)\__/ \_)(_/(____)


                    """)
            print("Available commands: \n\n- Play (play) \n- Settings (settings) \n- Quit (quit, exit, stop)\n")
            command = input("Enter a command: ")
            if command.strip().casefold() == "":
                badCommand()
            elif command.strip().casefold() == "settings":
                settings()
            elif command.strip().casefold() == "play":
                play()
            elif command.strip().casefold() == "stop" or command.strip().casefold() == "exit" or command.strip().casefold() == "quit":
                break
