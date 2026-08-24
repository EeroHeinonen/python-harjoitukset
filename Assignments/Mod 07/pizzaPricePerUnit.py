import math
userIn = 0

def calculate(userIn, price):
    
    pizzaArea = math.pi * (userIn / 2) ** 2
    pizzaCalc = price / pizzaArea
    return pizzaCalc

userIn = input("Input the diameter of the first pizza: ")
price = input("Input the price of the first pizza: ")
pizzaOne = calculate(int(userIn), int(price))

userIn = input("Input the diameter of the second pizza: ")
price = input("Input the price of the second pizza: ")
pizzaTwo = calculate(int(userIn), int(price))

if pizzaOne < pizzaTwo:
    print(f"The first pizza is a better deal at {pizzaOne:2.3f} €/m²!")
    
else:
    print(f"The second pizza is a better deal at {pizzaTwo:2.3f} €/m²!")