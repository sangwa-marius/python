class Dataset:
    
    library = "Pandas"
    
    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns
        
    @staticmethod
    def validate_size(size):
        print(size)
        
    @classmethod
    def change_library(cls, new_library):
        cls.library = new_library
        

    def display(self):
        print(self.name ,self.rows, self.columns)
        


Dataset.validate_size(345)