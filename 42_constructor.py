class employee:
    def __init__(self,name,salary,city):
        self.name = name
        self.salary = salary
        self.city = city

    def info(self):                  # self is must be required in any methods of python                                 
        print(f"salary of {self.name} is {self.salary}")
        
a = employee("Het","2000000000000","New York")      # self is passed as =>  a
b = employee("Ansh","1000000000000","Los Angeles")

a.info()
b.info()
    
    
    