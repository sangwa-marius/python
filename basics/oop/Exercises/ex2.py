class Dataset:
    
    def __init__(self,name,size,features):
        self.name = name
        self.size = size
        self.features = features
        

    def show_info(self):
        print("Dataset:",self.name)
        print("Samples:",self.size)
        print("Features:", self.features)
        


dataset1 = Dataset("House prices",689,23)
dataset1.show_info()