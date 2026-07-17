class Student:
    def __init__(self, name, school, age):
        self.age = age
        self.name = name
        self.school = school
        
        
    def introduce(self):
        print(f"Hello, my name is {self.name} and I study at {self.school}")    
        


student1 = Student("Sangwa Marius","Rwanda  Coding Academy",45)
student1.introduce()

