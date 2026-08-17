age = int(input("Input age:"))
notAllowed = "Medicine usage is not allowed."
if 15 <= age < 18:
    weight = float(input("Input weight (kg): "))
    if (age >= 18 or age >= 15 and weight >= 55):
        print("Medicine usage is allowed.")
    else:
        print(notAllowed)
else:
    print(notAllowed)