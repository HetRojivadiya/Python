import os

# if(not os.path.exists("data")):
#     os.mkdir("data")
#     for i in range(0,100):
#          os.mkdir(f"data/Data{i+1}")
    

# for i in range(0,100):
#     os.rename(f"data/Data{i+1}",f"data/Tutorial{i+1}")
    
folder = os.listdir("data")

print(folder)

for folders in folder:
    print(folders)
    print(os.listdir(f"data/{folders}"))