name = ("het","ansh","arjun","vatsal","dev")

temp = list(name)
temp.append("deeti")
name = tuple(temp)

print(name)


tup = (1,2,3,5,1,6)
print(tup.count(1))

#print(tup.index(1))
print(tup.index(1,3,5))   # 1 index return between   3 to 5 indices
