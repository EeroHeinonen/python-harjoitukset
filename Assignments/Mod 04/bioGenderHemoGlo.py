gender = input("Enter your biological gender M / F: ")
if gender == "M" or gender == "m" or gender == "F" or gender == "f":
    hemoGlo = int(input("Enter your hemoglobin level: "))
    
    if gender == "M" or gender == "m":
        if hemoGlo < 134:
            print("The hemoglobin level is below acceptable limits!")
        elif hemoGlo > 195:
            print("The hemoglobin level is above acceptable limits!")
        elif hemoGlo >= 135 and hemoGlo <= 195:
            print("The hemoglobin level is within acceptable limits.")

    elif gender == "F" or gender == "f":
        if hemoGlo < 117:
            print("The hemoglobin level is below acceptable limits!")
        elif hemoGlo > 175:
            print("The hemoglobin level is above acceptable limits!")
        elif hemoGlo >= 117 and hemoGlo <= 175:
            print("The hemoglobin level is within acceptable limits.")
else:
    print("Invalid input!")