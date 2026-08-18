size = int(input("Enter the size of the pike perch in centimeters: "))

sizeLimit = 37 - size

if size < 37:
    print(f"The fish is undersized! \n\nIt needs to be {sizeLimit} centimeter(s) longer, back into the lake it goes!")
else:
    print("The fish is of legal size!")