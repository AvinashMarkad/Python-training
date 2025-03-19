list1 = [1,"avinash",2,"kumar",3,"singh"]

n=len(list1)
print("length of the list is",n)
for i in range(n):
    print(i,"=",list1[i])


print("delete the element from the list")
del list1[1]
print(list1)

print("remove the element from the list")
list1.remove(3)
print(list1)


print("append the element in the list")
list1.append(4)
print(list1)


print("insert the element in the list")
list1.insert(2,5)   
print(list1)


print("pop the element from the list")
list1.pop(2)
print(list1)


print("extend the element in the list")
list1.extend([6,7,8])
print(list1)