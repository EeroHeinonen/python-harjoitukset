import math
from os import system
userIn = ""
price = ""
amount = ""
i = 0
p = 0

pizzaList = []

def calculate(userIn, price):
    
    pizzaArea = math.pi * ((userIn / 100) / 2) ** 2
    pizzaCalc = price / pizzaArea
    return pizzaCalc

while amount == "":
    system("cls")
    try:
        amount = int(input("Input the amount of pizzas to compare: "))
        if amount <= 1:
            system("cls")
            print("The amount must be greater than 1!")
            input("Press any key to continue...")
            amount = ""
    except :
        system("cls")
        print("The value is not a number!")
        input("Press any key to continue...")
        amount = ""

else:
    while i < amount:
        try:
            system("cls")
            userIn = float(input(f"Input the diameter of pizza {i + 1} in cm: "))

            try:
                system("cls")
                price = float(input(f"Input the price of pizza {i + 1} in €: "))

                if userIn != "" and price != "":
                    pizza = calculate(userIn, price)
                    pizzaList.append(pizza)
                    i += 1

            except:
                system("cls")
                price = ""
                print("Value is not a number!")
                input("Press any key to continue...")
                system("cls")

        except:
            system("cls")
            userIn = ""
            print("Value is not a number!")
            input("Press any key to continue...")
            system("cls")

    else:
        c = p + 1
        cheapest = pizzaList[p]
        try:
            for pizza in pizzaList:
                try:
                    if pizzaList[p] <= cheapest:
                        cheapest = pizzaList[p]
                        c = p + 1
                    else:
                        cheapest = cheapest
                except :
                    pass
            
                print(pizza)
                p += 1

            print(f"Pizza no. {c} is the best deal at {cheapest:2.2f} €/m²!")

        except :
            pass