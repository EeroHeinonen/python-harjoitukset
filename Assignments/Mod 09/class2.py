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

# while changeInSpeed != "q":
#     changeInSpeed = input("Enter the change in speed:")
#     car1.accelerate(int(changeInSpeed))
#     print(f"Auton {car1.registryNum} huippunopeus on {car1.topSpeed}, tämänhetkinen nopeus on {car1.currentSpeed} ja kuljettu matka on {car1.distanceTraveled}")


print(f"Auton {car1.registryNum} huippunopeus on {car1.topSpeed}, tämänhetkinen nopeus on {car1.currentSpeed} ja kuljettu matka on {car1.distanceTraveled}")
input("Press any key to continue...")
car1.accelerate(30)
print(f"Auton tämänhetkinen nopeus on: {car1.currentSpeed}")
input("Press any key to continue...")
car1.accelerate(70)
print(f"Auton tämänhetkinen nopeus on: {car1.currentSpeed}")
input("Press any key to continue...")
car1.accelerate(50)
print(f"Auton tämänhetkinen nopeus on: {car1.currentSpeed}")
input("Press any key to continue...")
car1.accelerate(-200)
print(f"Auton tämänhetkinen nopeus on: {car1.currentSpeed}")