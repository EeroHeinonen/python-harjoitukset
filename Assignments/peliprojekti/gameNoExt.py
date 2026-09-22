from os import system
from Modules import settingsMenu, badCommand, play

##Projekti 1
name = input("Enter your name: ")
age = ""
system("cls")
command = ""

while name == "":
    system("cls")
    print("You can not input an empty name!")
    input("Press any key to continue...")
    system("cls")
    name = input("Enter your name: ")
else:
    ##Projekti 2
    while age == "":
        try:
            system("cls")
            age = int(input("Enter your age: "))
        except ValueError:
            system("cls")
            print("You can not input an age that is not a number.")
            input("Press any key to continue...")
            age = ""
        else:
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
                    print("Available commands: \n\n- Play (play) \n- Settings (settings) \n- Quit (quit, exit, stop, q)\n")
                    command = input("Enter a command: ")
                    if command.strip().casefold() == "settings":
                        settingsMenu()
                    elif command.strip().casefold() == "play":
                        play()
                    elif command.strip().casefold() == "stop" or command.strip().casefold() == "exit" or command.strip().casefold() == "quit" or command.strip().casefold() == "q":
                        break
                    elif command.strip().casefold() != "" or command.strip().casefold() != "settings" or command.strip().casefold() != "play" or command.strip().casefold() != "stop" or command.strip().casefold() != "exit" or command.strip().casefold() != "quit":
                        badCommand()
