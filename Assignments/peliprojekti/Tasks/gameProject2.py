name = input("Input your name: ")
age = int(input("\nInput your age: "))
command = ""
if age < 12:
    print("The minimum age is 12!")
else:
    while command != "quit":
        print(f"\nHello {name}, welcome to the game!\n")
        print("Please input a command: \n\nAvailable commands: \n- play \n- settings \n- quit\n")
        command = input("Enter a command: ")
        if command == "play":
            print("The game will be added here in the future!")
            input("Press any key to continue...")
        elif command == "settings":
            print("This is the settings menu, there is nothing here yet.")
            input("Press any key to continue...")
        elif command == "quit":
            command = input("Are you sure? (y/n): ")
            if command == "y":
                print("\nGoodbye!\n")
                break
            elif command == "n":
                pass