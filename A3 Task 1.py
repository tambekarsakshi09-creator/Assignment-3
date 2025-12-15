# Function to calculate factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Taking input from the user
number = int(input("Enter a number: "))

# Calling the function and printing the result
result = factorial(number)
print("Factorial of", number, "is", result)
