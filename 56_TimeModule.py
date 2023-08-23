import time

# def forLoop():
#     for i in range(5000):
#         print(i)
        
# def whileLoop():
    
#     i=0
#     while i<5000:
#         print(i)
#         i+=1
    
# init = time.time()
# forLoop()
# time1=time.time()-init
# whileLoop()
# time2 = time.time()-init

# print(f"Time 1 : {time1} and Time 2: {time2}")


# print(4)
# time.sleep(3)
# print("this is Printed after 3 seconds")


t = time.localtime()

formate = time.strftime("%Y-%m-%d %H:%M:%S" , t)

print("formated time :",formate)