class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
        

    def display_info(self):
        print(self.brand, self.model, self.year)
    

car1 = Car("Toyota","Corolla", 2001)
car1.display_info()