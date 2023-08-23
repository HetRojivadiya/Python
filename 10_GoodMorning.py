import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
 
if(int(time.strftime('%H')) >= 0 and int(time.strftime('%H')) <12):
    print("good morning")
elif(int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) <18):
    print("good afternoon")
elif(int(time.strftime('%H')) >= 18 and int(time.strftime('%H')) < 21):
    print("good evening")
else:
    print("good night")
    
