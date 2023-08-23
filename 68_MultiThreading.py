import threading
import time
from concurrent.futures import ThreadPoolExecutor


def fun(seconds):
    time.sleep(seconds)
    print(f"Slepping for {seconds} seconds")
    
# fun(4)  Normal code
# fun(2)

def main():
    time1 = time.perf_counter()
    #same code using threrad

    t1 = threading.Thread(target=fun, args=[4])
    t2 = threading.Thread(target=fun, args=[2])

    t1.start()
    t2.start()


    # time2 = time.perf_counter()
    # print(time2-time1)
    # t1.join()     #agar ap rukna chahte ho thread khatam hone ke liye tab app join method ka use kar sakte ho
    # t2.join()

    time2 = time.perf_counter()
    print(time2-time1)
    
def pooling():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(fun , 4)
        future2= executor.submit(fun , 1)
        future3= executor.submit(fun , 2)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        

pooling()   # real world Project executionpool
#main()     #normal Thread execution