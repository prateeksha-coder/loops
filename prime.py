n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime number")
else:
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")
