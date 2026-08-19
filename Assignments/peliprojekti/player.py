from os import system

name = input("Enter your name: ")
age = int(input("Enter your age: "))
command = ""
difficulty = "Normal"
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
        print("Available commands: \nPlay (play) \nSettings (settings) \nQuit (quit, exit, stop)")
        command = input("Enter a command: ")
        if command == "quit":
            break
        elif command == "settings":
            system("cls")
            print("Settings available: \nDifficulty")
            print('"Back" to go back')
            command = input("Enter a setting to change: ")
            if command == "Difficulty" or command == "difficulty":
                system("cls")
                print("Current difficulty: " + difficulty)
                print("Difficulty settings: \nEasy \nNormal \nHard")
                print('"Back" to go back')
                command = input("Enter a difficulty to change: ")
                if command == "Easy" or command == "easy":
                    difficulty = "Easy"
                elif command == "Normal" or command == "normal":
                    difficulty = "Normal"
                elif command == "Hard" or command == "hard":
                    difficulty = "Hard"
                elif command != "Back" or command != "back":
                    pass

        elif command = "Play" or command == "play":
            system("cls")
            print("Not yet available!")
            ## Game code tba