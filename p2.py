def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Request input from the user
num = int(input("Enter a number: "))

# Check if the input is positive
if num < 0:
    print("Factorial for negative numbers does not exist.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    result = factorial(num)
    print("The factorial of", num, "is", result)
