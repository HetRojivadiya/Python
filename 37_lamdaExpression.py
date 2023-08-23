def double(cube,x):
    return cube(x)


# double = lambda x: x*2      #mini functions 
cube = lambda x : x*x*x

# avg = lambda x,y : (x+y)/2    #multi parameter

# print(double(5))
# print(cube(5))
# print((avg(5,7))
print(double(cube,5))