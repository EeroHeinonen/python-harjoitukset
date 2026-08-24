import random
dice = 0

def throwDice():
    dice = random.randint(1,6)
    return dice

while dice != 6:
    dice = throwDice()
    print(f"You rolled a {dice}! \n")