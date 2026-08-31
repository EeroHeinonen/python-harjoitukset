command = ""
from os import system
class Car:
    def __init__(self, registryNum, topSpeed, currentSpeed, distanceTraveled):
        self.registryNum = registryNum
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.distanceTraveled = 0

    def accelerate(self, changeInSpeed):
        self.currentSpeed += changeInSpeed
        if self.currentSpeed < 0:
            self.currentSpeed = 0
        elif self.currentSpeed > self.topSpeed:
            self.currentSpeed = self.topSpeed

    def travel(self, time):
        self.distanceTraveled += time * self.currentSpeed

car1 = Car("ABC-123", 142, 0, 0)

def changeSpeed():
    global changeInSpeed
    changeInSpeed = 0
    while changeInSpeed != "q":
        try:
            changeInSpeed = input("\nEnter the change in speed: ")
            car1.accelerate(int(changeInSpeed))
            break
        except ValueError:
            system("cls")
            print("The value must be a number!")
            input("Press any key to continue...")
            system("cls")

def setTimeTraveled():
    global time
    time = 0
    while time != "q":
        try:
            time = input("\nEnter the time to travel in hours: ")
            car1.travel(float(time))
            break
        except ValueError:
            system("cls")
            print("The value must be a number!")
            input("Press any key to continue...")
            system("cls")

while command.strip().casefold() != "q":
    system("cls")
    print(f"\nCar: {car1.registryNum}\nTop speed: {car1.topSpeed} km/h\nCurrent speed: {car1.currentSpeed} km/h\nDistance traveled: {car1.distanceTraveled:.2f} km")
    print("\nAvailable commands: \n- Set the speed (speed)\n- Set the traveled time (time)\n- Quit (q)\n")
    command = input("Enter a command: ")
    if command.strip().casefold() == "speed":
        changeSpeed()
    if command.strip().casefold() == "time":
        setTimeTraveled()
