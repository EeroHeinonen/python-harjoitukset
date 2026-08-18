import random

guess = 0
correct = random.randint(1,10)

while guess != correct:
	guess = int(input("Guess a number between 1 and 10: "))
	if guess < correct:
		print ("The correct number is higher!")
	elif guess > correct:
		print("The correct number is lower!")
	elif guess == correct:
		print("You guessed the number correctly!")