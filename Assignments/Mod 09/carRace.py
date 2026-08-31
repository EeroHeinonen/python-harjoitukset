from os import system
import random
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
command = ""

cars = []

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

for i in range(10):
    cars.append(Car(f"{random.choice(letters) + random.choice(letters) + random.choice(letters)}-{str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))}", random.randint(100, 200), 0, 0))

def race():
    i = 0
    for car in cars:
        if cars[i].distanceTraveled >= 100:
            system("cls")
            print(f"{cars[i].registryNum} won the race!")
            break

        changeInSpeed = random.randint(-10, 15)
        cars[i].accelerate(changeInSpeed)
        cars[i].travel(1)

        if changeInSpeed < 0:
            changed = "slowed down"
            changedSpeed = str(changeInSpeed)[1:]
        else:
            changed = "sped up"
            changedSpeed = changeInSpeed

        print(f"{cars[i].registryNum} {changed} by {changedSpeed} km/h, their current speed is {cars[i].currentSpeed} km/h and they have so far traveled for {cars[i].distanceTraveled} km(s)\n")
        i += 1

    input("Press any key to continue...")

while command.strip().casefold() != "q":
    system("cls")
    i = 0
    for car in cars:
        print(f"{cars[i].registryNum} Top speed: {cars[i].topSpeed}")
        i += 1
    print("\nAvailable commands: \n- Race (race)\n- Quit (q)\n")
    command = input("Enter a command: ")
    if command.strip().casefold() == "race":
        race()
