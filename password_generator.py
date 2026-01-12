import random
import string


def generate_password(length,level):
 if level == 1:
  characters = string.ascii_lowercase
 elif level == 2:
  characters = string.ascii_letters + string.digits
 elif level == 3:
  characters = string.ascii_letters + string.digits + string.punctuation
 else:
  print("Invalid choice")
 password =""
 for i in range(length):
  password += random.choice(characters)
 return password

print("Here are the choices to generate your password:")
print("1. Easy")
print("2. Medium")
print("3. Strong")

level = int(input("Enter the level of your choice (1-3): "))
length = int(input("Enter the length: "))
print("Your password is ready", generate_password(length,level))
