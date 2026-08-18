cabin = input("Enter the size of the cabin type: ")

if cabin == "LUX" or cabin == "lux":
    print("The LUX is a cabin with a balcony on the upper deck.")
elif cabin == "A" or cabin == "a":
    print("The A cabin is a windowed cabin above the car deck.")
elif cabin == "B" or cabin == "b":
    print("The B cabin is a windowless cabin above the car deck.")
elif cabin == "C" or cabin == "c":
    print("The C cabin is a windowless cabin below the car deck.")
else:
    print("Invalid cabin type!")