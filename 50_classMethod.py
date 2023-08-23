class Employee:
    company = "Apple"
    
    def show(self):
        print(f"Company : {self.company}")
     
    @classmethod                       # if we want to change class variable then it is use
    def changeCompany(cls,newCompany):
        cls.company = newCompany

e =Employee()
print(Employee.company)  
e.show()
e.changeCompany("Tesla")
e.show()
print(Employee.company)  
