# class Parent:
#     def parent_method(self):
#         print("This is Parent method")

# class Child(Parent):
    
#     def child_method(self):
#         print("This is Child method")
        
#     def parent_method(self):           #method overriding
#         print("het")
#         super().parent_method()
        
# obj = Child() 

# obj.child_method()
# obj.parent_method()


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    
    def __init__(self,name,id,lang):
        #self.name = name
        #self.id = id
        super().__init__(name,id)
        self.lang = lang
        
e = Employee("ansh",321)
p = Programmer("het",123,"Python")

print(p.id)
print(p.name)
print(p.lang)
        
    

