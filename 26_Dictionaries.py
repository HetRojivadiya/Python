dic = {
    "het" : "human being",
    "spoon" : "Object"
}

print(dic)
print(dic["het"])     #error
print(dic.get("het"))  # not error if value is not available

for key in dic.keys():
    print(key,dic[key])
    
for key in dic.values():
    print(key)
    
#print(dic.items())

for key,value in dic.items():
    print(f"the value corrosponding to the key {key} is {value}")
    
    
    
    
    
    
    
    
    
    
    