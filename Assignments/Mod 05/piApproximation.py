import math
import random

minP = float(-1)
maxP = float(1)
pointsInside = 0
points = 0

userIn = int(input("Enter the number of points to generate: "))

while points <= userIn:
	pointX = random.uniform(minP, maxP)
	pointY = random.uniform(minP, maxP)
	if pointX ** 2 + pointY ** 2 < 1:
		pointsInside += 1

	points += 1

piApprox = (4 * pointsInside / points)

print (f"The approximation of pi is: {piApprox}")


