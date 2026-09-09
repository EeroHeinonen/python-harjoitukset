from os import system
import time

highestFloor = ""
lowestFloor = ""
targetFloor = ""

class Elevator:
    def __init__(self, currentFloor, highestFloor, lowestFloor):
        self.currentFloor = lowestFloor
        self.highestFloor = highestFloor
        self.lowestFloor = lowestFloor

    def moveUp(self):
        self.currentFloor += 1
        print("Rising...\n")
        time.sleep(0.75)

    def moveDown(self):
        self.currentFloor -= 1
        print("Lowering...\n")
        time.sleep(0.75)

while highestFloor == "":
    system("cls")
    try:
        highestFloor = int(input("Enter the highest floor for the elevator: "))
        if highestFloor <= 0:
            system("cls")
            print(f"The value must be higher than 0!")
            input("Press any key to continue...")
            highestFloor = ""
    except :
        system("cls")
        print("The value must be a number!")
        input("Press any key to continue...")

else:
    while lowestFloor == "":
        system("cls")
        try:
            lowestFloor = int(input("Enter the lowest floor for the elevator: "))
            if lowestFloor >= highestFloor:
                system("cls")
                print(f'The value must be lower than the highest floor ("{highestFloor}")!')
                input("Press any key to continue...")
                lowestFloor = ""
            elif lowestFloor >= 1:
                system("cls")
                print(f"The value must be lower than 1!")
                input("Press any key to continue...")
                lowestFloor = ""

        except :
            system("cls")
            print("The value must be a number!")
            input("Press any key to continue...")

    else:

        elev = Elevator(lowestFloor, highestFloor, lowestFloor)

        while targetFloor.strip().casefold() != "q":
            system("cls")
            print(f"The current floor of the elevator is: {elev.currentFloor}")
            print('\nAvailable commands:\n- Up\n- Down\n- Target floor\n- "q" to quit\n')

            targetFloor = input("Enter command or target floor: ")

            try:
                if targetFloor.strip().casefold() == "up":
                    system("cls")
                    if elev.currentFloor == highestFloor:
                        print(f'The elevator can not move past the highest floor "({highestFloor})"!')
                        input("Press any key to continue...")
                    else:
                        elev.moveUp()
                        print(f"Elevator has reached floor {elev.currentFloor}!")
                        input("Press any key to continue...")

                elif targetFloor.strip().casefold() == "down":
                    system("cls")
                    if elev.currentFloor == lowestFloor:
                        print(f'The elevator can not move past the lowest floor ("{lowestFloor}")!')
                        input("Press any key to continue...")
                    else:
                        elev.moveDown()
                        print(f"Elevator has reached floor {elev.currentFloor}!")
                        input("Press any key to continue...")

                elif int(targetFloor) > elev.highestFloor:
                    system("cls")
                    print(f"Value is too high, the highest floor is {elev.highestFloor}!")
                    input("Press any key to continue...")
                    targetFloor = ""

                elif int(targetFloor) < elev.lowestFloor:
                    system("cls")
                    print(f"Value is too low, the lowest floor is {elev.lowestFloor}!")
                    input("Press any key to continue...")
                    targetFloor = ""

                elif int(targetFloor) == elev.currentFloor:
                    system("cls")
                    print(f"The elevator is already on floor {elev.currentFloor}!")
                    input("Press any key to continue...")
                    targetFloor = ""

                elif elev.currentFloor > int(targetFloor):
                    system("cls")
                    while elev.currentFloor > int(targetFloor):
                        elev.moveDown()
                    print(f"Elevator has reached floor {int(targetFloor)}!")
                    input("Press any key to continue...")

                elif elev.currentFloor < int(targetFloor):
                    system("cls")
                    while elev.currentFloor < int(targetFloor):
                        elev.moveUp()
                    print(f"Elevator has reached floor {int(targetFloor)}!")
                    input("Press any key to continue...")

            except :
                if targetFloor.strip().casefold() == "q":
                    system("cls")
                    print("Goodbye!")

                else:
                    system("cls")
                    print("The command is not valid!")
                    input("Press any key to continue...")