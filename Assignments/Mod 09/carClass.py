class Car:
    def __init__(self, registryNum, topSpeed, currentSpeed, distanceTraveled):
        self.registryNum = registryNum
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.distanceTraveled = 0

car1 = Car("ABC-123", 142, 0, 0)

print(f"Auton {car1.registryNum} huippunopeus on {car1.topSpeed}, tämänhetkinen nopeus on {car1.currentSpeed} ja kuljettu matka on {car1.distanceTraveled}")