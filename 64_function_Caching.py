#function cache : some big calculation of one digit like 2 in a function call it's store the answer
# when another time also same function call for same value 2 then it will directly return from cache
#it will not execute hole function so that's why time is save.


import functools
import time

@functools.lru_cache(maxsize=None)        #when use : when you know some your function is called same value multiple times else it will expensive respective to memory
def fx(n):
    time.sleep(5)    # assuming big calculations takes time 5 seconds
    return n*5

print(fx(5))
print("Done for n = 5")
print(fx(2))
print("Done for n = 2")

print(fx(5))
print("Done for n = 5")