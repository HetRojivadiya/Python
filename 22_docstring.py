#docstring : that is appear right after the definition of a function ,method ,class , module

def square(n):
    '''Takes in a number n, returns the square of n'''    #NOTE: it it defines after the definition of a function
    print(n*n)

square(5)

print(square.__doc__)