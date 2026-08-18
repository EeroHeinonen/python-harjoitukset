num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(input("Input the third number: "))

i = 0
numSum = [num1, num2, num3]
product = num1 * num2
product2 = product * num3
total = 0

for i in numSum:
    total += 1

print(total)
mean = (numSum[0] + numSum[1] + numSum[2]) / total

##print(f"The sum of the numbers is: {numSum} \nThe product of the numbers is: {product2} \nThe mean of the numbers is: {mean:10.2f}")