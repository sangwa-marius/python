class Model:
    
    def __init__(self,name):
        self.name = name
        self.accuracy = 0
        
    def train(self):
        print(self.name, "is training....")
        
    def evaluate(self):
            print("Accuracy:", self.accuracy)
            

model1 = Model("Neural Network")
model1.accuracy = 99
model1.train()
model1.evaluate()