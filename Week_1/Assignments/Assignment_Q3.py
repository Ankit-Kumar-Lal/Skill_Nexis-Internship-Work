# Even/Odd & Prime Number Checker

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if n < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")
