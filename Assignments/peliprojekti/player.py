from os import system

name = input("Enter your name: ")
command = ""
difficulty = "Normal"
inventory = []
item = "0"

def settingsFunc():
    global command
    while command.strip().casefold() != "back":
        system("cls")
        print("Settings available: \n\n- Difficulty\n")
        print('"Back" or nothing to go back\n')
        command = input("Enter a setting to change: ")

        if command.strip().casefold() == "difficulty":
            difficultySetting()

        elif command == "":
            system("cls")
            print("Invalid command!")
            input("Press any key to continue...")      

    return difficulty

def difficultySetting():
    global difficulty
    global command
    while command.strip().casefold() != "back":
        system("cls")
        print("Current difficulty: " + difficulty)
        print("Difficulty settings: \n\n- Easy \n- Normal \n- Hard\n")
        print('"Back" to go back')
        command = input("Enter a difficulty to change: ")
        if command.strip().casefold() == "easy":
            difficulty = "Easy"
            break
        elif command.strip().casefold() == "normal":
            difficulty = "Normal"
            break
        elif command.strip().casefold() == "hard":
            difficulty = "Hard"
            break
        elif command.strip().casefold() == "back":
            break
        else:
            system("cls")
            print("Invalid command!\n")
            input('Press any key to continue...')
            system("cls")

def addItem():
    global item
    while item != "BACK":
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
                print("\nInvalid item!\n")

    return item

def showInventory():
    system("cls")
    global item
    for item in inventory:
        print(f"- {item}")
    input('Press any key to continue...')

while name == "":
    system("cls")
    print("You can not input an empty name!")
    input("Press any key to continue...")
    system("cls")
    name = input("Enter your name: ")
    if name != "":
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
                    system("cls")
                    print("Invalid command!")
                    input("Press any key to continue...")
                elif command.strip().casefold() == "settings":
                    settingsFunc()
                elif command.strip().casefold() == "play":
                    system("cls")
                    print("Available commands \n\n- Add item \n- Inventory (Show inventory)\n")
                    command = input("Enter a command: ")
                    if command.strip().casefold() == "additem" or command.strip().casefold() == "add item":
                        addItem()
                    elif command.strip().casefold() == "inventory":
                        showInventory()
                    ## Game code tba
                    else:
                        system("cls")
                        print("Invalid command!")
                        input("Press any key to continue...")
                else:
                    break
