def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

x = int(input("Enter a number: "))
y = factorial(x)
print(f"Factorial of {x} is: {y}")