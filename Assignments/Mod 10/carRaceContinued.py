from os import system
import random
import time

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
command = ""
timeTraveled = 0
winner = ""
raceLen = ""

cars = []

class Racing:
    def __init__(self, raceName, raceLen, participants):
        self.raceName = raceName
        self.raceLen = raceLen
        self.participants = cars

    def race(self):
        global timeTraveled
        for car in self.participants:
            changeInSpeed = random.randint(-10, 15)
            car.accelerate(changeInSpeed)
            car.travel(1)

        timeTraveled += 1

    def printCurrent(self):
        if R.raceOver() == False:
            for car in self.participants:
                print(f"{car.registryNum} has so far traveled for {car.distanceTraveled} km(s) and current speed is {car.currentSpeed}\n")

            input("Press any key to continue...")

    def raceOver(self):
        global winner
        for car in self.participants:
            if car.distanceTraveled >= self.raceLen:
                winner = car.registryNum
                return True
        return False


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
    cars.append(Car(f"{random.choice(letters) + random.choice(letters) + random.choice(letters)}-{str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))}", random.randint(100, 200), 0, 0))
raceName = input("Please input the race name: ")
while raceLen == "":
    system("cls")
    try:
        raceLen = int(input("Please input the length of the race: "))
    except ValueError:
        system("cls")
        print("The value must be a number!")
        input("Press any key to continue...")
else:
    R = Racing(raceName, raceLen, cars)
    while command.strip().casefold() != "q" and R.raceOver() == False:
        system("cls")
        print(f"Race: {raceName}\nLength: {raceLen}\n\n")
        i = 1
        for car in R.participants:
            print(f"Car {i}\nRegistry number: {car.registryNum}\nTop speed: {car.topSpeed}\n")
            i += 1
        print("\nAvailable commands: \n- Race (race)\n- Quit (q)\n")
        command = input(f"Enter a command: ")
        if command.strip().casefold() == "race":
            while timeTraveled < 10:
                R.race()
                R.raceOver()
            else:
                R.printCurrent()
                timeTraveled = 0
    else:
        system("cls")
        print(f"The race is over! {winner} has won!")