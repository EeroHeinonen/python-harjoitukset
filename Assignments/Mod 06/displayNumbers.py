from webbrowser import Elinks


numList = []
userIn = 0

while userIn != "":
	userIn = input("Enter a number: ")
	if userIn == "":
		pass
	elif userIn != "":
		numList.append(int(userIn))
numList.sort(reverse = True)
print(numList)