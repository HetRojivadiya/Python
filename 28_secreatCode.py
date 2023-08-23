str = "abcdefghu47"

if(len(str)<=3):
    enc = str[::-1]
else:
    enc = str[3:]
    enc += str[0:3]

print(enc)

if(len(enc) <= 3):
    dec = enc[::-1]
else:
    dec = enc[-3:]
    dec += enc[:-3]
    
print(dec)