class Calculator:
    
    @staticmethod
    def add (*numbers):
        return sum(numbers)
    
sum = Calculator.add(3,4,5)
print(sum)