def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using This Function")
    return mfx

@greet
def hello():
    print("hello world")
    
#@greet
def add(a,b):
    print(a+b)
    
    
hello()            # first hello pass to greet function and greet function decorate the function and return function

greet(add)(1,2)