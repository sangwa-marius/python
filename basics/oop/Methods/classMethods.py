    
"""Class Methods work with class variables"""


class Student:
    
    school  = "University of Rwanda" # class variable
    @classmethod
    def change_school(cls, new_school): # class method
        cls.school = new_school
        
    @classmethod
    def show_school(cls):
        print(cls.school)
        
    def __init__(self,name, age, home_address):
        self.name = name # instance variable
        self.age = age   # instance variable
        self.home_address = home_address # instance variable
        
    def intro(self): # instance method
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")
        


class Model:
    
    framework = "PyTorch"
    
    @classmethod 
    def show_framework(cls):
        print(cls.framework)

        
Student.change_school("Mount Kenya University")
Student.show_school()

student1 = Student("Marius",23,"Gatsibo")
student1.school = "dkfjd"
Student.show_school()
print(student1.school)

Model.show_framework()