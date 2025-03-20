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

# def display(st):
#     def show():
#         return "show function "
#     result = show() + st + " display function"
#     return result

# print(display("Hello"))

#.............................................................................

# def positionalArgs(a,b,c):
#     print(a,b,c)

# positionalArgs(10,20,30)

#.............................................................................

# def keywordArgs(a,b,c):
#     print(a,b,c)

# keywordArgs(c=30,a=10,b=20)

#.............................................................................

def defaultArgs(a,b,c=30):
    print(a,b,c)

defaultArgs(10,20)
defaultArgs(10,20,40)