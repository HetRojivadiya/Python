a = 4
b = 4

c = [1,2,3]
d = [1,2,3]

print(a is b) # exact location of object in memory      
#true
print(a == b)
#true

print(c is d) # exact location of object in memory
#false
print(c == d)
#true