from os import system

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

    def moveDown(self):
        self.currentFloor -= 1

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
                print(f'The value must be lower than the highest floor! ("{highestFloor}")')
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

        while targetFloor != "q":
            system("cls")
            print('Enter "quit / q" to quit')
            print(f"The current floor of the elevator is: {elev.currentFloor}")

            targetFloor = input("Enter the target floor: ")

            try:
                if int(targetFloor) > elev.highestFloor:
                    system("cls")
                    print(f"Value is too high, the highest floor is {elev.highestFloor}!")
                    input("Press any key to continue...")
                elif int(targetFloor) < elev.lowestFloor:
                    system("cls")
                    print(f"Value is too low, the lowest floor is {elev.lowestFloor}!")
                    input("Press any key to continue...")
                elif int(targetFloor) == elev.currentFloor:
                    system("cls")
                    print(f"The elevator is already on floor {elev.currentFloor}!")
                    input("Press any key to continue...")
                elif elev.currentFloor > int(targetFloor):
                    while elev.currentFloor > int(targetFloor):
                        elev.moveDown()
                    print(f"Elevator has reached the target floor {int(targetFloor)}!")
                    input("Press any key to continue...")
                elif elev.currentFloor < int(targetFloor):
                    while elev.currentFloor < int(targetFloor):
                        elev.moveUp()
                    print(f"Elevator has reached the target floor {int(targetFloor)}!")
                    input("Press any key to continue...")
            except :
                if targetFloor.strip().casefold() == "q" or targetFloor.strip().casefold() == "quit":
                    pass
                else:
                    system("cls")
                    print("The value is not a number!")
                    input("Press any key to continue...")
