class employee:
    name = "het"
    salary = "100000000000"
    city = "Los Angeles"
    
    def info(self):                                         #reference to the current object to the class
        print(f"salary of {self.name} is {self.salary}")
    
a = employee()
b = employee()

b.name = "Ansh"
b.salary = "20000000000"
b.city = "New York"

print(a.name , a.salary , a.city)
a.info()
b.info()
    