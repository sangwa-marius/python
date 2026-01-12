
def power_function(exponent):
  def inner(x):
    return x ** exponent
  return inner

def base_exponent(base,exp):
  return base ** exp

square = power_function(2)
cube = power_function(3)
while True:
 print ("Hello ! are you ready to calculate?\nChoose in the list below:")
 print ("1. square")
 print ("2. Cube")

 while True:
  choice = int(input("Enter your choice 1 or 2: "))
  if choice == 1 or choice ==2:
   break
  else:
   print ("Please input the valid choice!")

 user_input = int(input("Enter the number: "))
 if choice == 1:
  square = square(user_input)
  print (f"The square of {user_input} is {square}")

 else:
  cube = cube(user_input)
  print (f"The cube of {user_input} is {cube}")

 print ("Now let's make it more advanced:")

 base = float(input("Enter the base: "))
 exp = float(input("Enter the exponent: "))

 result = base_exponent(base,exp)

 print(f"The power of {base} to {exp} is {result:.3f}")
 cont = input('Do you want to continue calculating? [y/n]')
 if cont =='n' or cont =='N':
  break
 else:
  print("Let's continue witht our calculations..")
