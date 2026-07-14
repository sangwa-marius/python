def add_any(*numbers):
    return sum(numbers)

def describe(**dict):
    for key , value in dict.items():
        print(f"{key} : {value} ")

print(add_any(1,4,3,5,7,2,3))
describe(name="Sangwa Marius",age = 2, role="Backend Engineer")