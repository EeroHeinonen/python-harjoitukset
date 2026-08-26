nameSet = set()
userIn = "0"
prevIn = ""

while userIn != "":
    userIn = input("Please enter a name: ")
    if userIn in nameSet:
        print("Name already added!\n")
    elif userIn == "":
        pass
    else:
        nameSet.add(userIn)
        print("New name!\n")

else:
    for name in nameSet:
        print(f"\n- {name}")
        print("")