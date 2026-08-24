import random
dice = 0

numOfSides = input("What is the maximum roll? ")

def throwDice(numOfSides):
    dice = random.randint(1,numOfSides)
    return dice

while dice != int(numOfSides):
    dice = throwDice(int(numOfSides))
    print(f"You rolled a {dice}! \n")