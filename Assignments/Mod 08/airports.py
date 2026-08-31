from os import system

userIn = ""
airportDict = {}

def search():
	global airportICAO
	airportICAO = ""
	while airportICAO == "":
		system("cls")
		airportICAO = input("Enter the ICAO code of the airport: ")
		if airportICAO == "":
			system("cls")
			print("The input value can not be empty!")
			input("Press any key to continue...")

	if airportICAO in airportDict:
		system("cls")
		print(f"The name of the airport with the code {airportICAO} is {airportDict[airportICAO]}")
		input("Press any key to continue...")
	else:
		system("cls")
		airportICAO = ""
		print("The ICAO was not found in the list!")
		input("Press any key to continue...")

def inputFunc():
	system("cls")
	global airportName
	global airportICAO
	airportName = ""
	airportICAO = ""

	while airportName == "":
		system("cls")
		airportName = input("Enter the airport name: ")
		if airportName == "":
			system("cls")
			print("The airport name can not be empty!")
			input("Press any key to continue...")

	while airportICAO == "":
		system("cls")
		airportICAO = input("Enter the airport ICAO: ")
		if airportICAO == "":
			system("cls")
			print("The airport ICAO code can not be empty!")
			input("Press any key to continue...")

	system("cls")
	print("Airport saved!")
	input("Press any key to continue...")

	airportDict.update({airportICAO: airportName})

while userIn != "q":
	system("cls")
	userIn = input("Would you like to search (s), input (i) or quit (q): ")
	if userIn.strip().casefold() == "s":
		search()
	elif userIn.strip().casefold() == "i":
		inputFunc()