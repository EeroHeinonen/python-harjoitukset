changeInSpeed = ""
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

car1 = Car("ABC-123", 142, 0, 0)

while changeInSpeed != "q":
    changeInSpeed = input("Enter the change in speed:")
    car1.accelerate(int(changeInSpeed))
    print(f"Auton {car1.registryNum} huippunopeus on {car1.topSpeed}, tämänhetkinen nopeus on {car1.currentSpeed} ja kuljettu matka on {car1.distanceTraveled}")
    print(f"")