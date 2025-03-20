dic = {101:"rahul",102:"raj",103:"sonam",104:"rani",105:"rajesh"}

print("before modify : ",dic)
print(id(dic))

dic[100] = "python"

print("after modify : ",dic)
print(id(dic))

print(dic.keys())
print(dic.values())

print(dir(dic))
