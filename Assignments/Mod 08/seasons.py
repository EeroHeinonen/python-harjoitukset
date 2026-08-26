from os import system


season = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "fall", "fall", "fall", "winter")
x = False

while x == False:
    try:
        system("cls")
        userIn = int(input("Enter index of month: "))
        month = season[userIn - 1]
        print(f"The {userIn}. month is in {month}")
        x = True
    except ValueError:
        system("cls")
        print(f"Please enter a number!")
        input("Press any key to continue...")
        x = False