from multiprocessing import Value
from os import system
import time
import random

highestFloor = ""
lowestFloor = ""
targetFloor = ""
targetElev = ""
currentFloor = ""
numOfElev = ""
chanceOfFire = 0

class House:
    def __init__(self, numOfElev, highestFloor, lowestFloor, targetElev):
        self.highestFloor = highestFloor
        self.lowestFloor = lowestFloor
        self.numOfElev = numOfElev
        self.targetElev = targetElev
        self.elevList = []

    def fireAlarm(self):
        system("cls")
        print("Fire alarm! All elevators called to the bottom floor!")
        i = 0
        for elev in house.elevList:
            while house.elevList[i].currentFloor > house.lowestFloor:
                house.elevList[i].moveDown()
            i += 1
        input("Press any key to continue...")

class Elevator:
    def __init__(self, currentFloor):
        self.currentFloor = lowestFloor

    def moveUp(self):
        print(f"Rising...\nElevator is currently at floor {self.currentFloor}.\n")
        self.currentFloor += 1
        time.sleep(1)

    def moveDown(self):
        global e
        print(f"Lowering...\nElevator is currently at floor {self.currentFloor}.\n")
        self.currentFloor -= 1
        time.sleep(1)
while numOfElev == "":
    system("cls")
    try:
        numOfElev = int(input("Enter the number of elevators in the house: "))
        if numOfElev <= 0:
            system("cls")
            print(f"The value must be higher than 0!")
            input("Press any key to continue...")
            numOfElev = ""

    except ValueError:
        system("cls")
        print("The value must be a number!")
        input("Press any key to continue...")

else:

    while highestFloor == "":
        system("cls")
        try:
            highestFloor = int(input("Enter the highest floor for the elevator: "))
            if highestFloor <= 0:
                system("cls")
                print(f"The value must be higher than 0!")
                input("Press any key to continue...")
                highestFloor = ""

        except ValueError:
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

            except ValueError:
                system("cls")
                print("The value must be a number!")
                input("Press any key to continue...")

        else:

            house = House(numOfElev, highestFloor, lowestFloor, targetElev)
            for i in range(numOfElev):
                elev = Elevator(currentFloor)
                house.elevList.append(elev)
                i += 1

            while targetElev.strip().casefold() != "q":
                system("cls")
                targetFloor = ""
                e = 1
                for elev in house.elevList:
                    print(f"The current floor of elevator {e} is: {house.elevList[e - 1].currentFloor}")
                    e += 1

                try:
                    targetElev = input('\nEnter target elevator, "f" to pull the fire alarm or "q" / "quit" to quit: ')
                    house.targetElev = targetElev

                    if targetElev.strip().casefold() == "f":
                        house.fireAlarm()

                    elif int(targetElev) <= 0:
                        raise IndexError

                    try:
                        eg = house.elevList[int(targetElev) - 1]

                        while targetFloor.strip().casefold() != "b":
                            system("cls")
                            e = 1
                            for elev in house.elevList:
                                print(f"The current floor of elevator {e} is: {house.elevList[e - 1].currentFloor}")
                                e += 1

                            print('\nAvailable commands:\n- Up\n- Down\n- Target floor\n- "b" or "back" to go back\n')
                            targetFloor = input("Enter command or target floor: ")

                            try:
                                chanceOfFire = random.randint(0,10)

                                if chanceOfFire == 1:
                                    house.fireAlarm()
                                    break

                                elif targetFloor.strip().casefold() == "up":
                                    system("cls")
                                    if house.elevList[int(targetElev) - 1].currentFloor == house.highestFloor:
                                        print(f'The elevator can not move past the highest floor "({house.highestFloor})"!')
                                        input("Press any key to continue...")
                                    else:
                                        house.elevList[int(targetElev) - 1].moveUp()
                                        print(f"Elevator {int(targetElev)} has reached floor {int(targetFloor)}!")
                                        input("Press any key to continue...")

                                elif targetFloor.strip().casefold() == "down":
                                    system("cls")
                                    if house.elevList[int(targetElev) - 1].currentFloor == house.lowestFloor:
                                        print(f'The elevator can not move past the lowest floor ("{house.lowestFloor}")!')
                                        input("Press any key to continue...")
                                    else:
                                        house.elevList[int(targetElev) - 1].moveDown()
                                        print(f"Elevator {int(targetElev)} has reached floor {int(targetFloor)}!")
                                        input("Press any key to continue...")

                                elif int(targetFloor) > house.highestFloor:
                                    system("cls")
                                    print(f"Value is too high, the highest floor is {house.highestFloor}!")
                                    input("Press any key to continue...")
                                    targetFloor = ""

                                elif int(targetFloor) < house.lowestFloor:
                                    system("cls")
                                    print(f"Value is too low, the lowest floor is {house.lowestFloor}!")
                                    input("Press any key to continue...")
                                    targetFloor = ""

                                elif int(targetFloor) == house.elevList[int(targetElev) - 1].currentFloor:
                                    system("cls")
                                    print(f"Elevator {house.targetElev} is already on floor {house.elevList[int(targetElev) - 1].currentFloor}!")
                                    input("Press any key to continue...")
                                    targetFloor = ""

                                elif house.elevList[int(targetElev) - 1].currentFloor > int(targetFloor):
                                    system("cls")
                                    while house.elevList[int(targetElev) - 1].currentFloor > int(targetFloor):
                                        house.elevList[int(targetElev) - 1].moveDown()
                                    print(f"Elevator {int(targetElev)} has reached floor {int(targetFloor)}!")
                                    input("Press any key to continue...")

                                elif house.elevList[int(targetElev) - 1].currentFloor < int(targetFloor):
                                    system("cls")
                                    while house.elevList[int(targetElev) - 1].currentFloor < int(targetFloor):
                                        house.elevList[int(targetElev) - 1].moveUp()
                                    print(f"Elevator {int(targetElev)} has reached floor {int(targetFloor)}!")
                                    input("Press any key to continue...")

                            except ValueError:
                                if targetFloor.strip().casefold() == "b" or targetFloor.strip().casefold() == "back":
                                    break
                                else:
                                    if targetFloor.strip().casefold() == "down" or targetFloor.strip().casefold() == "up":
                                        pass
                                    else:
                                        system("cls")
                                        print("The command is not valid!")
                                        input("Press any key to continue...")

                    except IndexError:

                        system("cls")
                        print("The target elevator can not be outside the range of the number of elevators!")
                        input("Press any key to continue...")
                        targetElev = ""
                except IndexError:

                    system("cls")
                    print("The target elevator can not be outside the range of the number of elevators!")
                    input("Press any key to continue...")
                    targetElev = ""

                except ValueError:
                        if targetElev.strip().casefold() == "q" or targetElev.strip().casefold() == "quit":
                            system("cls")
                            print("Goodbye!")
                            targetElev = "q"

                        elif targetElev.strip().casefold() == "f" or targetElev.strip().casefold() == "fire":
                            pass
                            targetElev = ""

                        else:
                            system("cls")
                            print("The value must be a number!")
                            input("Press any key to continue...")
                            targetElev = ""