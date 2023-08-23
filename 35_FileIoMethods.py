# f = open('myfile.txt','r')

# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break;

f = open('myfile.txt','w')
lines = ['hello het\n','you need to upgrade your self consistensly']
f.writelines(lines)


