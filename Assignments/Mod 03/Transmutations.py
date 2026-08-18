import math

talent = float(input("Input the number of talents: "))
nails = float(input("Input the number of nails: "))
bullets = float(input("Input the number of bullets: "))

totalTalent = talent * 8512
totalNails = nails * 425.6
totalBullets = bullets * 13.3

totalKg = math.trunc((totalTalent + totalNails + totalBullets) / 1000)
totalG = (totalTalent + totalNails + totalBullets) % 1000
print(f"Total weight: {totalKg} kilograms and {totalG} grams.")