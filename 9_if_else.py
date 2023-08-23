a = input("enter your age :")

print("your age is :",a)

# if else


# if(int(a)>18):
#     print("You can drive")
# else:
#     print("You can not drive")

# elif

# if(int(a) == 0):
#     print("Number is zero")
# elif(int(a) > 0):
#     print("Number is Positive")
# else:
#     print("Number is Negative")

# nested if

if(int(a) >= 0):
    if(int(a)==1):
        print("congratulation")
    else:
        print("Sorry")
else:
    print("hahahahahaha")



a= 10
b= 20

print("A") if a>b else print("B") if a==b else print("B")

c = 9 if a>b else 0
print(c)