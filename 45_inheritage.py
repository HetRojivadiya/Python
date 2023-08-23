class Emp:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def show(self):
        print(f"The name of employee {self.id} is {self.name}")
        
class Programmer(Emp):
    def showLan(self):
        print("The default programmer laguage is Python")
    
a= Emp("het",3223)
a.show()

b=Programmer("ansh",3222)
b.showLan()
b.show()

