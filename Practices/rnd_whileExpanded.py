import random

repeats = 0
tossesTotal = 0
while repeats < 100000:
    dice1 = dice2 = tosses = 0
    while (dice1 != 6 or dice2 != 6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        tosses += 1
##print(f"It required {tosses:d} tosses.")
    repeats += 1
    tossesTotal = tossesTotal + tosses

averageTosses = tossesTotal / repeats
print(f"Average tosses: {averageTosses:5.3f}")