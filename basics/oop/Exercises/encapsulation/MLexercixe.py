class Dataset:
    
    def __init__(self):
        self.__samples = 34
        
    
    @property
    def samples(self):
        return self.__samples
    
    @samples.setter
    def samples(self, samples):
        if (samples >= 0):
            self.__samples = samples
        else:
            raise ValueError("Samples should be greater than 0")
            

dataset1 = Dataset()

dataset1.samples=0