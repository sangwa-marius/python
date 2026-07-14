correctPassword = "sanMariento"

password = input("Enter password: ")

while(password != correctPassword):
    password = input("Enter password: ")
    
print("Access granted" +"\n")

fruits = ["Orange", "Banana","cherry"]
for idx, fruit in enumerate(fruits):
    answer= input(f"Do you like {idx + 1}. {fruit}? (yes/no)")
    if (answer == "yes"):
        print(f"ooh! I love  {fruit} too\n")
    elif(answer == "no"):
        print(f"oops why don't you like {fruit}?\n")
    else:
        print("Invalid answer\n")
        
        
number = int(input("Enter a number which is not negative: "))

for i in range(1,13):
    print(f"{i} x {number} = {i * number}")
    

