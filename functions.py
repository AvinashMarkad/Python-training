# def add(y):
#     print("Addition of two numbers")
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     return a+b+y

# print(add(20))
# sum = add(20)
# print(sum)

#.............................................................................

# def display():
#     def show():
#         return "show function"
#     result = show() + " display function"
#     return result

# print(display())

#.............................................................................

def display(st):
    def show():
        return "show function "
    result = show() + st + " display function"
    return result

print(display("Hello"))

#.............................................................................

