"""
Task 2: Implement user input to receive numbers and an operation choice.
"""

def numbers():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    return x, y

def operation():
    operation = input("Enter an operation (+, -, *, /): ")
    return operation

def calculate(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y
    else:
        return "Invalid operation. Please enter a valid operation."

x, y = numbers()
operation = operation()
result = calculate(x, y, operation)

print(f"The result is {result}")