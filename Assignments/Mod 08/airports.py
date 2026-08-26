from os import system

userIn = ""
airportDict = {}

def search():
	system("cls")
	airportICAO = input("Enter the ICAO code of the airport: ")
	system("cls")
	print(f"The name of the airport with the code {airportICAO} is {airportDict[airportICAO]}")
	input("Press any key to continue...")

def inputFunc():
	system("cls")
	airportName = input("Enter the airport name: ")
	airportICAO = input("Enter the ICAO code of the airport: ")
	airportDict.update({airportICAO: airportName})

while userIn != "q":
	system("cls")
	userIn = input("Would you like to search (s), input (i) or quit (q): ")
	if userIn.strip().casefold() == "s":
		search()
	elif userIn.strip().casefold() == "i":
		inputFunc()