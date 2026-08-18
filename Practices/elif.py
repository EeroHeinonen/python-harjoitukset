age = int(input("Input your age: "))
if age >= 65:
    print("You're at retirement age.")
elif age >= 18:
    print("You're at working age.")
elif age >= 7:
    print("You're at school age.")
else:
    print("You're a young child.")