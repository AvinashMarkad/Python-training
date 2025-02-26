def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def calculator(operator, a, b):
    switch = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    func = switch.get(operator, lambda a, b: "Invalid operator")
    return func(a, b)

# Example usage
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

result = calculator(operator, a, b)
print("Result:", result)
