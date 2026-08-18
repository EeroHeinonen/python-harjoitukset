inches = 0
while inches >= 0:
    inches = float(input("Enter the value: "))
    centimeters = inches * 2.54
    if inches >= 0:
        print(f"{inches} inches is {centimeters} centimeters!")
    else:
        print("Not a positive value!")