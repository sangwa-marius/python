class Vehicle:
    
    def __init__(self,name):
        self.name = name;
        
    def start(self):
        print(self.name, "is Starting")
        
    
    def stop(self):
        print(self.name, "is Stopping")
        

class Car(Vehicle):
    
    def __init__(self,name):
        super().__init__(name)
    
    def drive(self):
        print(self.name ,"is Driving")


Car("Imodoka").start()
Car("ikankari").stop()