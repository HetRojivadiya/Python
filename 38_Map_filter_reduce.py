def cube(x):
    return x*x*x
    
l = [1,2,3,4,5]

# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

#Map
newl = list(map(cube,l))    #cube or  lambda x:x*x*x
print(newl)



#Filter
def filter_function(a):
    return a>2
    
new = list(filter(filter_function , l))  
print(new)

#Reduce

from functools import reduce

numbers = [1,2,3,4,5,6,7]

def mysum(x,y):
    return x+y

sum = reduce(mysum,numbers)
print(sum)










