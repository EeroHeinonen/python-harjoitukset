command = ""
changeInSpeed = 0
time = 0
distanceTraveled = 0
from os import system
class Car:
    def __init__(self, registryNum, topSpeed, speed, distance, time, usage):
        self.registryNum = registryNum
        self.topSpeed = topSpeed
        self.speed = 0
        self.distance = 0
        self.time = 0

class Electric(Car):
    def __init__(self, registryNum, topSpeed, batteryCapacity, speed, distance, time, usage):
        super().__init__(registryNum, topSpeed, speed, distance, time, usage)
        self.batteryCapacity = batteryCapacity
        self.usage = usage

class Gas(Car):
    def __init__(self, registryNum, topSpeed, tankCapacity, speed, distance, time, usage):
        super().__init__(registryNum, topSpeed, speed, distance, time, usage)
        self.tankCapacity = tankCapacity
        self.usage = usage

cars = []
cars.append(Electric("ABC-123", 180, 52.5, 0, 0, 0, 12.7))
cars.append(Gas("ACD-123", 165, 32.3, 0, 0, 0, 5.3))

def travel():
    for car in cars:
        if issubclass(type(car), Electric):
            if car.batteryCapacity <= 0:
                car.batteryCapacity = 0
                car.distance = car.distance
            else:
                car.batteryCapacity -= (car.usage / 100) * (car.time * car.speed)
                car.distance += car.time * car.speed
        elif issubclass(type(car), Gas):
            if car.tankCapacity <= 0:
                car.tankCapacity = 0
                car.distance = car.distance
            else:
                car.tankCapacity -= (car.usage / 100) * (car.time * car.speed)
                car.distance += car.time * car.speed
        

def changeSpeed():
    i = 1
    for car in cars:
        try:
            changeInSpeed = int(input(f"\nEnter the change in speed for car {i}: "))
            car.speed = car.speed + changeInSpeed
        except ValueError:
            system("cls")
            print("The value must be a number!")
            input("Press any key to continue...")
        i += 1

def setTimeTraveled():
    i = 1
    for car in cars:
        try:
            time = float(input(f"\nEnter the time to travel in hours for car {i}: "))
            car.time = time
        except ValueError:
            system("cls")
            print("The value must be a number!")
            input("Press any key to continue...")
        i += 1

    travel()

while command.strip().casefold() != "q":
    system("cls")
    for car in cars:
        if issubclass(type(car), Gas):
            print(f"Car: {car.registryNum}\nSpeed: {car.speed} km/h\nTop speed: {car.topSpeed} km/h\nDistance traveled: {car.distance} km\nUsage: {car.usage} l/100 km\nCapacity: {car.tankCapacity:.2f} l\n")
        elif issubclass(type(car), Electric):
            print(f"Car: {car.registryNum}\nSpeed: {car.speed} km/h\nTop speed: {car.topSpeed} km/h\nDistance traveled: {car.distance} km\nUsage: {car.usage} kWh/100 km\nCapacity: {car.batteryCapacity:.2f} kWh\n")
    print("\nAvailable commands: \n- Set the speed (speed)\n- Set the traveled time (time)\n- Quit (q)\n")
    command = input("Enter a command: ")
    if command.strip().casefold() == "speed":
        changeSpeed()
    if command.strip().casefold() == "time":
        setTimeTraveled()