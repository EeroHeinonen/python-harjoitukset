litres = 0
gallons = 0

def convert(gallons):
	if gallons == "":
		return
	else:
		litres = float(gallons) * 3.785
		return litres

while str(gallons) != "":
	gallons = input("Input amount in gallons to convert: ")
	litres = convert(gallons)
	if gallons == "":
		print("Invalid input!")
	elif float(gallons) <= 0:
		print("The value must be greater than zero! \n")
		break
	else:
		print(f"{gallons} gallons is {litres:3.2f} litres! \n")
