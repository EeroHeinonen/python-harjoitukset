fahrInput = input("Input temperature in Fahrenheit: ")
fahrNum = float(fahrInput)
cels = (fahrNum - 32) * 5 / 9
print(f"Temperature in celsius: {cels:5.3f}")