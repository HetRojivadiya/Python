with open('myfile.txt','r') as f:
    f.seek(15)     #read from 15 bytes
    print(f.read())
    print(f.tell())  #last cursor position
    
    f.truncate(3)  #truncate to 30 bytes