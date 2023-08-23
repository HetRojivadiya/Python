class Emp:
    company_name = "apple"    #class Variable
    
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.8   
        
    def show(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.company_name} is {self.raise_amount}")
 
        
e = Emp("het")
e.company_name = "Google"  #instance variable
Emp.show(e)  #e.show()

e1 = Emp("ansh")   
Emp.show(e1)  #e.show()

