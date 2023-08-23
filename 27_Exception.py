a = 10
b = 0

try:
    c = a/b
except Exception as e:
    print("Error is occures :",e)
finally:
    print("hahaha")    # specially defined in function

if(a!=5):
    raise ValueError("value of A is not 5")


