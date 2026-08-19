num = input("Enter a number: ")
lowNum = int(num)
highNum = int(num)
while num != "":
    if int(num) < lowNum:
        lowNum = int(num)
    elif int(num) > highNum:
        highNum = int(num)
    num = input("Enter another number: ")

else:
    print(lowNum, highNum)