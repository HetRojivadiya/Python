class MyClass:
    def __init__(self,value):
        self.value = value
        
    def show(self):
        print(f"Value is {self.value}")
     
    @property
    def het(self):
        return self.value
      
    @het.setter
    def het(self, new_value):
        self.value = new_value
    
obj = MyClass(10)
obj.het = 100
obj.show()