def add(a,b):
    sum = a + b
    prod = a * b
    quo = a / b
    diff = a - b
    return sum , prod, quo, diff


sum, prod, quo, diff = add(2,3)    
print(sum,prod, quo, diff)