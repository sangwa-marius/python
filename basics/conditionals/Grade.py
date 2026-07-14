marks = float(input("Enter your marks: "))
grade = ''

if (marks <0 or marks > 100 ):
    print("Marks out or bounds")
elif(marks >= 90):
    grade ='A'
elif(marks >=80):
    grade = 'B'
elif(marks >= 70):
    grade ='C'
elif(marks >= 60):
    grade = 'D'
else:
    grade = 'F'


print(f"Your marks are {marks} and your grade is {grade}")
    
    
    