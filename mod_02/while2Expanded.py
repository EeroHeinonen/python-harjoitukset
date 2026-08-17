command = input("Input command: ")
while command != "stop":
    if command == "MAYDAY":
        break

    print("Executing command: " + command)
    command = input("Input command: ")

else:
    print("Goodbye!")
    
print("Execution stopped")