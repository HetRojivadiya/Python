# names ="het,ansh"

# namesLength = len(names)
# print("names length:",namesLength)

# print(names[0:3])
# print(names[:3])
# print(names[:-1])     # [0 : len(names)-1]
# print(names[-2:])     # [len(names)-2 : len(names)]


# str = "heth"
# position=3
# char = 'r'

string ="ABCDCDC"
sub_string="CDC" 



count = 0
for i in range(len(string)):
    if(string[i]==sub_string[0]):
    
        if(string[i:i+len(sub_string)]==sub_string):
            count=count+1
            
print(count)