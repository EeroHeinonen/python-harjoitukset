numList = []
userIn = 1
total = 0

def calculate(numList):
    total = 0
    for num in numList:
        total = num + total
    return total

while userIn != "":
    userIn = input("\nEnter a number:")
    if userIn == "":
        pass
    else:
        numList.append(int(userIn))
        total = calculate(numList)

else:
    print(f"\n{total}")