#a = True

print(a:=True)    #first python assign a to true and after print it
print(b:=False)

foods = list()

while (food := input("enter food : ")) != "quit":
    foods.append(food)
    
print(foods)