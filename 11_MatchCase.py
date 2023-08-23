x=int(input())

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case _ if(x<0):
        print("x is negative")
        print(x)
    case _ if(x>0):
        print("x is positive")
        print(x)