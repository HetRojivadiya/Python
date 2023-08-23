def Generator():
    for i in range(5):
        yield i
        
gen = Generator()

# print(next(gen))

for j in gen:
    print(j)
    
#Generator : main application of the generator that allows you to generate values on the fly rather than store the entire sqeuence in memory.

