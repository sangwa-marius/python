class Employee:
    
    company = "Google"
    
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        
    def show_info(self):
        print(self.name,self.salary);