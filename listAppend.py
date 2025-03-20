a = []

n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    a.append(int(input("Enter the element: ")))

# print("The list is: ",a)
# print("The length of the list is: ",len(a))



for elements in dir(a):
    if "__" in elements:
        pass
    else:
        print(elements)

print("..........................string elements are from here................")
str = "length of the list is"

for elements in dir(str):
    if "__" in elements:
        pass
    else:
        print(elements)