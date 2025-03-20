a={

}

n=int(input("Enter the number of elements: "))

for i in range(n):
    key=int(input("Enter the key: "))
    value=input("Enter the value: ")
    # a[key]=value
    a.update({key:value})

print(a)