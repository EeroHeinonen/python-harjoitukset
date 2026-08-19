attempts = 0

while attempts <= 4:

	user = input("Enter username: ")
	password = input("Enter password: ")

	if user == "python" and password == "rules":
		print("Welcome!")
		break

	elif user != "python" and password != "rules":
		print("Invalid username and password!")
		attempts += 1

	elif user != "python":
		print("Invalid username!")
		attempts += 1

	elif password != "rules":
		print("Invalid password")
		attempts += 1

else:
	print("Access denied!")