import os

global num
num = 1

def changer(filename,num):
    s = str(num)
    os.rename(f"IMAGES/{filename}",f"IMAGES/{s}.png")

folder = os.listdir("IMAGES")

for folders in folder:
    print(folders)
    changer(folders,num)
    num+=1
    
f = os.listdir("IMAGES")

for f1 in f:
    print(f1)
    
