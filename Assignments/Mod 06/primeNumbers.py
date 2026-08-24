num = int(input("Enter a number: "))

if num <= 1:
    print("The number is not a prime.")
else:
    prime = True

    ##Code snippet found on "geeksforgeeks.org" and modified.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            print("The number is not a prime.")
            break
    if prime == True:
        print("The number is a prime.")






