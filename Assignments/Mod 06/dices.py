import random
rollTotal = 0

numDice = int(input("Enter the number of dice to roll: "))

for i in range(numDice):
    roll = random.randint(1, 6)
    rollTotal = roll + rollTotal    
    ##print(roll)

print(rollTotal)