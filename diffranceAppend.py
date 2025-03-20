a =  [1,2,3,4]
b = [1,2]

c =[]

for i in a:
    if i not in b:
        c.append(i)
print(c)