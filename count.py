a=[1,1,2,2,3,3,4,4,5,5,10]
b=[]

for i in a:
    if (a.count(i)>1):
        pass
    else:
        b.append(i)
print(b)