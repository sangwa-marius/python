person ={
    "name":"Marius",
    "age":23,
    "role":"Software engineer",
    "school":"Rwanda coding academy"
}

person["university"]="MIT"
print(person)

for key , value in person.items():
    print(f"{key} => {value}")