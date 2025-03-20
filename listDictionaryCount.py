str = "AVINASHMARKAD"

dict = {}

for elements in str:
    if elements in dict:
        dict[elements] += 1
    else:
        dict[elements] = 1
print(dict)