numList = []
numListOrg = []
userIn = 0

def oddOut(numList):
    for num in numList:
        if num % 2:
            numList.remove(num)
    return numList

while userIn != "":
    userIn = input("\nEnter a number: ")
    if userIn == "":
        pass
    else:
        numList.append(int(userIn))
        numListOrg.append(int(userIn))
        numList = oddOut(numList)

else:
    print(f"\nThe original list is: {numListOrg}\nThe modified list is: {numList}\n")