l = list(str(input()))
s = str()
print(s)
l.reverse();
flag =True;

for i in range(len(s)):
    print(s[i],l[i])
    if(s[i]!=l[i]):
        flag=False;
        
if flag==True:
    print("palindrome")
else:
    print("Not Palindrome");
