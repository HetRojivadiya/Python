#string are immutable  

a = "Het!!!!! !!!!"
print(a.upper())
print(a.lower())

print(a.rstrip("!"))   # remove leading !

print(a.replace("Het","ansh"))

print(a.split(" ")[0])


print(a[0])

heading = "instroduce tO jS"
print(heading.capitalize())

print(heading.center(50))

print(a.count("!"))

print(a.endswith("!"))
print(a.endswith("!" , 2 ,5))

print(heading.find("tO"))    #if any word is not present then it will return -1

print(heading.index("jS"))  #if any word is not present then it will return error

str = "welcome"
print(str.isalpha())  # all string is alphabetic

print(str.islower())  # all string is in lowercase 

print(str.isprintable())  # if \n then it returns false

print(str.istitle()) 



