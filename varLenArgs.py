# def VariableLengthArgs(*args):
#     z=args[0]+args[1]+args[2]
#     print("Sum of the numbers is: ",z," and the string is: ",args
# [3])
# VariableLengthArgs(10,20,30,"Hello") 

#.............................................................................

# def kaywordVariableLengthArgs(**kwargs):
#     print(kwargs)
#     print(kwargs['a'],kwargs['b'],kwargs['c'],kwargs['d'])
#     print(kwargs['a']+kwargs['b']+kwargs['c']+kwargs['d'])
# kaywordVariableLengthArgs(a=10,b=20,c=30,d=40)

#.............................................................................

# local variable

def localVariable():
    x = 10
    print("Local variable: ",x)
localVariable()

#.............................................................................

# global variable

y = 20
def globalVariable():
    print("Global variable: ",y)
globalVariable()
#.............................................................................    